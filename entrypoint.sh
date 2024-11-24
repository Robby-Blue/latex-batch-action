#!/bin/sh
python3 /batch_compile.py $1
cd pdfs
zip -r /github/workspace/pdfs.zip .