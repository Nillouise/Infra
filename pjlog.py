#!/usr/bin/env python3

import os
import sys
import fcntl
import json

for cc in sys.stdin:
    if(cc.startswith("{")):
        c = json.loads(cc)
        sys.stdout.write("{0} {1} {2}\n".format(c.get('@timestamp', 'MISS'),c.get('level', 'MISS'), c.get('message', 'MISS')))
    else:
        sys.stdout.write(cc+'\n')
