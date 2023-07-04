import os
import glob
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('--repo', default='none')
args = ap.parse_args()
print(args.repo)
user_name = args.repo.split('/')[0]
repo_name = args.repo.split('/')[1]

md_list = sorted(glob.glob('docs/*.md'))
print(md_list)
with open("README.md", 'w') as indexf:
    indexf.write("# 3D Knowledge Graph\n\n")
    for ikg in md_list:
        ititle = ikg.split('_')[-1].split('.')[0]
        print(ititle)
        indexf.write("<!-- ko-fi :id=" + "junxnone.github.io/jstools/md3dkg/?md=https://" + user_name + ".github.io/" + repo_name + '/' + ikg +  " :color=#1599d6 -->\n" + ititle + "\n" + "<!-- ko-fi -->\n" )
