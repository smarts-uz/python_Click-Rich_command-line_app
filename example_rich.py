# from rich import print
#
# print("Hello, [bold green]Geeks[/bold green]!")

from time import sleep
from rich.console import Console

console = Console()
tasks = [f"Task {n}" for n in range(1, 8)]

with console.status("[bold dark_orange]Finishing tasks...") as status:
	while tasks:
		task = tasks.pop(0)
		sleep(1)
		console.log(f"{task} complete")
