# A telegram bot that accepts magnet links and starts the download on your vps
This idea had two main reasons. Firstly torrent downloads seemed to always be slower than normal direct download speeds. I wanted a way to improve that. Secondly, in torrenting seeding is always important so you can give back to the community. But with Iran's internet speed and price no one cared about that. So now that people are buying personal VPSs for their VPN needs. they might as well use it for other reasons.

## It's very important to know that every vps provider is not ok with you torrenting on their vps. and this can get you suspended. Remember to check before doing this.

### Steps to run the program
clone this repo
```bash
git clone https://github.com/parsamrrelax/todirectlink
```
cd to it's directory where the repo is cloned.
In telegram from botfather. create a new telegram bot and get your bot token and replace it with BOT-TOKEN inside of py.py
```bash
nano py.py
```
then run first.sh
```bash
bash first.sh
```
after the installation is done. edit the nginx file with your editor.
```bash
nano /etc/nginx/sites-enabled/default
```
add this to your server block
```
   location /downloads {
       alias /var/lib/transmission-daemon/downloads/;
       autoindex on;
   }
```
after that run
```bash
nohup python3 py.py
```
Now if you open your telegram bot. It will ask your for a magnet link. Send it a magnet link and it will download and seed it for you.
You can access the files via http://YOURSERVERIP/downloads and direct download or stream them.

if you want to use HTTPS which you should. get ssl certificates via acme.sh and add this code to your server block in nginx config
```bash
nano /etc/nginx/sites-enabled/default
```

```
   listen 443 ssl;
   ssl_certificate /path/to/cert;
   ssl_certificate_key /path/to/privatekey;
```
Now you can access the files via HTTPS and even with your domain.