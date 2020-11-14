#!/bin/bash

echo "Enter the json file to be fixed"
read json_file

#find " }{ " pattern and replace it with " },{ "
sed -i 's/\}{/\},{/g' $json_file

#add " [ " to the beginning of the file
sed -i '1i\[' $json_file

#append " ] " to the end of the file
sed -i '$a\]' $json_file

echo "Your $json_file has been fixed"
