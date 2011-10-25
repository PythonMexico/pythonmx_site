# -*- coding: utf-8 -*-
"""
    MoinMoin - mod_wsgi driver script
"""

import sys, os
from MoinMoin.web.serving import make_application

application = make_application(shared=True)

