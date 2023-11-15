# importing click
import click

# @click.command()
# def main():
# 	click.echo("This cli is built with click. ")
#
# if __name__=="__main__":
# 	main()


# @click.command()
# @click.argument('name')
# def greeting(name):
# 	click.echo("Hello, {}".format(name))
#
#
# if __name__ == "__main__":
# 	greeting()



# @click.command()
# @click.option('--string', default='World',
# 			  help='This is a greeting')
# def hello(string):
# 	click.echo("Hello, {}".format(string))
#
#
# if __name__ == "__main__":
# 	hello()

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()