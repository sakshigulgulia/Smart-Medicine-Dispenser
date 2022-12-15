#!/bin/sh

rm -rf /Prescriptions/*

python3 firebase_download.py

python3 gsheet_easyocr.py Prescriptions