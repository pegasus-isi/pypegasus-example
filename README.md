# Prerequisites

1. Python >= 3.6
1. HTCondor
1. Pegasus

# Install

```sh
pip3 install git+https://github.com/pegasus-isi/pypegasus
# OR
pip3 install -e ../pypegasus .
```

# Workflow Example

`create_file_<i>` &#8594; `create_file_<i>`, where i &#8594; 1 .. *N*

# Usage

```sh
$ pypegasus-example --help

Usage: pypegasus-example [OPTIONS] N

  Py pegasus Example.

Options:
  --help  Show this message and exit.
```
