import click

@click.command()
@click.option('--name', default='мир', help='Кого приветствовать')
def hello(name):

    click.echo(f"Привет, {name}!")

if __name__ == '__main__':
    hello()