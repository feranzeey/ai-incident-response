def investigate(cpu, memory):

    if cpu > 90:
        return {
            "root_cause": "High CPU Usage",
            "confidence": "95%",
            "fix": "Restart Service"
        }

    elif memory > 90:
        return {
            "root_cause": "Memory Leak",
            "confidence": "92%",
            "fix": "Scale Containers"
        }

    return {
        "root_cause": "Unknown",
        "confidence": "50%",
        "fix": "Manual Investigation"
    }