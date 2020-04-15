# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup


version = '0.1.0.dev0'


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="bobtemplates.redturtle.plone",
    version=version,
    description="Templates for Plone projects.",
    long_description=long_description,
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="web plone zope skeleton project",
    author="RedTurtle Technology",
    author_email="sviluppoplone@redturtle.it",
    url="https://github.com/RedTurtle/bobtemplates.redturtle.plone",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/bobtemplates.redturtle.plone",
        "Source": "https://github.com/RedTurtle/bobtemplates.redturtle.plone",
        "Tracker": "https://github.com/RedTurtle/bobtemplates.redturtle.plone/issues",
    },
    license="GPL version 2",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["bobtemplates", "bobtemplates.redturtle"],
    include_package_data=True,
    zip_safe=False,
    install_requires=["setuptools", "bobtemplates.plone"],
    setup_requires=[],
    tests_require=[],
    extras_require={},
    entry_points={
        "mrbob_templates": [
            "buildout_redturtle = bobtemplates.redturtle.plone.bobregistry:buildout_redturtle",
        ]
    },
)
