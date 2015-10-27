#!/usr/bin/env python

## CREATED BY CHRISTOPHER LAVENDER
## INTEGRATIVE BIOINFORMATICS, NIEHS
## VERSION DATE 2015-10-27

import sys
from optparse import OptionParser

if len(sys.argv) == 1:
    sys.stdout.write("Usage: python gtf_to_searchWindows.py <GTF file>\n")
    exit()

parser = OptionParser()

(options, args) = parser.parse_args()