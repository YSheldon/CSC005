#python /home/test/parser.py
cp -r /home/csc-dailynews/newsmarkdown/. /home/website/CSC005/_posts/.
git add .
git commit -m "daily"
git push -u origin gh-pages
