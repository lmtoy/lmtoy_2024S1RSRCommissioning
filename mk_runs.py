#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024S1RSRCommissioning"


#        obsnums per source (make it negative if not added to the final combination)
on = {}

on['I10565']  = [ 110669, 110670 ]

    
on['I12112']  = [ 110665, 110666 ]

    
#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['I10565']     = "linecheck=1"
pars1['I12112']     = "linecheck=1"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['I10565']     = "srdp=1"
pars2['I12112']     = "srdp=1"


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
