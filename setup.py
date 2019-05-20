import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='frechfrechfrech_first_package-frechfrechfrech',
      version='0.2',
      author='Alex Frech',
      author_email='frechfrechfrech@gmail.com',
      description='My first package attempt',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/frechfrechfrech/frechfrechfrech_first_package',
      license='MIT',
      packages=setuptools.find_packages(),
      # zip_safe=False,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
