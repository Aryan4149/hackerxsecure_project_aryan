# api/core/prevention_rules.py

PREVENTION_RULES = {
    "Benign": {
        "force_block": False,
        "custom_message": "Normal traffic detected. No action required."
    },

    # DOS / DDOS
    "DoS Hulk": {
        "force_block": True,
        "custom_message": "DoS Hulk detected. Source IP blocked due to traffic flooding."
    },
    "DDoS": {
        "force_block": True,
        "custom_message": "Distributed DoS detected. Immediate blocking applied."
    },
    "DoS GoldenEye": {
        "force_block": True,
        "custom_message": "GoldenEye HTTP flood detected. Requests blocked."
    },
    "DoS slowloris": {
        "force_block": True,
        "custom_message": "Slowloris attack detected. Connections terminated."
    },
    "DoS Slowhttptest": {
        "force_block": True,
        "custom_message": "Slow HTTP test attack detected. Protection enabled."
    },

    # BRUTE FORCE
    "FTP-Patator": {
        "force_block": True,
        "custom_message": "FTP brute-force detected. Authentication blocked."
    },
    "SSH-Patator": {
        "force_block": True,
        "custom_message": "SSH brute-force detected. SSH access blocked."
    },

    # WEB ATTACKS (ALL VARIANTS)
    "Web Attack Sql Injection": {
        "force_block": True,
        "custom_message": "SQL Injection detected. Malicious queries blocked."
    },
    "Web Attack Brute Force": {
        "force_block": True,
        "custom_message": "Web brute-force attack detected. Access blocked."
    },
    "Web Attack XSS": {
        "force_block": True,
        "custom_message": "XSS attack detected. Script payload blocked."
    },

    # OTHER
    "PortScan": {
        "force_block": False,
        "custom_message": "Port scanning detected. IP flagged and monitored."
    },
    "Bot": {
        "force_block": True,
        "custom_message": "Botnet traffic detected. Automated traffic blocked."
    },
    "Infiltration": {
        "force_block": True,
        "custom_message": "Infiltration detected. Lateral movement blocked."
    },
    "Heartbleed": {
        "force_block": True,
        "custom_message": "Heartbleed exploit detected. Emergency block applied."
    }
}


def normalize_label(label: str) -> str:
    if not label:
        return "Benign"

    label = label.strip()
    label = label.replace("–", "-")
    label = label.replace("—", "-")
    label = label.replace("�", "")
    label = label.replace("?", "")
    label = label.replace("-", " ")

    label = " ".join(label.split())
    return label


def get_prevention_rule(label: str) -> dict:
    clean = normalize_label(label)

    if clean in PREVENTION_RULES:
        return PREVENTION_RULES[clean]

    return {
        "force_block": False,
        "custom_message": "Unknown activity detected. Monitoring traffic."
    }
