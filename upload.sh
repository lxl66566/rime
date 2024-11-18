#!/usr/bin/env bash

set -exof pipefail

python tools/format_custom_phrase.py
git add -A
git commit -a --allow-empty-message -m "$*"
git push origin master

