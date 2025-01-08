# Deployment Guide

## Prerequisites

### Hardware Requirements
- **SIEM Servers**: 
  - 16+ CPU cores
  - 64GB+ RAM
  - 2TB+ storage
- **EDR Management**:
  - 8+ CPU cores
  - 32GB+ RAM
  - 1TB+ storage
- **Network Infrastructure**:
  - 10Gbps network capacity
  - Redundant connections
  - Load balancers

### Software Requirements
- **Operating Systems**:
  - RHEL/CentOS 8+ for servers
  - Windows 10/11 for endpoints
  - Ubuntu 20.04+ for containers
- **Virtualization**:
  - VMware ESXi 7.0+
  - Docker 20.10+
  - Kubernetes 1.22+

### Licenses & Subscriptions
- BitDefender GravityZone Ultra Plus
- Action1 RMM Enterprise
- NVIS SDP Enterprise
- Splunk Enterprise Security
- Wazuh Enterprise
- TheHive Project

## Deployment Steps

### 1. Core Infrastructure Setup

#### Network Segmentation
```bash
# Configure VLANs
vlan create id 100 name "Security-Tools"
vlan create id 101 name "Endpoints"
vlan create id 102 name "Servers"

# Configure routing
ip route add security-tools vlan 100
ip route add endpoints vlan 101
ip route add servers vlan 102
```

#### Firewall Rules
```bash
# Allow SIEM traffic
firewall-cmd --permanent --add-port=514/tcp
firewall-cmd --permanent --add-port=1514/tcp
firewall-cmd --permanent --add-port=1515/tcp

# Allow EDR communication
firewall-cmd --permanent --add-port=8443/tcp
firewall-cmd --permanent --add-port=443/tcp
```

### 2. SIEM Deployment

#### Wazuh Server
```bash
# Install Wazuh
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | gpg --no-default-keyring --keyring gnupg-ring:/usr/share/keyrings/wazuh.gpg --import && chmod 644 /usr/share/keyrings/wazuh.gpg
echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | tee -a /etc/apt/sources.list.d/wazuh.list
apt-get update
apt-get install wazuh-manager
```

#### Splunk Enterprise
```bash
# Deploy Splunk
wget -O splunk-8.2.6-a6fe1ee8894b-Linux-x86_64.tgz 'https://download.splunk.com/products/splunk/releases/8.2.6/linux/splunk-8.2.6-a6fe1ee8894b-Linux-x86_64.tgz'
tar xvzf splunk-8.2.6-a6fe1ee8894b-Linux-x86_64.tgz -C /opt
/opt/splunk/bin/splunk start --accept-license
```

### 3. Endpoint Security

#### BitDefender Deployment
```powershell
# Deploy BitDefender
$installerPath = "\\deployment\software\BitDefender\installer.exe"
$arguments = "/quiet INSTALLDIR=`"C:\Program Files\BitDefender`" /log `"C:\Windows\Temp\BitDefender_install.log`""
Start-Process -FilePath $installerPath -ArgumentList $arguments -Wait
```

#### Action1 RMM
```powershell
# Deploy Action1
$action1Installer = "\\deployment\software\Action1\setup.exe"
$arguments = "/silent /install /norestart"
Start-Process -FilePath $action1Installer -ArgumentList $arguments -Wait
```

### 4. Zero Trust Implementation

#### NVIS SDP
```bash
# Install NVIS Controller
docker pull nvis/controller:latest
docker run -d --name nvis-controller \
  -p 443:443 \
  -v /etc/nvis:/etc/nvis \
  nvis/controller:latest

# Deploy NVIS Gateway
docker pull nvis/gateway:latest
docker run -d --name nvis-gateway \
  -p 8443:8443 \
  -v /etc/nvis:/etc/nvis \
  nvis/gateway:latest
```

### 5. Integration Setup

#### TheHive Deployment
```bash
# Deploy TheHive
docker pull thehive-project/thehive4:latest
docker run -d --name thehive \
  -p 9000:9000 \
  -v /opt/thp/thehive/data:/opt/thp/thehive/data \
  -v /opt/thp/thehive/index:/opt/thp/thehive/index \
  thehive-project/thehive4:latest
```

#### Slack Integration
```bash
# Configure Slack webhook
curl -X POST -H 'Content-type: application/json' \
--data '{"text":"Security Infrastructure Online"}' \
https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

## Post-Deployment Verification

### 1. Security Checks
```bash
# Verify SIEM connectivity
nc -vz wazuh-server 1514
nc -vz splunk-server 8089

# Check EDR status
curl -k https://bitdefender-server:8443/status
curl -k https://action1-server:443/health
```

### 2. Integration Tests
```bash
# Test Wazuh-Splunk integration
/var/ossec/bin/agent_control -ls
splunk search "source=wazuh"

# Test TheHive integration
curl -XPOST -H "Content-Type: application/json" http://thehive:9000/api/alert -d @test-alert.json
```

### 3. Performance Monitoring
```bash
# Monitor SIEM performance
top -p $(pgrep -d',' -f ossec)
splunk btool check

# Check network latency
ping -c 100 wazuh-server | awk -F/ '/^rtt/ { print $5 }'
```

## Troubleshooting

### Common Issues

1. **SIEM Connection Issues**
```bash
# Reset Wazuh manager
systemctl restart wazuh-manager
tail -f /var/ossec/logs/ossec.log

# Verify Splunk forwarder
/opt/splunkforwarder/bin/splunk list forward-server
```

2. **EDR Problems**
```powershell
# Check BitDefender service
Get-Service | Where-Object {$_.Name -like "*BitDefender*"}
Restart-Service BitDefenderAgent

# Verify Action1 connectivity
Test-NetConnection -ComputerName action1-server -Port 443
```

3. **Integration Failures**
```bash
# Check TheHive logs
docker logs thehive
journalctl -u thehive

# Verify Slack webhooks
curl -X POST -H "Content-Type: application/json" \
  -d '{"text":"test"}' \
  https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

## Maintenance Procedures

### Daily Checks
- Monitor SIEM event flow
- Verify EDR agent health
- Check integration status
- Review alert queues

### Weekly Tasks
- Update threat intelligence
- Tune detection rules
- Backup configurations
- Review performance metrics

### Monthly Procedures
- Patch security tools
- Update compliance reports
- Review access policies
- Test recovery procedures

## Security Metrics

### Key Performance Indicators
- Mean Time to Detect (MTTD)
- Mean Time to Respond (MTTR)
- False Positive Rate
- Agent Health Status
- Event Processing Rate

### Compliance Metrics
- Policy Compliance Rate
- Patch Compliance
- Access Control Compliance
- Incident Response Time

## Documentation & Training

### Required Documentation
- Incident Response Playbooks
- Configuration Standards
- Operating Procedures
- Recovery Plans

### Training Requirements
- SIEM Administration
- EDR Management
- Incident Response
- Threat Hunting
