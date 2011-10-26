# -*- coding: iso-8859-1 -*-
# IMPORTANT! This encoding (charset) setting MUST be correct! If you live in a
# western country and you don't know that you use utf-8, you probably want to
# use iso-8859-1 (or some other iso charset). If you use utf-8 (a Unicode
# encoding) you MUST use: coding: utf-8
# That setting must match the encoding your editor uses when you modify the
# settings below. If it does not, special non-ASCII chars will be wrong.

"""
    MoinMoin - Configuration for a single wiki

    If you run a single wiki only, you can omit the farmconfig.py config
    file and just use wikiconfig.py - it will be used for every request
    we get in that case.

    Note that there are more config options than you'll find in
    the version of this file that is installed by default; see
    the module MoinMoin.config.multiconfig for a full list of names and their
    default values.

    Also, the URL http://moinmo.in/HelpOnConfiguration has
    a list of config options.

    ** Please do not use this file for a wiki farm. Use the sample file
    from the wikifarm directory instead! **
"""

import os
import glob

from MoinMoin.config import multiconfig, url_prefix_static
import MoinMoin
from MoinMoin.config.multiconfig import DefaultConfig
from MoinMoin.auth import BaseAuth
from MoinMoin.security import Permissions
from MoinMoin.user import User

class PlonePermissions(Permissions):
    """special permission. allow all"""

    def __getattr__(self, attr):
        return lambda pagename: True

class PloneAuth(BaseAuth):
    login_inputs = ['username']
    logout_possible = False
    name = 'repoze.who'

    def request(self, request, user_obj, **kw):
        user = request.env.get('repoze.who.identity', {}).get('user', None)
        if user:
            user = User(
                    request, auth_username=user.uid,
                    auth_method=self.name,
                    auth_attribs=('name', 'aliasname', 'email', 'password'))
            #user.may = PlonePermissions(user)
            user.language = 'es'
            user.valid = 1
            return user, True
        return user_obj, True


class Config(multiconfig.DefaultConfig):

    wikiconfig_dir = os.path.abspath(os.path.dirname(__file__))
    instance_dir = '/Users/erik/Develop/pythonmx_site/var/wiki'
    data_dir = os.path.join(instance_dir, 'data', '') # path with trailing /
    data_underlay_dir = os.path.join(instance_dir, 'underlay', '') # path with trailing /
    url_prefix_static = '/wiki' + url_prefix_static

    sitename = u'PythonMexico'
    logo_string = u'<img src="%s/common/moinmoin.png" alt="MoinMoin Logo">' % url_prefix_static
    page_front_page = u'FrontPage'
    
    navi_bar = [
        #u'%(page_front_page)s',
        u'RecentChanges',
        u'FindPage',
        u'HelpContents',
    ]

    theme_default = 'modern'
    language_default = 'es'

    page_category_regex = ur'(?P<all>Category(?P<key>(?!Template)\S+))'
    page_dict_regex = ur'(?P<all>(?P<key>\S+)Dict)'
    page_group_regex = ur'(?P<all>(?P<key>\S+)Group)'
    page_template_regex = ur'(?P<all>(?P<key>\S+)Template)'

    show_hosts = 1
    
    superuser = ['admin',]

    # Enable graphical charts, requires gdchart.
    #chart_options = {'width': 600, 'height': 300}

    auth = [PloneAuth()]
    cookie_lifetime = 1 # 1 hour after last access ldap login is required again
    user_autocreate = True

    # we don't allow the user to change those values on UserPreferences page
    user_form_disable = ['name', 'aliasname', 'email', ]
    # we remove those fields as they are not used for ldap based logins
    user_form_remove = ['password', 'password2', ]

    acl_rights_default = u'Known:read,write,admin,delete,revert All:read'

    # liste du cd
    acl_rights_before  = ','.join(superuser)+':read,write,admin,delete,revert'
    
