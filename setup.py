from setuptools import setup
from setuptools import find_packages


from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name='fibotestunitaire',
  version='1.0.0',
  #long_description=readme,
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Zounaikha',
  author_email='zounaikha111@gmail.com',
  url='https://github.com/zounaikha/M1-2022-rattrapage',
  packages=find_packages(),
  entry_points={
    'console_script':[
      'hello-world-cli = M1_2022_rattrapage.main:fibonacci',
    ],
  },
)
