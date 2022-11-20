tmux new -s test -d

tmux selectp -t 0    # select the first (0) pane
tmux splitw -h -p 75 # split it into two horizontal parts
tmux selectp -t 0    # select the first (0) pane
tmux splitw -v -p 50 # split it into two vertical halves

# After this 3 panes will be created with pane number 0 (left- horizontal)
# Pane 1 (vertical pane under the pane 0)
# And Pane 2 with the remaining screen size 
# Then we divide this remaining pane 2 into three similar panes
# repeat this till all 8 panes are created

tmux selectp -t 2    # select the new, second (2) pane
tmux splitw -h -p 66 # split it into two halves
tmux selectp -t 2    # select the second (2) pane
tmux splitw -v -p 50 # split it into two vertical halves

tmux selectp -t 4    # select the new, fourth (4) pane
tmux splitw -h -p 50 # split it into two halves
tmux selectp -t 4    # select the fourth (4) pane
tmux splitw -v -p 50 # split it into two halves

tmux selectp -t 6    # select the new, sixth (6) pane
tmux splitw -v -p 50 # split it into two halves
tmux selectp -t 0    # go back to the first pane
tmux attach -t test

sleep 3s

tmux send-keys -t 0 'sh /opt/openssl/root/x1.sh' 'C-m'
tmux send-keys -t 1 'sh /opt/openssl/root/x2.sh' 'C-m'
tmux send-keys -t 2 'sh /opt/openssl/root/x3.sh' 'C-m'
tmux send-keys -t 3 'sh /opt/openssl/root/x4.sh' 'C-m'
tmux send-keys -t 4 'sh /opt/openssl/root/x5.sh' 'C-m'
tmux send-keys -t 5 'sh /opt/openssl/root/x6.sh' 'C-m'
tmux send-keys -t 6 'sh /opt/openssl/root/x7.sh' 'C-m'
tmux send-keys -t 7 'sh /opt/openssl/root/x8.sh' 'C-m'
