import sys
from datetime import datetime

import pandas as pd
import openpyxl
import click

import firebase_admin
from firebase_admin import credentials, firestore
import pytz


def initialize_app(cer_file):
    cred = credentials.Certificate(cer_file)
    firebase_admin.initialize_app(cred)


@click.command()
@click.argument('cer_file',)
def download(cer_file):
    initialize_app(cer_file)
    records = []
    db = firestore.client()
    ch_ref = db.collection('users').stream()
    for doc in ch_ref:
        data = doc.to_dict()
        records.append({'lineId': data.get('lineId'),
                        'firstname': data.get('firstname'),
                        'lastname': data.get('lastname'),
                        'number': data.get('number'),
                        })
    df = pd.DataFrame(records)
    df.to_excel('new_users_{}.xlsx'.format(datetime.today().strftime('%Y%m%d')), index=False)


if __name__ == '__main__':
    download()
