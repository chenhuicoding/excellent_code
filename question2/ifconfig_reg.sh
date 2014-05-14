#!/bin/bash
# Program
# parse the output of ifconfig and return hash
#History
#2014/5/14
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin

read -p "please input ifconfig: " config
hash=eval $config | grep -A 1  'Link encap' |sed '/--/d' | sed 's/Link.*$//g'| sed 's/^.*addr://g' | sed 's/Bcast.*$//g' | sed 's/Mask.*$//g'| awk '{if(NR%2==0) {print $0} else {printf"%s ",$0}}'
echo $hash
