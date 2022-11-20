cat /opt/openssl/root/.local/share/sqlmap/output/*.csv > vuln.out
python3 /opt/openssl/root/same-domain-vuln.py
python3 /opt/openssl/root/same-domain-linkz.py
