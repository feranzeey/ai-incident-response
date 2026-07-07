import subprocess

print("Restarting Flask container...")

subprocess.run(["docker", "restart", "flask-app"])

print("Done!")