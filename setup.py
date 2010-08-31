from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='dolmen.xmlobject',
      version=version,
      description="Dolmen XML object loader/dumper",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='GPL',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['dolmen'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'dolmen.content',
          'z3c.schema2xml',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
