import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eucl_dist",
    version="1.0.1",
    author="Divakar Roy",
    description="Euclidean Distance Computation in Python for 4x-100x+ speedups over SciPy and scikit-learn. Also leverages GPU for better performance on specific datasets.",
    keywords="Euclidean Distance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/droyed/eucl_dist",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires = [
      'numpy',
      'pandas',
      'scipy',
      'scikit-learn',
      'scikit-cuda',
      'pycuda',
    ]
)