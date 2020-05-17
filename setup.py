from setuptools import setup
from Cython.Build import cythonize

setup(name="qpt_generator",
      version="0.1",
      description="Question Paper Template Generator",
      author="Niraj Kamdar",
      ext_modules=cythonize('qpt_generator.pyx'),
      license='MIT',
      url='https://github.com/Niraj-Kamdar/qpt_generator',
      download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
      keywords=['question', 'paper', 'template', 'generator'],
      install_requires=[
          'cython',
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      )
