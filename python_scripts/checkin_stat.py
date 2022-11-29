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
    ch_ref = db.collection('checkins').stream()
    for doc in ch_ref:
        data = doc.to_dict()
        today = datetime(2022, 11, 28).date()
        dt = data['checkedAt'].astimezone(pytz.timezone('Asia/Bangkok'))
        if dt.date() == today:
            records.append({'datetime': dt.strftime('%Y-%m-%d %H:%M'),
                         'method': data['method'],
                         'number': data['number']})
    df = pd.DataFrame(records)
    df.to_excel('checkin_{}.xlsx'.format(today.strftime('%Y%m%d')), index=False)


if __name__ == '__main__':
    download()
