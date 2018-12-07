#!/usr/bin/env bash

set -ex

command -v aws || { echo "I require aws but it's not installed. Aborting." >&2; exit 1; }

REMOTE_MAPPINGS_DIR=s3://clamped90-photos
LOCAL_MAPPINGS_DIR=/volume1/photo

aws s3 sync $LOCAL_MAPPINGS_DIR $REMOTE_MAPPINGS_DIR --dryrun

exit 0
