from distutils.core import setup

setup(
    name = 'autobears',
    version = '0.1.0',
    author = 'Caleb Wang',
    author_email = 'cw@berkeley.edu',
    packages = ['calnet', 'telebears', 'autobears']
    license = 'LICENSE.txt',
    install_requires = ['mechanize']
}
