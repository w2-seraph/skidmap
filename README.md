# skidmap
Automated mass dorking to sqlmap operations
![ezgif-1-33463bc290](https://user-images.githubusercontent.com/24370258/202878598-54f80b6a-5b31-4c97-8255-7a8828c89e7e.gif)

Usage

1. Establish key authentication to remote server used in "pushdorks.sh" (ssh-copy-id)
2. Copy contents of ./sqlmap to remote server home directory
3. Edit pushdorks.sh accordingly (remote server ip and user)
4. Generate dorks with provided tools
4. Run skidmap.sh

Explanation

  Acts as URL scraping C2 to a remote sqlmap installation, sends sqlmap collected urls and deals with starting/stopping it. The idea was full automation and honeypot resilience. (granted enough dorks are supplied)
