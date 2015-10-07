#!/usr/bin/python2
__author__ = 'xtotdam'

import sys

syntax, text = sys.argv[1:3]
   
#ln = 'True' if text.count('\n') > 1 else 'False'
ln = 'True'

code_block = '''\
{{{{{{ code: lang="{syntax}" linenumbers="{ln}"
{code}
}}}}}}'''.format(
    syntax=syntax,
    ln=ln,
    code=text.strip()
    )

print code_block
