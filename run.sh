# run the tool analyzing both xss and sql vulnerabilities
./run-all.pl -a -A -g -y xss $1

# go to results forlder
cd graphs

# remove all _dep files
rm -f *_dep.dot
rm -f *.php.txt


