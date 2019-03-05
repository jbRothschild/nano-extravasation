#!/bin/bash
# script that downloads everything to the right foldeer

TMPFILE='temp.zip'; PWD=$(pwd); DATADIR='data';
mkdir ${DATADIR}
wget "https://ndownloader.figshare.com/files/14019401" -O ${TMPFILE}
unzip -d ${PWD}/${DATADIR} ${TMPFILE}
rm ${TMPFILE}
