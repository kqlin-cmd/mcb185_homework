#!/bin/bash

zcat ../MCB185/data/dictionary.gz \
| grep -E '^.{4,}$' \
| grep -i 'r' \
| grep -iv '[^acinorz]'
