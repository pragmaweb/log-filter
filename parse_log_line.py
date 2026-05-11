def parse_log_line(line: str) -> dict:
    if ";" in line:
        parts = line.split(";")
        ip = parts[0]
        status = int(parts[1])
        return {"ip": ip, "status": status}
    else:
        return None
