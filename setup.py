from setuptools import setup
from setuptools import find_packages

#creation du fichier de configuaration du projet 
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name='projettestunitaire',
  version='1.1.0',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Sara Tazibt',
  author_email='sarahtazibt17@gmail.com',
  url='https://github.com/Sarahtazibt/M1-2022-rattrapage/',
  packages=find_packages(),
  entry_points={
    'console_script':[
      'hello-world-cli = M1_2022_rattrapage.main:fibonacci',
    ],
  },
)
