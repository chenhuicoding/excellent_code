#!/bin/bash
#filename: cut_access_log.sh

LOGS_PATH="/var/log/message/"

mkdir -p ${LOGS_PATH} $(date -d "yesterday" +"%Y")/$(date -d "yesterday" +"%m")/

mv ${LOGS_PATH}access.log ${LOGS_PATH}$(date -d "yesterday" +"%Y")/$(date -d "yesterday" +"%m")/access_$(date -d "yesterday" +"%Y%m%d").log

# use crontab to cut the log file regularly
# crontab -e
# 00 00 * * * /bin/bash cut_access_log.sh
