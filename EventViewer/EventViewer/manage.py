# -*- coding: utf8 -*-
#!/usr/bin/env python
'''
Created on Feb 22, 2013

@author: alekseynikiforov
'''

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EventViewer.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
