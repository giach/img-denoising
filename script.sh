#!/bin/bash
ROOT=images

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

# output=`ls images/dominantcol/sp/ | grep 'fix*'`
# echo $output
# output=`ls images/dominantcol/gauss/  | grep 'fix*'`
# output=`ls images/fewcol/sp/  | grep 'fix*'`
# output=`ls images/fewcol/gauss/  | grep 'fix*'`
# output=`ls images/manycol/sp/  | grep 'fix*'`
# output=`ls images/manycol/gauss/  | grep 'fix*'`
# output=`ls images/people/sp/  | grep 'fix*'`
# output=`ls images/people/gauss/  | grep 'fix*'`