import sys
import os
import shutil
from distutils.core import setup, Extension

from txtorcon import __version__, __author__, __contact__, __copyright__, __license__, __url__

setup(name = 'txtorcon',
      version = __version__,
      description = 'Twisted-based Tor controller client, with state-tracking and configuration abstractions.',
      long_description = open('README','r').read(),
      keywords = ['python', 'twisted', 'tor', 'tor controller'],
      requires = ['twisted (>10.1.0)',
                  'GeoIP',
                  'ipaddr'],
      classifiers = ['Framework :: Twisted',
                     'License :: OSI Approved :: MIT License',
                     'Natural Language :: English',
                     'Operating System :: POSIX :: Linux',
                     'Operating System :: Unix',
                     'Programming Language :: Python',
                     'Topic :: Internet :: Proxy Servers',
                     'Topic :: Internet',
                     'Topic :: Security'],                     
      author = __author__,
      author_email = __contact__,
      url = __url__,
      license = __license__,
      packages  = ["txtorcon", "txtorcon.test"],
#      scripts = ['examples/attach_streams_by_country.py'],

      ## I'm a little unclear if I'm doing this "properly", especially
      ## the documentation etc. Do we really want "share/txtorcon" for
      ## the first member of the tuple?

      data_files = [('share/txtorcon', ['INSTALL', 'README', 'TODO', 'meejah.asc']),
                    
                    ## this includes pre-built single-page HTML docs
                    ## into the distribution. the map construct grabs
                    ## everything in doc_html/_static
                    ('share/txtorcon', ['doc_html/index.html', 'doc_html/objects.inv'] + map(lambda x: os.path.join('doc_html/_static', x), os.listdir('doc_html/_static'))),

                    ## this includes the Sphinx source for the
                    ## docs. The "map+filter" construct grabs all .rst
                    ## files and re-maps the path
                    ('share/txtorcon', ['docs/apilinks_sphinxext.py', 'docs/conf.py', 'docs/Makefile', 'docs/avatar.png'] + map(lambda x: os.path.join('docs', x), filter(lambda x: x[-3:] == 'rst', os.listdir('docs'))) + map(lambda x: os.path.join('docs/_static', x), os.listdir('docs/_static'))),

                    ## include all the examples
                    ('share/txtorcon/examples', map(lambda x: os.path.join('examples', x), filter(lambda x: x[-3:] == '.py', os.listdir('examples'))))
                    ]
      )
