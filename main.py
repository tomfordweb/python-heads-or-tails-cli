import click
import random

@click.command()
@click.option('--count', prompt='How many rolls')
@click.option('--sides', prompt='How many sides')
def command(count, sides):
    click.echo('Rolling a D%s %s time(s)' % (count, sides))
    sides = int(sides)
    for i in range(1, int(count)):
        rollDice(i, sides)



def rollDice(iterator, sides):
    result = random.randint(1, sides)
    result = str(result)
    click.echo('Roll %s: %s' % (iterator, result))

if __name__ == '__main__':
    command()