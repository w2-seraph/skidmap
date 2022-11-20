python3 comparison-nonverb.py
sleep 5s
cp dorks_out.txt ./sqlmap/dorks_out.txt
cat ./sqlmap/dorks_out.txt >> ./sqlmap/linkz.txt;rm ./sqlmap/dorks_out.txt'
echo 1 > dorks_out.txt
sh ./sqlmap/init.sh
sh ./sqlmap/output-result.sh
cp ./sqlmap/vuln.out ./vuln.out
cat vuln.out >> results.txt
rm vuln.out
