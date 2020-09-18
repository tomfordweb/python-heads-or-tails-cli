import click

@click.command()
def headsOrTails():
    click.echo('hello world')


if __name__ == '__main__':
    headsOrTails()