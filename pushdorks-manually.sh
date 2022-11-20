scp dorks_out.txt openssl@13.13.17.17:~
ssh openssl@13.13.17.17 'cat ~/dorks_out.txt >> ~/linkz.txt;rm ~/dorks_out.txt'
echo 1 > dorks_out.txt
ssh openssl@13.13.17.17 '~/init.sh'
ssh openssl@13.13.17.17 '~/output-result.sh'
scp openssl@13.13.17.17:~/vuln.out ./vuln.out
cat vuln.out >> results.txt
rm vuln.out
