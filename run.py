import os
import sys


wb_path = r'"C:\Program Files\ANSYS Inc\v201\Framework\bin\Win64\RunWB2"'
script = 'script.wbjn'
cmdline = '{} -B -R {}'.format(wb_path, script)

try:
    os.system(cmdline)
except Exception:
    print('Failed to launch ANSYS Workbench!')
    sys.exit(0)




