# Network Architecture

## Overview
```mermaid
graph TD
    subgraph Internet
        ext[External Traffic]
    end

    subgraph DMZ [DMZ Network - 10.0.1.0/24]
        fw[Firewall]
        ids[Suricata IDS]
        hp[HoneyPot Network]
    end

    subgraph Internal [Internal Network - 10.0.0.0/24]
        subgraph Security Infrastructure
            wazuh[Wazuh SIEM]
            splunk[Splunk]
            thehive[TheHive]
            rita[RITA]
        end

        subgraph Access Control
            nvis[NVIS ZTNA]
            pf[PacketFence NAC]
        end

        subgraph Endpoint Protection
            bd[BitDefender EDR]
            action1[Action1 MRR]
        end
    end

    subgraph HoneyNet [HoneyNet - 10.0.2.0/24]
        hpftp[FTP Honeypot]
        hpsmb[SMB Honeypot]
        hprdp[RDP Honeypot]
        tokens[Canary Tokens]
    end

    ext --> fw
    fw --> ids
    ids --> Internal
    ids --> hp

    hp --> hpftp
    hp --> hpsmb
    hp --> hprdp
    hp --> tokens

    %% Security Infrastructure Connections
    ids --> wazuh
    rita --> wazuh
    wazuh --> splunk
    wazuh --> thehive

    %% Access Control Connections
    nvis --> Internal
    pf --> Internal

    %% Endpoint Protection
    bd --> wazuh
    action1 --> wazuh

classDef network fill:#f9f,stroke:#333,stroke-width:2px;
classDef security fill:#bbf,stroke:#333,stroke-width:2px;
classDef honeypot fill:#ffb,stroke:#333,stroke-width:2px;

class DMZ,Internal,HoneyNet network;
class wazuh,splunk,thehive,rita,ids security;
class hpftp,hpsmb,hprdp,tokens honeypot;
```

## Network Segments

### DMZ Network (10.0.1.0/24)
- Suricata IDS for network monitoring
- Initial honeypot access points
- Firewall controls

### Internal Network (10.0.0.0/24)
- Security monitoring infrastructure
- Access control systems
- Endpoint protection management

### HoneyNet (10.0.2.0/24)
- Isolated honeypot network
- Deception technology
- Canary tokens

## Security Components

### Monitoring & Detection
- Wazuh SIEM: Central security monitoring
- Splunk: Log analysis and visualization
- RITA: Network traffic analysis
- Suricata IDS: Network intrusion detection

### Access Control
- NVIS ZTNA: Zero Trust access control
- PacketFence: Network Access Control

### Endpoint Security
- BitDefender EDR: Endpoint detection and response
- Action1 MRR: Remote management

### Deception
- HoneyPots: FTP, SMB, RDP services
- Canary Tokens: Tracking documents and credentials
