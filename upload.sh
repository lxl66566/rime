#!/usr/bin/env bash

set -exof pipefail

git-se e
git commit -a --allow-empty-message -m "$*"
git push origin main
