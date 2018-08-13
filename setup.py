from setuptools import setup

setup(
name='snapshotalyzer-fotis',
version = '0.1',
author="Fotis Skarmoutsos",
author_email="fskarm@yahoo.com",
description="A tool to manage AWS EC2 snapshots",
license="GPLv3+",
packages =['fotis'],
url="https://github.com/fskarmoutsos/snapshotalyzer",
Install_requires =[
    'click',
    'boto3'
],
entry_points='''
    [console_scripts]
    fotis = fotis:cli
    '''
)
