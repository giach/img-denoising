#!/bin/bash

# relative/absolute path to the image set
ROOT=images

echo "Remove the generated images"
categories=`ls $ROOT`
for cat in $categories
do
  echo "$cat category"
  path_sp=$ROOT/$cat/sp/
  path_gauss=$ROOT/$cat/gauss
  
  # remove the images from sp directories
  fix_sp=`ls $path_sp | grep 'fix*'`
  for fix_sp_cat in $fix_sp
  do
  	rm $ROOT/$cat/sp/$fix_sp_cat/* >& /dev/null
  done
  echo "Done removing the images from the sp directory"

  # remove the images from gauss directories
  fix_gauss=`ls $path_gauss | grep 'fix*'`
  for fix_gauss_cat in $fix_gauss
  do
  	rm $ROOT/$cat/gauss/$fix_gauss_cat/* >& /dev/null
  done
  echo "Done removing the images from the gauss directory"
  echo ""

done
