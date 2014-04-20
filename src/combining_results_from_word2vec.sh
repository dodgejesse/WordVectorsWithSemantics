#!/bin/bash
TOPDIR=/cab1/jessed/pgm_project/WordVectorsWithSemantics
RESULTS=${TOPDIR}/results/*
TOTAL=${TOPDIR}/scratch/end_result.txt
touch $TOTAL
for f in $RESULTS
do
    echo "$f" >> $TOTAL
    tail -2 $f >> $TOTAL
    echo "\n" >> $TOTAL
done