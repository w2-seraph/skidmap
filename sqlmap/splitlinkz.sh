rm xa*
cd /opt/openssl/root/ && cp /opt/openssl/root/linkz.txt /opt/openssl/root/linkz.txt.bak
cd /opt/openssl/root/ && split -n 8 /opt/openssl/root/linkz.txt
cd /opt/openssl/root/ && echo > /opt/openssl/root/linkz.txt
