# Miraikumiko

My personal website

## Features

* Frontend - Vuejs
* Backend - Fastapi + SQLAlchemy

## Dependencies

* Python + pip
* Nodejs + npm
* Nginx
* OpenRC or Systemd

# Configuration

Frontend config `frontend/src/config.js` need setup API url:

```
export const API_URL = "https://miraikumiko.space/api"
```

Backend config `miraikumiko.conf` have 3 database engines `sqlite`, `mariadb` and `postgresql`:

```
[database]
TYPE        = sqlite
HOST        =
PORT        =
DATABASE    = ./miraikumiko.db
USERNAME    =
PASSWORD    =
```

# Installing

Working directory is in `/var/www/miraikumiko.space`

Copy config to `/etc/miraikumiko.conf`

## Setup frontend

```
cd frontend
npm i
npm run build
```

## Setup backend

```
python -m venv venv
. venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## Setup OpenRC

`cp contrib/openrc/miraikumiko /etc/init.d/miraikumiko`

## Setup Systemd

`cp contrib/systemd/miraikumiko.service /etc/systemd/system/miraikumiko.service`

# Setup Nginx

```
cp contrib/nginx/sites-available/miraikumiko.conf /etc/nginx/sites-available/miraikumiko.conf
ln -s /etc/nginx/sites-available/miraikumiko.conf /etc/nginx/sites-enabled/miraikumiko.conf
```

# Start

Create user and password:

`python run.py -n admin -p password`

## OpenRC

```
rc-update add miraikumiko default
rc-update add nginx default

rc-service miraikumiko start
rc-service nginx start
```

## Systemd

`systemctl enable --now miraikumiko nginx`
