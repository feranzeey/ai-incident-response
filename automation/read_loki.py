import requests
import time

# Loki API endpoint
url = "http://localhost:3100/loki/api/v1/query_range"

# Current time (nanoseconds)
end = int(time.time() * 1e9)

# One hour ago
start = end - (60 * 60 * 1000000000)

# Query logs with the label job="flask"
params = {
    "query": '{job="flask"}',
    "start": start,
    "end": end,
    "limit": 20
}

# Send request to Loki
response = requests.get(url, params=params)

# Check the response
if response.status_code == 200:
    data = response.json()

    results = data["data"]["result"]

    if not results:
        print("No logs found.")
    else:
        print("Logs:\n")

        for stream in results:
            for log in stream["values"]:
                print(log[1])

else:
    print("Error:", response.status_code)
    print(response.text)