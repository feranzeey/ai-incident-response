import requests

url = "http://localhost:9090/api/v1/query"

query = {
    "query": "100 - (avg by(instance)(rate(node_cpu_seconds_total{mode='idle'}[5m])) * 100)"
}

response = requests.get(url, params=query)

print(response.json())