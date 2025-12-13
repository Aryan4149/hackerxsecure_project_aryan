# api/core/prevention_engine.py

def prevention_decision(label: str, severity: float) -> dict:
    """
    Always returns a valid prevention message.
    No external JSON. No missing keys. No undefined UI.
    """

    label_clean = label.strip() if label else "Unknown Attack"

    if severity >= 0.9:
        action = "BLOCK"
        message = (
            f"{label_clean} detected.\n\n"
            "Automatic Actions:\n"
            "- Source IP blocked\n"
            "- Traffic rate limited\n"
            "- Incident logged\n\n"
            "Recommended Steps:\n"
            "- Inspect firewall and server logs\n"
            "- Enable IDS/IPS rules\n"
            "- Apply strict rate limiting"
        )

    elif severity >= 0.6:
        action = "WARN"
        message = (
            f"Suspicious activity detected: {label_clean}.\n\n"
            "System Actions:\n"
            "- Traffic monitored\n"
            "- Alert raised\n\n"
            "Recommended Steps:\n"
            "- Monitor traffic patterns\n"
            "- Enable additional logging\n"
            "- Prepare mitigation rules"
        )

    else:
        action = "MONITOR"
        message = (
            f"Low-risk activity observed: {label_clean}.\n\n"
            "System Status:\n"
            "- No immediate threat\n\n"
            "Recommended Steps:\n"
            "- Continue monitoring\n"
            "- Review periodically"
        )

    return {
        "attack_type": label_clean,
        "severity": round(severity, 2),
        "action": action,
        "message": message
    }
