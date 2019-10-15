import gzip
from Bio import SeqIO

def uniprot_seqrecords(file_location):
    """obtains all the records from the gzip xml file"""
    records = []

    handle = gzip.open(file_location)
    for record in SeqIO.parse(handle, "uniprot-xml"):
        records.append({"length":len(record),"taxonomy":record.annotations["taxonomy"]})
    handle.close()
    return records
