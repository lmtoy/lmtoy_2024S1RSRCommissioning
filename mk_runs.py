#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024S1RSRCommissioning"



#        obsnums per source (make it negative if not added to the final combination)
on = {}

#on['Blanksky'] = [ 110444]
#on['1051p213'] = [ 110877]

on['I08311']   = [ 111601, 111601]

on['I10565']   = [-110669, 110670,-110879,-110880, 110898, 110899,
                   112315, 112316, 112333, 112334, 112383, 112384,
                   112573, 112574,-112637,-112638, 112643, 112644,
                   113195, 113196, 113206, 113883, 113884,
                   114027, 114028, 114030, 114032,
                  ]

on['I12112']   = [ 110665, 110666, 110963, 110964, 111583, 111584,
                   111606, 111607,112651, 112652,
                   113185, 113186, 113188, 113209,
                   113577, 113578,
                  ]
 
on['I17208']   = [ 111032, 111033, 113645, 113646, 113650, 113651, 113790, 113791,
                   114035, 114036,
                   ]

    
#        common parameters per source on the first dryrun (run1a, run2a)
#        strong ones need cthr=0.015
pars1 = {}
#pars1['Blanksky']   = ""
#pars1['1051p213']   = "linecheck=1"
pars1['I08311']     = "linecheck=1"
pars1['I10565']     = "linecheck=1"
pars1['I12112']     = "linecheck=1"
pars1['I17208']     = "linecheck=1"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
#pars2['Blanksky']   = ""
#pars2['1051p213']   = ""
pars2['I08311']     = ""
pars2['I10565']     = ""
pars2['I12112']     = ""
pars2['I17208']     = ""


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
