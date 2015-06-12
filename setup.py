from setuptools import setup


setup(name='disrupt',
      version='1.0.0',
      description='A python "tool" for "interacting" with the terminals of "friends" and "colleagues".',
      url='http://github.com/dellis23/disrupt',
      author='Daniel Ellis',
      author_email='ellisd23@gmail.com',
      license='GPLv3',
      install_requires=[],
      packages=['disrupt'],
      scripts=[
          'bin/disrupt',
      ])
