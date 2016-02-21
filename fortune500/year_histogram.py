import json
import sys
import matplotlib.pyplot as plt

from pandas.io.parsers import read_csv

df = read_csv(open(sys.argv[1]))
counts = df.groupby('company')['rank'].agg({'num_times':len}).reset_index()
histogram = counts.groupby('num_times')['company'].agg({'total': len, 'companies': lambda x: list(x)})

recs = histogram.to_records()
recs = {
    'data': [dict(zip(('x', 'y'), (int(r[0]), int(r[2])))) for r in recs],
    'companies': dict((int(r[0]), r[1]) for r in recs),
}
output = json.dumps(recs)

outf = open(sys.argv[2], "w")
outf.write(output)
outf.close()


