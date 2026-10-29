# OPDS and Other Readers

By the end of this chapter your e-reader
app — or any OPDS client — can browse
your Kavita shelves and fetch books from
them, and you have walked the same feed
the app walks, down to a real book. The
web interface is Kavita's reading room;
**OPDS** is the door other reading rooms
use.

## What OPDS is, in one paragraph

OPDS — Open Publication Distribution
System — is the standard way library
apps and e-readers browse a book server:
the server publishes **feeds**, simple
XML lists ("these are the libraries",
"these are the books in this library",
each with a download link), and the app
presents them its own way. It is the
same idea as RSS, for books. If an app
says it supports OPDS catalogues, it can
read from Kavita.

## Your address and your key

OPDS is **on by default**. Your personal
address is:

```text
http://<your-server>:5000/api/opds/<your API key>/
```

Two parts deserve attention:

- **The `/api` matters.** Leave it out
  and the address shows you the website
  instead — the lab's first fetch of
  `/opds/<key>/` returned the reading
  room's HTML, not a feed. The feed
  lives under `/api/opds/`.
- **The API key is the password.** Each
  account has its own key (you will find
  yours under your user settings, where
  Kavita shows the OPDS address ready to
  copy). Anyone holding the key browses
  and downloads as that account — with
  that account's library limits, which is
  the saving grace: the invited reader's
  key opens Lab Books and nothing else.
  Treat the key like a password, and
  regenerate it from your settings if it
  leaks.

Give a reader app that address and it
will prompt for nothing more; the key in
the address is the credential.

## Walking the feed

The lab read the feed the way an app
does, one list at a time. The root feed
introduces itself as a catalogue named
*Kavita* and offers the front doors:

```text
On Deck · Recently Updated · Recently Added ·
Reading Lists · Want to Read · All Libraries · All Collections
```

Follow **All Libraries** and the feed
names the libraries; follow one and it
lists the books, each an entry with the
series' title and its links:

```text
libraries/2  ->  A Short Paper on Rain, Sea of Paper Boats, The Clockwork Garden
```

An app takes it from there: cover
thumbnails from the feed, the book file
from the acquisition link, and reading
in the app's own reader. Progress made
in an outside app is the app's business;
progress in Kavita's own readers is
Kavita's (chapter 6). One known meeting
point: Kavita stores a **KOReader hash**
for every book file — the fingerprint
KOReader devices use to recognise a
book — which is the hook KOReader's
Kavita sync uses to tie a device to the
server. The lab recorded the hashes; a
real KOReader pairing needs the device,
and is described here, not demonstrated.

## When OPDS is the right door

- A **dedicated e-reader app** you
  already love, reading your Kavita
  shelf as one more catalogue.
- A **tablet or phone** where the
  app's reader beats a browser tab.
- **Downloading for offline** — the
  feed's whole purpose is fetching
  files, and the fetched file is your
  original, unchanged.

And when it is not: discovery and
organisation live in the web interface —
collections, lists, scans, users. OPDS
is a reading door, not an admin door.
