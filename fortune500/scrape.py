import csv
import glob
import html5lib

from csv import DictWriter
from lxml import etree
from lxml.cssselect import CSSSelector

versions = [
    {
        'years': range(1955, 2006),
        'row_selector': '.maglisttable .rowcolor1, .maglisttable .rowcolor2',
    },
    #    {
    #        'years': range(2006, 2012),
    #        'row_selector': 'tr.tablerow',
    #    },
]

def add_rows(tree, version, year, writer):
    sel = CSSSelector(version['row_selector'])
    for row in sel(tree):
        writer.writerow({
            'rank': row[0].text,
            'company': row[1][0].text,
            'revenue': row[2].text,
            'profit': row[3].text,
            'year': year
        })

writer = DictWriter(open("fortune500.csv", "w"), ["year", "rank", "company", "revenue", "profit"])

for ver in versions:
    for year in ver['years']:
        for fname in glob.glob("./dl/%d*" % year):
            tree_file = open(fname)
            tree = html5lib.parse(tree_file, treebuilder="lxml")
            add_rows(tree, ver, year, writer)
            tree_file.close()
            
