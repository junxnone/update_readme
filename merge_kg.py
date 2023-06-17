import os
import glob
import argparse
import json

ap = argparse.ArgumentParser()
ap.add_argument('--kgf', type=str, nargs='+', default='none', help='python merge_kg.py kg1.json kg2.json kg3.json')
args = ap.parse_args()
print(args.kgf)

skg = {'nodes':[],'links':[]}
for ijsonf in args.kgf:
    with open(ijsonf,'r') as f:
        a = json.load(f)
        for inode in a['nodes']:
            skg['nodes'].append(inode)
        for ilink in a['links']:
            skg['links'].append(ilink)
            
print(skg)
with open("skg.json", 'w') as f:
    json.dump(skg, f)
