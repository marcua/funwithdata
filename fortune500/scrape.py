import csv
import glob
import html5lib


versions = [
    {
        'years': range(1955, 2006),
        'row_selector': 'tr#tablerow',
    },
    {
        'years': range(2006, 2012),
        'row_selector': 'tr#tablerow',
    },
]

def parse_file(tree, version):
    print "yay!"

for ver in versions:
    for year in ver['years']:
        for fname in glob.glob("./dl/%d*" % year):
            tree_file = open(fname)
            tree = html5lib.parse(tree_file, treebuilder="lxml")
            parse_file(tree, ver)
            
