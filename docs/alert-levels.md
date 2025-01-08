# Enterprise Security Alert Classification and Response Matrix

## Alert Level Categories (MITRE ATT&CK Aligned)

### CRITICAL: Emergency Response Alerts (Level 12-15) → #security-emergency
- **Level 15**: Active APT/Nation-State Actor Detection
  - Command & Control (C2) traffic detected
  - Data exfiltration in progress
  - Domain Generation Algorithm (DGA) activity
  - Cobalt Strike beacon detection
  - Living-off-the-land binaries (LOLBins) abuse

- **Level 14**: Active Exploitation
  - Zero-day vulnerability exploitation
  - Remote Code Execution (RCE) attempts
  - Buffer overflow attacks
  - SQL injection attacks
  - Cross-site scripting (XSS) attacks

- **Level 13**: Critical Infrastructure Compromise
  - Domain Admin credential compromise
  - Golden/Silver Ticket attacks
  - Pass-the-Hash attacks
  - Kerberoasting attempts
  - Active directory replication attacks

- **Level 12**: Advanced Malware Detection
  - Ransomware indicators
  - Fileless malware detection
  - PowerShell Empire framework
  - Metasploit framework activity
  - Memory-resident malware

**Response Protocol**: 
- IMMEDIATE: Maximum 15-minute response time
- SOC Level 3 engagement
- CIRT team activation
- Executive notification
- Potential system isolation

### HIGH: Critical Security Alerts (Level 9-11) → #security-critical
- **Level 11**: Lateral Movement Indicators
  - SMB enumeration
  - WMI exploitation
  - PsExec usage
  - Remote PowerShell execution
  - Suspicious RDP connections

- **Level 10**: Privilege Escalation Attempts
  - UAC bypass attempts
  - Scheduled task manipulation
  - Service manipulation
  - DLL hijacking
  - Token manipulation

- **Level 9**: Reconnaissance Activities
  - Port scanning
  - Network enumeration
  - DNS reconnaissance
  - LDAP queries
  - Email harvesting

**Response Protocol**:
- URGENT: 1-hour response time
- SOC Level 2 investigation
- Incident tracking required
- Team lead notification

### MEDIUM: Security Alerts (Level 6-8) → #security-alerts
- **Level 8**: Policy Violations
  - Unauthorized software installation
  - GPO modification attempts
  - Firewall rule changes
  - Certificate policy violations
  - Data classification violations

- **Level 7**: System Integrity Issues
  - Registry modifications
  - Boot sector alterations
  - Driver installations
  - Service configurations
  - Scheduled task creation

- **Level 6**: Authentication Events
  - Failed login attempts
  - Password policy violations
  - MFA failures
  - Session timeout violations
  - Account lockouts

**Response Protocol**:
- Standard: 8-hour response time
- SOC Level 1 review
- Daily review cycle
- Weekly reporting

### LOW: Informational Security Events (Level 3-5) → #security-info
- **Level 5**: System Changes
  - Software updates
  - Patch installations
  - Configuration changes
  - User permission modifications
  - Group membership changes

- **Level 4**: Compliance Monitoring
  - Asset inventory changes
  - License compliance
  - Policy acknowledgments
  - Training completion
  - Access reviews

- **Level 3**: Routine Scanning Activities
  - Basic security events
  - Non-critical system alerts

**Response Protocol**:
- Routine: 24-hour review cycle
- Automated analysis
- Monthly reporting
- Trend analysis

## SIEM Integration Matrix

### Splunk SIEM (Critical Assets)
- Levels 12-15: Real-time forwarding
- Levels 9-11: Near real-time (5-minute delay)
- Custom correlation rules
- Threat hunting dashboards
- IOC matching

### Wazuh SIEM (All Assets)
- All levels monitored
- FIM monitoring
- Compliance checking
- Vulnerability detection
- Behavioral monitoring

### TheHive Integration
- Automatic case creation (Levels 9-15)
- Automated playbook triggering
- MITRE ATT&CK mapping
- IOC extraction
- Threat intelligence correlation

## Incident Response Integration

### SOC Team Engagement
- L3 Analysts: Levels 12-15
- L2 Analysts: Levels 9-11
- L1 Analysts: Levels 6-8
- SOC Operators: Levels 3-5

### Automated Response Actions
- Network isolation (Levels 12-15)
- Asset quarantine (Levels 11-15)
- Account suspension (Levels 10-15)
- EDR response actions (Levels 8-15)
- SOAR playbooks (All levels)

### Notification Matrix
- SMS/Call: Levels 12-15
- Email + Slack: Levels 9-11
- Slack only: Levels 6-8
- Dashboard: Levels 3-5

## Threat Intelligence Correlation
- MISP integration
- AlienVault OTX
- VirusTotal Enterprise
- IBM X-Force
- Recorded Future

## Compliance Mapping
- MITRE ATT&CK Framework
- NIST Cybersecurity Framework
- ISO 27001
- CIS Controls
- PCI DSS
- HIPAA (if applicable)
- SOX (if applicable)

## Alert Level Standardization

### Severity Levels

### Level 3-5: Low
- Basic security events
- Non-critical system alerts
- Routine scanning activities
- Example: Failed login attempts (< 3)

### Level 6-8: Medium
- Suspicious activities
- Multiple failed authentications
- Unauthorized access attempts
- Example: HoneyPot access attempts

### Level 9-11: High
- Active intrusion attempts
- Malware detection
- Data exfiltration attempts
- Example: RITA beacon detection

### Level 12-15: Critical
- Confirmed breaches
- Active ransomware
- Critical system compromise
- Example: HoneyCred admin access

## Tool-Specific Mappings

### Wazuh
- Low: 3-5
- Medium: 6-8
- High: 9-11
- Critical: 12-15

### BitDefender EDR
- Low: 3
- Medium: 7
- High: 10
- Critical: 13

### Suricata
- Low: 3
- Medium: 7
- High: 10
- Critical: 13

### RITA
- Beacon Score < 0.3: Level 3
- Beacon Score 0.3-0.7: Level 7
- Beacon Score 0.7-0.9: Level 10
- Beacon Score > 0.9: Level 13

### PacketFence
- Warning: Level 3
- Minor: Level 7
- Major: Level 10
- Critical: Level 13

## Integration Points

### TheHive Case Creation
- Level 3-5: Low priority (P4)
- Level 6-8: Medium priority (P3)
- Level 9-11: High priority (P2)
- Level 12-15: Critical priority (P1)

### Slack Notifications
- Level 3-5: #security-info
- Level 6-8: #security-alerts
- Level 9-11: #security-critical
- Level 12-15: #security-critical + @security-team
