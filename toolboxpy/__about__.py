# -*- coding:utf-8 -*-
from __future__ import absolute_import, division, print_function

import os
import subprocess

__all__ = [
    "__title__", "__summary__", "__version__", "__author__",
    "__email__", "__copyright__",
]

MAJOR = 1
MINOR = 0
MICRO = 0
IS_RELEASE = True
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)


# Return the git revision as a string
def git_version():
    def _minimal_ext_cmd(cmd):
        # construct minimal environment
        env = {}
        for k in ['SYSTEMROOT', 'PATH']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(cmd, stdout=subprocess.PIPE, env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(['git', 'rev-parse', 'HEAD'])
        GIT_REVISION = out.strip().decode('ascii')
    except OSError:
        GIT_REVISION = "Unknown"

    return GIT_REVISION


def get_version_info():
    # Adding the git rev number needs to be done inside
    # write_version_py(), otherwise the import of toolbox.version messes
    FULLVERSION = VERSION
    if os.path.exists('.git'):
        GIT_REVISION = git_version()
    else:
        GIT_REVISION = "Unknown"

    if not IS_RELEASE:
        FULLVERSION += '.dev0+' + GIT_REVISION[:7]

    return FULLVERSION, GIT_REVISION


__version__ = get_version_info()[0]

__author__ = 'ancy'
__date__ = '2023.03.01'
__copyright__ = "Copyright 2023"
__title__ = "ToolBoxPy"
__summary__ = "ToolBoxPy is a package which provides programming toolkit to developers."
__email__ = "397031272@qq.com"


