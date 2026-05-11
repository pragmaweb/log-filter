from parse_log_line import parse_log_line

def filter_logs(lines, min_status=400):
    for line in lines:
        dic = parse_log_line(line)
        if dic is None:
            continue
        if dic['status'] >= min_status:
            yield dic
