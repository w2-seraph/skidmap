cat ak-vgull.ans
echo "[+] Initializing tmux panes..."

result=`ps aux | grep -i "tomcat" | grep -v "grep" | wc -l`
if [ $result -ge 1 ]
   then
        echo "[~] tmux is still running pls kill it"
   else

   sleep 3
   tmux new -s fest -d

   tmux selectp -t 0    # select the first (0) pane
   tmux splitw -v  # split it into two horizontal parts
   tmux selectp -t 0    # select the first (0) pane
   tmux splitw -v  # split it into two vertical halves

   sleep 2s
   tmux select-layout even-vertical
   tmux send-keys -t 0 'python3 searx-a.py' 'C-m'
   tmux send-keys -t 1 'python3 searx-b.py' 'C-m'
   tmux send-keys -t 2 'python3 searx-c.py' 'C-m'
   sleep 1s
   tmux attach-session

fi
