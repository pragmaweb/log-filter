from filter_logs import filter_logs
from unique_ips import unique_ips

raw_logs = [
    "192.168.0.1;200",
    "10.0.0.2;404",
    "192.168.0.1;200",
    "10.0.0.3;500",
    "10.0.0.2;404",
    "172.16.0.1;200",
    "10.0.0.3;403"
]


filtered = filter_logs(raw_logs, min_status=400)
result = unique_ips(filtered)
print(result)
