#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pandas as pd
import openpyxl
import click

import firebase_admin
from firebase_admin import credentials, firestore


def initialize_app(cer_file):
    cred = credentials.Certificate(cer_file)
    firebase_admin.initialize_app(cred)


@click.command()
@click.argument('cer_file',)
@click.argument('input_file')
def upload(cer_file, input_file):
    initialize_app(cer_file)
    db = firestore.client()
    user_ref = db.collection('users')
    df = pd.read_excel(input_file, dtype={'passcode': object, 'phone': object})
    for idx, row in df.iterrows():
        row['licenseId'] = '{:.0f}'.format(row["licenseId"]) if row['licenseId'] else ''
        data = row.to_dict()
        data['lineId'] = ''
        user_ref.add(data)
        print(f'{row["firstname"]} {row["lastname"]}')


if __name__ == '__main__':
    upload()