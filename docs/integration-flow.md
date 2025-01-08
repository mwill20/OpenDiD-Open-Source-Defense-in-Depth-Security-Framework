# Integration Flow

## Data Flow Diagram

```mermaid
graph TD
    %% Data Sources
    subgraph Endpoint Security
        BD[BitDefender EDR]
        A1[Action1 RMM]
    end

    subgraph Network Security
        SU[Suricata IDS]
        PF[PacketFence NAC]
        RT[RITA]
        NV[NVIS ZTNA]
    end

    subgraph Deception
        HP[HoneyPots]
        HC[HoneyCreds]
        CT[Canary Tokens]
    end

    subgraph Central SIEM
        WZ[Wazuh Manager]
        WI[Wazuh Indexer]
        subgraph Playbooks
            PB1[Honeypot Access]
            PB2[HoneyCred Abuse]
            PB3[Ransomware Response]
        end
    end

    subgraph Analysis & Response
        SP[Splunk]
        TH[TheHive]
        subgraph Cases
            C1[Incident Cases]
            C2[Alert Cases]
        end
    end

    subgraph Notification
        SL[Slack Channels]
        EM[Email Alerts]
        subgraph Channels
            SC1[#security-info]
            SC2[#security-alerts]
            SC3[#security-critical]
        end
    end

    %% Data Collection Flows
    BD -->|Malware/EDR L3-13| WZ
    A1 -->|System Events L3-10| WZ
    SU -->|Network IDS L3-13| WZ
    PF -->|NAC Events L3-13| WZ
    RT -->|Beacons L7-13| WZ
    NV -->|Access Events L3-10| WZ
    HP -->|Honeypot Access L7-10| WZ
    HC -->|Cred Abuse L10-13| WZ
    CT -->|Token Alerts L7-13| WZ

    %% SIEM Processing
    WZ -->|Events| WI
    WI -->|Correlated Alerts| PB1
    WI -->|Correlated Alerts| PB2
    WI -->|Correlated Alerts| PB3
    
    %% Analysis Flow
    WI -->|Enriched Data| SP
    WI -->|Incidents L9+| TH
    
    %% Case Management
    TH -->|Creates| C1
    TH -->|Creates| C2
    
    %% Response Actions
    C1 -->|Updates| SP
    C2 -->|Updates| SP
    
    %% Notifications
    SP -->|L3-5| SC1
    SP -->|L6-8| SC2
    TH -->|L9-11| SC3
    TH -->|L12-15| EM

    %% Bidirectional
    SP <-->|Context & Analytics| TH

    %% Styling
    classDef endpoint fill:#f9f,stroke:#333,stroke-width:2px;
    classDef network fill:#bbf,stroke:#333,stroke-width:2px;
    classDef deception fill:#fbf,stroke:#333,stroke-width:2px;
    classDef siem fill:#bff,stroke:#333,stroke-width:2px;
    classDef analysis fill:#bfb,stroke:#333,stroke-width:2px;
    classDef notify fill:#fbb,stroke:#333,stroke-width:2px;
    classDef playbook fill:#fff,stroke:#333,stroke-width:1px,stroke-dasharray: 5 5;
    classDef case fill:#ffe,stroke:#333,stroke-width:1px;
    classDef channel fill:#fee,stroke:#333,stroke-width:1px;

    class BD,A1 endpoint;
    class SU,PF,RT,NV network;
    class HP,HC,CT deception;
    class WZ,WI siem;
    class SP,TH analysis;
    class SL,EM notify;
    class PB1,PB2,PB3 playbook;
    class C1,C2 case;
    class SC1,SC2,SC3 channel;
```

## Alert Flow

1. **Data Collection (L3-13)**
   - **Endpoint Security**
     * BitDefender EDR: Malware, exploits, suspicious behavior
     * Action1 RMM: System events, patch status, compliance
   - **Network Security**
     * Suricata IDS: Network intrusions, protocol anomalies
     * PacketFence: Access control, device profiling
     * RITA: Beaconing, long connections, data transfer
     * NVIS: Zero-trust access events
   - **Deception Technology**
     * HoneyPots: Service access, interaction patterns
     * HoneyCreds: Credential usage, access attempts
     * Canary Tokens: Document access, credential use

2. **Central SIEM Processing**
   - **Wazuh Manager**
     * Event correlation
     * Threat intelligence matching
     * Initial alert triage
   - **Wazuh Indexer**
     * Event enrichment
     * Historical correlation
     * Threat hunting data
   - **Playbooks**
     * Honeypot Access Response
     * HoneyCred Abuse Response
     * Ransomware Response

3. **Analysis & Response**
   - **Splunk**
     * Advanced correlation
     * Threat hunting
     * Compliance reporting
     * Performance metrics
   - **TheHive**
     * Case management
     * Incident response
     * IOC management
     * Team coordination

4. **Notification Chain**
   - **Low Priority (L3-5)**
     * Channel: #security-info
     * Type: Dashboard updates
     * Frequency: Daily digest
   - **Medium Priority (L6-8)**
     * Channel: #security-alerts
     * Type: Real-time alerts
     * Frequency: As detected
   - **High Priority (L9-11)**
     * Channel: #security-critical
     * Type: Immediate alerts
     * Frequency: Real-time
   - **Critical (L12-15)**
     * Channel: #security-critical
     * Additional: Email alerts
     * Frequency: Immediate with acknowledgment

## Integration Points

### Wazuh → Splunk
- Real-time event forwarding via HEC
- Custom field mapping for correlation
- Alert enrichment with threat intel
- Automated response tracking

### Wazuh → TheHive
- Case creation for L9+ alerts
- Evidence attachment (logs, captures)
- Playbook triggering based on alert type
- Bi-directional status updates

### Splunk ↔ TheHive
- Incident context sharing
- Historical data correlation
- IOC extraction and sharing
- Response action tracking
- Performance metrics
