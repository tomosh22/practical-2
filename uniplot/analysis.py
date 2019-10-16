def average_len(records):
    """Returns the average len for records."""
    totalLength = 0
    for record in records:
        totalLength += record["length"]
    return round(totalLength / len(records))


def average_len_taxa(records,depth):
    """Returns the average length for each taxa, down to passed depth"""
    record_by_taxa = {}
    for r in records:
        for x in range(depth):
            taxa = r["taxonomy"][x]
            record_by_taxa.setdefault(taxa, []).append(r)
        #taxa = r.annotations["taxonomy"][0]
        #record_by_taxa.setdefault(taxa, []).append(r)

    return {taxa: average_len(record) for (taxa, record) in record_by_taxa.items()}
