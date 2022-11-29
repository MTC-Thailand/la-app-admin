import pandas as pd
import click
import random
import emoji

@click.command()
@click.argument('input_file')
def draw(input_file):
    df = pd.read_excel(input_file)
    max = len(df)
    success = set()
    while True:
        while True:
            idx = random.randint(1, max)
            if idx not in success:
                u = df.iloc[idx]
                print(f'{u["number"]} {u["firstname"]} {u["lastname"]}')
                break
        prompt = input('Success? ')
        if prompt == 'y':
            success.add(idx)
            print(emoji.emojize(':thumbs_up:'))
            print('=' * 20)
        else:
            print(emoji.emojize(':broken_heart:'))


if __name__ == '__main__':
    draw()



