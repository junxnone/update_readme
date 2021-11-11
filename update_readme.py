import os
import glob
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('--repo', default='none')
args = ap.parse_args()
print(args.repo)
repo_name = args.repo.split('/')[1]

notebook_list = sorted(glob.glob('*/*.ipynb'))

file_category = {}
for inb in notebook_list:
    file_category[inb] = inb.split('/')[0]

pre_category = 'init'
with open("README.md", 'w') as indexf:
    indexf.write("# Jupyter Notebook Index")
for ifile in file_category:
    category = file_category[ifile]

    if category != pre_category:
        with open("README.md", 'a') as indexf:
            indexf.write("\n\n## " + category + "\n- [" + ifile.split('/')[1] + "](https://junxnone.github.io/" + repo_name + "/nbv.html?notebook_name=" + ifile + ")")
    else:
        with open("README.md", 'a') as indexf:
            indexf.write("\n- [" + ifile.split('/')[1] + "](https://junxnone.github.io/" + repo_name + "/nbv.html?notebook_name=" + ifile + ")")

    pre_category = file_category[ifile]
