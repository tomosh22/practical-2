import argparse
from . import parse
from . import analysis
from . import plot
LOC="uniprot_receptor.xml.gz"
smallLOC = "./resources/uniprot_sprot_small.xml.gz"
def cli():
    """command line interface"""
    parser = argparse.ArgumentParser(prog="uniplot")
    subparsers = parser.add_subparsers(help="""
    Command Line Arguments:
    
    dump: prints all information about every protein
    
    list: prints the names of every protein
    
    average: prints the average length of every protein
    
    small: prints the average length of every protein in the smaller uniprot file
    
    plot: plots a graph of frequency against taxa for every protein
    """)
    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)
    subparsers.add_parser("average").set_defaults(func=average)
    subparsers.add_parser("small").set_defaults(func=small)
    subparsers.add_parser("plot").set_defaults(func=plot_average_by_taxa)
    subparsers.add_parser("dir").add_argument()

    args = parser.parse_args()
    args.func()
def names():
    """prints the names of every protein"""
    for record in parse.uniprot_seqrecords(LOC):
        print(record.name)
def dump():
    """prints all information about every protein"""
    for record in parse.uniprot_seqrecords(LOC):
        print(record)
def average():
    """prints the average length of every protein"""
    print("Average length is: " + str(round(analysis.average_len(parse.uniprot_seqrecords(LOC)))))
def small():
    """prints the average length of every protein in the smaller uniprot file"""
    print("Average small length is: " + str(round(analysis.average_len(parse.uniprot_seqrecords(smallLOC)))))
def plot_average_by_taxa():
    """plots a graph of frequency against taxa for every protein"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC))
    plot.plot_bar_show(av)
