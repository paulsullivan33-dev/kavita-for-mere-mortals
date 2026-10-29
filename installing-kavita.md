# Installing Kavita

By the end of this chapter Kavita is
running on your machine, answering on
port 5000, and you have the two checks
that prove it: the web page and the
health endpoint. The install is
unusually simple — Kavita ships as one
self-contained program per platform. No
database to set up, no runtime to
install, no web server in front of it.

## Get the release

Download the archive for your platform
from the project's GitHub releases page.
For a 64-bit Linux machine the file is
named like this (the version number
will have moved on; the lab used
0.9.1.4):

```bash
curl -LO https://github.com/Kareadita/Kavita/releases/download/v0.9.1.4/kavita-linux-x64.tar.gz
```

There are matching archives for ARM
Linux, Windows, and macOS in the same
release. The archive is about 118 MB —
the size is the embedded runtime and
web application; there is nothing else
to fetch.

Unpack it where it will live. Your home
folder is fine for a first run:

```bash
mkdir -p ~/kavita-server
tar -xzf kavita-linux-x64.tar.gz -C ~/kavita-server
```

Inside is a folder `Kavita` holding
hundreds of library files and one
executable, also named `Kavita`. Make
sure the executable bit is set:

```bash
chmod +x ~/kavita-server/Kavita/Kavita
```

## First run

Start it from its own folder:

```bash
cd ~/kavita-server/Kavita
./Kavita
```

The first run does real work before it
serves anything: it creates its
**config folder** (`config/` next to the
executable), builds the database,
generates the secret key it signs user
sessions with, and runs its migrations.
On the lab's small shared machine that
took the better part of a minute. The
lines you are waiting for are:

```text
[Kavita] [Information] Kavita.Server.Program Kavita - v0.9.1.4
[Kavita] [Information] Microsoft.Hosting.Lifetime Now listening on: http://[::]:5000
```

Leave it running. (Keeping it running
across reboots — a systemd unit on
Linux, a scheduled task on Windows — is
ordinary service plumbing for your
platform; the program itself neither
knows nor cares.)

Two things the first run decided for
you, worth knowing now:

- **Config lives with the program.** The
  `config` folder holds `kavita.db`,
  `appsettings.json` (port, base URL),
  `logs/`, and the extracted covers.
  Move the folder and you move the
  server's memory.
- **Port 5000, all interfaces.** Kavita
  listens on every network address of
  the machine, which is what a home
  server should do — and why it belongs
  on a network you trust. To change the
  port, edit `Port` in
  `config/appsettings.json` and restart.

## The checks

With the server up, prove it from a
second terminal:

```bash
curl http://127.0.0.1:5000/api/health
```

The answer is one word:

```text
Ok
```

And the reading room itself:

```bash
curl -s http://127.0.0.1:5000/ | grep -o '<title>[^<]*</title>'
```

```text
<title>Kavita</title>
```

Point a browser on the same machine at
`http://127.0.0.1:5000` and you get the
welcome screen asking you to create the
first account — which is chapter 4,
where the server also meets its first
books.

## What is not in this install

There is no installer wizard, no
database prompt, and nothing to phone
home for: the release runs offline, and
the lab ran it exactly that way. Docker
images exist for Kavita and are a fine
route on a machine that already runs
containers; this guide uses the plain
binary so that what is running, and
where its files are, is never in doubt.
