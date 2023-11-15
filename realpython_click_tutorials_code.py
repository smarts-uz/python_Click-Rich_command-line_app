# ls.py v1
#
# from pathlib import Path
#
# import click
#
# @click.command()
# @click.argument("path")
# def cli(path):
#     target_dir = Path(path)
#     if not target_dir.exists():
#         click.echo("The target directory doesn't exist")
#         raise SystemExit(1)
#
#     for entry in target_dir.iterdir():
#         click.echo(f"{entry.name:{len(entry.name) + 5}}", nl=False)
#
#     click.echo()
#
# if __name__ == "__main__":
#     cli()
#
#
#
# ls.py v2

# from pathlib import Path
#
# import click
#
# @click.command()
# @click.argument(
#     "path",
#     type=click.Path(
#         exists=True,
#         file_okay=False,
#         readable=True,
#         path_type=Path,
#     ),
# )
# def cli(path):
#     for entry in path.iterdir():
#         click.echo(f"{entry.name:{len(entry.name) + 5}}", nl=False)
#
#     click.echo()
#
# if __name__ == "__main__":
#     cli()


# ls.py v3

from pathlib import Path

import click

@click.command()
@click.argument(
    "paths",
    nargs=-1,
    type=click.Path(
        exists=True,
        file_okay=False,
        readable=True,
        path_type=Path,
    ),
)
def cli(paths):
    for i, path in enumerate(paths):
        if len(paths) > 1:
            click.echo(f"{path}/:")
        for entry in path.iterdir():
            click.echo(f"{entry.name:{len(entry.name) + 5}}", nl=False)
        if i < len(paths) - 1:
            click.echo("\n")
        else:
            click.echo()

if __name__ == "__main__":
    cli()