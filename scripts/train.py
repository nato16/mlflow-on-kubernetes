import os
import click

@click.command()
@click.argument("infile")
def main(infile):
    lines=None
    with open(infile,"r") as fin:
        lines=fin.readlines()
    print (lines)
