#!/bin/bash

#echo "Enter the json file to be fixed"
#read $1

#find " }{ " pattern and replace it with " },{ "
sed -i 's/\}{/\},{/g' $1

#add " [ " to the beginning of the file
sed -i '1i\[' $1

#append " ] " to the end of the file
sed -i '$a\]' $1

echo "Your $1 has been fixed"
