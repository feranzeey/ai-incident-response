def fix(problem):

    if problem == "High CPU Usage":
        print("Restarting service...")

    elif problem == "Memory Leak":
        print("Scaling containers...")

    elif problem == "Deployment Failure":
        print("Rolling back deployment...")

    elif problem == "Cache Issue":
        print("Clearing cache...")

    else:
        print("No automatic fix available.")