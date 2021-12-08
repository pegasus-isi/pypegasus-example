"""Py pegasus_example Example."""
import json
from pathlib import Path

import click
from pypegasus import Input, Output, task, workflow

from . import mod1
from .mod2 import y


def x():
    print("X" * 1000)


@task()
def create_file(n, out: Output):
    x()
    mod1.y()
    y()
    _out: Path = Path(out)
    _out.resolve()
    with _out.open("w") as f:
        f.write(f"N = {n}\n")


@task()
def clone_file(in_: Input, out: Output):
    """."""
    _out: Path = Path(out)
    with _out.open("w") as f:
        f.write("Child\n")
        f.write(open(in_, "r").read())


def n():
    a = lambda: 100
    b = 1

    @task()
    def func():
        print("AA", a, b)

    return func


nn = n()


class Z:
    def __init__(self, xx=100):
        self.xx = xx

    @task()
    def z(self, z):
        print("Class Z", self.xx, z)


@workflow("adag")
def run(n):
    """."""
    for i in range(n):
        create_file(i, out=f"f{i}.txt")
        clone_file(f"f{i}.txt", out=f"f{i}-child.txt")
    nn()
    # Z(999).z(1)


@click.command()
@click.pass_context
@click.argument(
    "n",
    required=True,
    type=int,
)
def pypegasus_example(ctx, n):
    """Py pegasus Example."""
    try:
        run(n)
    except Exception as e:
        _error(ctx, e)

    click.secho("✨ Success", fg="green")


def _error(ctx, e, ec=1):
    click.secho(f"Message: {str(e)}", fg="red")
    click.secho("Error", fg="red")
    e.x
    ctx.exit(ec)
