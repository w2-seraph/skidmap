result=`ps aux | grep -i "sqlmap" | grep -v "grep" | wc -l`
if [ $result -ge 3 ]
   then
        echo "[~]sqlmap is still running"
   else
        echo "[+]sqlmap not running"
        echo "[-]stopping tmux"
        pkill tmux
        echo "[+]starting tmux multiplexer with python process"
	cd ~ && sh ~/splitlinkz.sh
        cd ~ && sh ~/tmux-6split-cmd.sh
        echo "[+]finished"
fi
