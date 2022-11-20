cat ~/.local/share/sqlmap/output/*.csv > vuln.out
python3 ~/same-domain-vuln.py
python3 ~/same-domain-linkz.py
