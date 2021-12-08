import os

from setuptools import setup

src_dir = os.path.dirname(__file__)
home_dir = os.path.abspath(os.path.join(src_dir, "../.."))

install_requires = ("Click",)  # "pypegasus",


# TODO: Someday remove this method and replace with setuptools.find_namespace_packages
def find_namespace_packages(where):
    pkgs = []
    for root, dirs, _ in os.walk(where):
        root = root[len(where) + 1 :]
        for pkg in dirs:
            if pkg == where or pkg.endswith(".egg-info") or pkg == "__pycache__":
                continue

            pkgs.append(os.path.join(root, pkg).replace("/", "."))

    return pkgs


setup(
    name="pypegasus-example",
    version="0.0.1",
    author="Pegasus Team",
    author_email="pegasus@isi.edu",
    description="Pegasus Workflow Management System Python API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="Apache2",
    url="http://pegasus.isi.edu",
    python_requires=">=3.6",
    keywords=["scientific workflows"],
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
    ),
    entry_points={
        "console_scripts": (
            "pypegasus-example = pypegasus_example.__main__:pypegasus_example",
        ),
    },
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
)
