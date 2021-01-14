#!/bin/bash
FILES=/home/rubik/Documents/tibame/project/ETL/reviews/*.txt
for f in $FILES
  do 
    #sort -u "$f" > "./fixed/fixed_$(basename "$f")"
    sort -u "$f" > "./fixed/$(basename "$f")"
  done
