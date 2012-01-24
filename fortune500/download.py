import itertools
import urllib2
import time

download_to = "dl"

versions = [
    #    { 'base': "http://money.cnn.com/magazines/fortune/fortune500_archive/full",
    #      'pages': ["1.html", "101.html", "201.html", "301.html", "401.html"],
    #      'years': range(1955, 1956),#2006),
    # 'pattern': "%s/%d/%s"},
    { 'base': "http://money.cnn.com/magazines/fortune/fortune500",
      'pages': ["index.html", "101_200.html", "201_300.html", "301_400.html", "401_500.html", "501_600.html", "601_700.html", "701_800.html", "901_1000.html"],
      'years': range(2006, 2008),
      'pattern': "%s/%d/full_list/%s"},
]

for ver in versions:
    pattern = ver['pattern']
    base = ver['base']
    for year, page in itertools.product(ver['years'], ver['pages']):
        target = pattern % (base, year, page)
        output_fname = "%s/%d_%s" % (download_to, year, page)
        print target, "->", output_fname
        
        output_file = open(output_fname, "w")
        output = urllib2.urlopen(target).read()
        output_file.write(output)
        output_file.close()

        time.sleep(1)

"""

html5lib.parse(f, treebuilder="lxml")


soup = BeautifulSoup(urllib2.urlopen('http://www.timeanddate.com/worldclock/astronomy.html?n=78').read())

for row in soup('table', {'class' : 'spad'})[0].tbody('tr'):
  tds = row('td')
  print tds[0].string, tds[1].string
"""
