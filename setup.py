
#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='OpenFisca-nsw',
    version='12.0.0',
    author='Foster Digital',
    author_email='tj@foster.digital',
    description=u'OpenFisca tax and benefit system for NSW',
    keywords='benefit microsimulation social tax',
    license='http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    url='https://github.com/tjharrop/openfisca-nsw',
    include_package_data=True,  # Will read MANIFEST.in
    install_requires=[
        'git+https://github.com/tjharrop/openfisca-core.git#egg=openfisca-core',
        ],
    extras_require={
        'test': [
            'flake8 >=3.4.0,<3.7.0',
            'flake8-print',
            'nose',
            'yamllint'
            ]
        },
    packages=find_packages(),
    test_suite='nose.collector',
    )
