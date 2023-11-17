import click
from rich.console import Console
from rich.table import Table

@click.group()
def cli():
    pass

@cli.command()
@click.option('-n', '--name', default='World', help='Name to greet')
def hello(name):
    """Simple program that greets NAME for a given number of TIMES."""
    console = Console()
    console.print(f"Hello, [bold magenta]{name}![/bold magenta]")

@cli.command()
@click.option('-c', '--count', default=1, help='Number of greetings')
@click.argument('name')
def greet(count, name):
    """Greet NAME multiple TIMES."""
    console = Console()
    for x in range(count):
        console.print(f"Hello {name}!")

@cli.command()
def list():
    """List all users."""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID")
    table.add_column("Name")
    table.add_row("1", "Alice")
    table.add_row("2", "Bob")
    console = Console()
    console.print(table)

if __name__ == '__main__':
    cli()