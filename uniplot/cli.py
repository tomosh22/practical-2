import gzip
import argparse
from Bio import SeqIO
handle = gzip.open("uniprot_receptor.xml.gz")
def cli():
    parser = argparse.ArgumentParser(prog="uniplot")
    subparsers = parser.add_subparsers(help="Sub Command Help")
    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)
    args = parser.parse_args()
    args.func()
def names():
    for record in SeqIO.parse(handle, "uniprot-xml"):
        print(record.name)
def dump():
    for record in SeqIO.parse(handle, "uniprot-xml"):
        print(record)