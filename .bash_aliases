    alias solution='git add solution.py && git commit -m 'commit' && git push -u origin master'
    alias mon='gnome-system-monitor'
    alias update='sudo apt-get update && sudo apt-get dist-upgrade && sudo apt-get autoremove && sudo apt-get clean'
    alias descartes='nmcli nm enable true ; nmcli nm wifi on ; nmcli con up id "DESCARTES" ; firefox https://wall3.univ-paris5.fr:8001/index.php?redirurl=https%3A%2F%2Fduckduckgo.com ; sleep 8s ; firefox www.gmail.com'
    alias ndescartes='killall firefox ; nmcli con down id 'DESCARTES' ; nmcli nm wifi off'
    alias con='firefox https://wall3.univ-paris5.fr:8001/index.php?redirurl=https%3A%2F%2Fduckduckgo.com'
