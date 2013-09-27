#!/usr/bin/env python

from os import walk
from os.path import join
from sys import exit, argv
from re import search
from json import dump


def get_logfiles_path(root_path):
    """
    Walks through the root_path tree and stores the path of every file
    in a list. Returns that list.

    """

    logpaths = []
    for root, dirs, files in walk(root_path):
        for file_name in files:
            if file_name.endswith('.log'):
                logpaths.append(join(root, file_name))

    return logpaths



def search_for_links(fileslist):
    """
    Reads every file in fileslist, which should be a list with the
    paths of every file to be sweeped. Performs a regex search
    for a web url pattern, and filters the most obvious
    disposable ones. 

    Returns a list containing all the links.

    """

    stored_links = []
    for file_path in fileslist:
        with open(file_path) as file2read:
            for line in file2read:
                if 'Topic' not in line:
                    link = search("(http|ftp|https)?:\/\/([\w\-_]+(?:(?:\."
                                  "[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*"
                                  "[\w\-\@?^=%&amp;/~\+#])?", line)
                    if (link and
                        ('paste' not in link.group() and
                         'stackoverflow' not in link.group() and
                         'pymbook' not in link.group() and
                         'github' not in link.group() and
                         'google' not in link.group() and
                         'facebook' not in link.group() and
                         'twitter' not in link.group() and
                         'pypi' not in link.group() and
                         'rafb' not in link.group() and
                         'finance' not in link.group() and
                         '127.0.0.1' not in link.group() and
                         'dgplug' not in link.group() and
                         'kushal' not in link.group() and
                         'arnauorriols' not in link.group() and
                         'sayanchowdhury' not in link.group())):
                       stored_links.append(link.group())

    return stored_links



if __name__ == "__main__":
    usage = "\nUsage: $ python link_searcher.py <root_dir> <json_file>\n"
    if len(argv) == 3:
        with open(argv[2], 'w') as json_file:
            dump(search_for_links(get_logfiles_path(argv[1])), json_file)
    else:
        print usage
