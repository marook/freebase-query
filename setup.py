#!/usr/bin/env python

import distutils.core
import os.path

projectdir = os.path.dirname(os.path.abspath(__file__))
srcdir = os.path.join(projectdir, 'src')
bindir = os.path.join(srcdir, 'bin')

distutils.core.setup(
    name = 'freebase-query',
    author = 'Markus Pielmeier',
    author_email = 'markus.pielmeier@gmail.com',
    license = 'GPLv3',

    requires = [ 'freebase' ],

    data_files = [
        (os.path.join('share', 'doc', 'freebase-query'), ['README'])
    ],

    scripts = [
        os.path.join(bindir, 'freebase-query'),
        ],
)
