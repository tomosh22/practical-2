def average_len(records):
    totalLength = 0
    for record in records:
        totalLength += len(record)
    return totalLength / len(records)