# -*- coding:utf-8 -*-
from __future__ import absolute_import, division, print_function

import sys
import textwrap

if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Python version >= 3.6 required.")


PACKAGE_NAME = 'ToolBoxPy'
ABOUT_FILE = '{}/__about__.py'.format(PACKAGE_NAME)

about = {}
with open(ABOUT_FILE) as f:
    exec(f.read(), about)


if sys.version_info[0] == 2:
    with open('README.md') as f:
        LONG_DESCRIPTION = f.read()
else:
    with open('README.md', encoding='utf-8') as f:
        LONG_DESCRIPTION = f.read()


def parse_setuppy_commands():
    """
    Check the commands and respond appropriately.
    """
    args = sys.argv[1:]

    if not args:
        # User forgot to give an argument probably, let setuptools handle that.
        return True

    # The following commands are supported, but we need to show more
    # useful messages to the user
    if 'install' in args:
        print(textwrap.dedent("""
            Note: if you need reliable uninstall behavior, then install
            with pip instead of using `setup.py install`:
              - `pip install .`       (from a git repo or downloaded source release)
              - `pip install ToolBox`   (last release on PyPI)
            """))
        return True


def setup_package():
    parse_setuppy_commands()

    install_requirements = [
        "colorlog",
    ]

    # try:
    #     import cv2
    # except ImportError:
    #     install_requirements += ["opencv-python"]

    dev_requirements = [
        "pylint",
        "pytest",
        "tox",
    ]

    # This import is here because it needs to be done before importing setup()
    # from numpy.distutils, but after the MANIFEST removing and sdist import
    # higher up in this file.
    from setuptools import setup
    from setuptools import find_packages

    metadata = dict(
        name=PACKAGE_NAME,
        version=about['__version__'],
        description=about['__summary__'],

        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",

        author=about['__author__'],
        author_email=about['__email__'],
        classifiers=[
            "Natural Language :: English",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: Implementation :: CPython",
        ],

        packages=find_packages(exclude=['tests', 'test_*', "tests.*"]),
        include_package_data=True,

        # 这里只能限制 pip install 命令，使用 setup.py install不会检查
        python_requires='!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*',

        install_requires=install_requirements,
        extras_require={
            "dev": dev_requirements,
        },
    )

    setup(**metadata)


if __name__ == '__main__':
    setup_package()
