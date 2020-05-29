#!/bin/bash
find $1 -maxdepth 1 -type f -exec python3 process_tsv.py {} \; > $2
