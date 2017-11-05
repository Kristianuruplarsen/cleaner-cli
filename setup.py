from setuptools import setup
setup(name = "cleaner",
      version = "0.1dev",
      packages = ["cleaner_cli"],
      entry_points = {'console_scripts': [
      'clean=cleaner_cli.__main__:main'
      ]}
      )
