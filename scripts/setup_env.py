#!/usr/bin/env python3
import os
import yaml
import json
from pathlib import Path

def load_env_template():
    """Load environment variables from template"""
    env_vars = {}
    with open('../.env.template', 'r') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key = line.split('=')[0].strip()
                env_vars[key] = os.getenv(key, '')
    return env_vars

def convert_json_to_yaml(json_file, yaml_file):
    """Convert JSON config to YAML format"""
    with open(json_file, 'r') as f:
        config = json.load(f)
    
    with open(yaml_file, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)
    
    # Backup original JSON file
    json_file.rename(json_file.with_suffix('.json.bak'))

def update_config_files(env_vars):
    """Update configuration files with environment variables"""
    config_dir = Path('../configs')
    
    # Convert JSON configs to YAML
    json_configs = list(config_dir.rglob('*.json'))
    for json_file in json_configs:
        yaml_file = json_file.with_suffix('.yaml')
        print(f"Converting {json_file} to YAML format")
        convert_json_to_yaml(json_file, yaml_file)
    
    # Update all YAML configs with environment variables
    yaml_configs = list(config_dir.rglob('*.yaml'))
    for config_file in yaml_configs:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
            
        # Recursively update environment variables
        def update_env_vars(data):
            if isinstance(data, dict):
                return {k: update_env_vars(v) for k, v in data.items()}
            elif isinstance(data, list):
                return [update_env_vars(item) for item in data]
            elif isinstance(data, str) and data.startswith('${') and data.endswith('}'):
                env_var = data[2:-1]
                return env_vars.get(env_var, data)
            return data
        
        config = update_env_vars(config)
        
        with open(config_file, 'w') as f:
            yaml.dump(config, f, default_flow_style=False)

def main():
    """Main function to setup environment"""
    print("Loading environment variables...")
    env_vars = load_env_template()
    
    print("Updating configuration files...")
    update_config_files(env_vars)
    
    print("Environment setup complete!")

if __name__ == "__main__":
    main()
