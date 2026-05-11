def unique_ips(logs):
    unique = []
    for element in logs:
        ip = element['ip']
        if ip not in unique:
            unique.append(ip)
    return unique
