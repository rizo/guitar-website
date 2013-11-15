#!/usr/bin/env python2.7

import os
import sys
import json
from string import Template


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
VIEWS_DIR = os.path.join(PROJECT_ROOT, "views")


def view(name):
    directory = os.path.join(VIEWS_DIR, name + ".view")
    template = Template(file(os.path.join(directory, name + ".html")).read())
    content = json.load(file(os.path.join(directory, name + ".json")))
    return template.substitute(content)


def render(view):
    sys.stdout.write(view)


def main():
    print "Content-type: text/html\n\n"
    render(view("main"))


if (__name__ == "__main__"):
    main()

