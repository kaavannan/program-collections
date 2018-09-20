#!/usr/bin/env python3

__author__ = ['[Brandon Amos](http://bamos.github.io)']
__date__ = '2014.11.02'

"""
Produces a Markdown table concisely summarizing a list of GitHub repositories.
"""

from github import Github
import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument('repos', nargs="+", type=str)
args = parser.parse_args()
github = Github(os.getenv("GITHUB_TOKEN"))


def sanitize_for_md(s):
    s = s.replace("*", "\*")
    return s

# print("Generated on {}.\n".format(time.strftime("%Y-%m-%d")))
print("Name | Stargazers | Description")
print("|".join(["----"] * 3))
for r_name in sorted(args.repos, key=lambda v: v.upper()):
    try:
        r = github.get_repo(r_name)
    except:
        sys.stderr.write("Error: Repository '{}' not found.\n".format(r_name))
        sys.exit(-1)
    content = " | ".join([
        "[{}]({})".format(r.full_name, r.html_url),
        str(r.stargazers_count),
        sanitize_for_md(r.description)
    ])
    print(content)
