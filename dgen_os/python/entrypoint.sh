#!/bin/sh -l

set -e

echo "#################################################"
echo "Starting ${GITHUB_WORKFLOW}:${GITHUB_ACTION}"

sh -c "$*"
#cd "$(/Users/msizemor/dgen/dgen_os/python/ "$0")"
python dgen_model.py

echo "#################################################"
echo "Completed ${GITHUB_WORKFLOW}:${GITHUB_ACTION}"
