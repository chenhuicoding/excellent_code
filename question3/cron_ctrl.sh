#!/bin/bash

CRON_PATH=/var/spool/cron/crontabs
jobname=$1
if [ "$2" == "--stop" ]; then
    cat $CRON_PATH/$USER | grep $jobname 
    sed -i 's/^\(.*'"$jobname"'.*\)$/\#\1/' /var/spool/cron/crontabs/$USER
    cat $CRON_PATH/$USER | grep $jobname 
elif [ "$2" == "--start" ]; then
    cat $CRON_PATH/$USER | grep $jobname 
    sed -i 's/^#\(.*'"$jobname"'.*\)$/\1/' $CRON_PATH/$USER
    cat $CRON_PATH/$USER | grep $jobname 
elif [ "$2" == "--list" ]; then
    result=`grep ^#.*"$jobname".* $CRON_PATH/$USER`
    if  [ "$result" != "" ] ; then
        echo "stop"
       # echo $result
    else
        echo "start"
      #  echo $result
    fi
else
    echo "input correct subcommand"
fi

