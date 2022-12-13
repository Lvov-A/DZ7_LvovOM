from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.1',
      description='Very useful code',
      url='vstavit ssilku na github',
      author='Lvov Oleksii',
      author_email='lvovlvov92@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:start']}
)
