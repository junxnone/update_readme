import os
import glob
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('--repo', default='none')
args = ap.parse_args()
print(args.repo)
user_name = args.repo.split('/')[0]
repo_name = args.repo.split('/')[1]

notebook_list = sorted(glob.glob('*/*.ipynb'))

file_category = {}
categorys = []
for inb in notebook_list:
    file_category[inb] = inb.split('/')[0]

for ifile in file_category:
    categorys.append(file_category[ifile])

pre_category = 'init'
with open("README.md", 'w') as indexf:
    indexf.write("# Jupyter Notebooks\n\n")

for ifile in file_category:
    category = file_category[ifile]

    if category != pre_category:
        with open("README.md", 'a') as indexf:
            indexf.write("\n\n## " + category + "\n- [" + ifile.split('/')[1] + "](https://" + user_name + ".github.io/" + repo_name + "/nbv.html?notebook_name=" + ifile + ")")
    else:
        with open("README.md", 'a') as indexf:
            indexf.write("\n- [" + ifile.split('/')[1] + "](https://" + user_name + ".github.io/" + repo_name + "/nbv.html?notebook_name=" + ifile + ")")

    pre_category = file_category[ifile]
