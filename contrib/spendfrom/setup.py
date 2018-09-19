from distutils.core import setup
setup(name='DCUspendfrom',
      version='1.0',
      description='Command-line utility for dcu "coin control"',
      author='Gavin Andresen',
      author_email='gavin@dcufoundation.org',
      requires=['jsonrpc'],
      scripts=['spendfrom.py'],
      )
