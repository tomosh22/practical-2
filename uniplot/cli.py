import argparse
from . import parse
from . import analysis
from . import plot

LOC = "uniprot_receptor.xml.gz"
smallLOC = "./resources/uniprot_sprot_small.xml.gz"


def cli():
    """command line interface"""
    parser = argparse.ArgumentParser(prog="uniplot")
    parser.add_argument("--directory")
    parser.add_argument("--depth")
    subparsers = parser.add_subparsers(help="""
    Command Line Arguments:
     NOTE: --directory and/or --depth must come before any other arguments
    
    --directory: specify a custom uniprot file
    
    --depth: specify how many taxa to go down
    
    dump: prints all information about every protein
    
    list: prints the names of every protein
    
    average: prints the average length of every protein
    
    small: prints the average length of every protein in the smaller uniprot file
    
    plot: plots a graph of frequency against taxa for every protein
    
    plotpie: plots a pie chart of frequency against taxa for every protein
    """)
    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)
    subparsers.add_parser("average").set_defaults(func=average)
    subparsers.add_parser("small").set_defaults(func=small)
    subparsers.add_parser("plot").set_defaults(func=plot_average_by_taxa)
    subparsers.add_parser("plotpie").set_defaults(func=plot_average_by_taxa_pie)
    args = parser.parse_args()
    if not args.depth:
        args.depth = 1
    if not args.__contains__("func"):
        args.func = dump
    global LOC
    if args.directory:
        LOC = args.directory
    if args.func == plot_average_by_taxa or args.func == plot_average_by_taxa_pie:
        args.func(int(args.depth) - 1)
    else:
        args.func()


def names():
    """prints the names of every protein"""
    for record in parse.uniprot_seqrecords(LOC):
        print(record["name"])


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


def plot_average_by_taxa(depth):
    """plots a graph of frequency against taxa for every protein"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC), depth)
    plot.plot_bar_show(av)


def plot_average_by_taxa_pie(depth):
    """plots a graph of frequency against taxa for every protein"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC), depth)
    plot.plot_pie_show(av)
