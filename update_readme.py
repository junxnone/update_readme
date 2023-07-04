import os
import glob
import argparse
import pytz
import datetime

ap = argparse.ArgumentParser()
ap.add_argument('--repo', default='none')
args = ap.parse_args()
print(args.repo)
user_name = args.repo.split('/')[0]
repo_name = args.repo.split('/')[1]

md_list = sorted(glob.glob('docs/*.md'))
with open("README.md", 'w') as indexf:
    indexf.write("# 3D Knowledge Graph\n\n")
    for ikg in md_list:
        ititle = ikg.split('_')[-1].split('.')[0]
        indexf.write("<!-- ko-fi :id=" + "junxnone.github.io/jstools/md3dkg/?md=https://" + user_name + ".github.io/" + repo_name + '/' + ikg +  " :color=#1599d6 -->\n" + ititle + "\n" + "<!-- ko-fi -->\n" )
    indexf.write("<!-- ko-fi :id=" + "github.com/junxnone/tmdkg/issues/new :color=#1599d6 -->\n" +  "Create New KG\n" + "<!-- ko-fi -->\n" )
    tz = pytz.timezone('Asia/Shanghai')

    uddate = datetime.datetime.now(tz).strftime("%m%d")
    udtime = datetime.datetime.now(tz).strftime("%H%M%S")
    tstr = '<kbd>' + '<sub>@' + udtime + uddate + '</sub></kbd>\n'
    indexf.write(tstr)
