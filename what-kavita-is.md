# What Kavita Is

You have books as files — EPUBs, PDFs,
comics in CBZ zips — spread across
folders, disks, and download histories.
Every reading app you have ever used
wants to *import* them: copy them into
its own library, keep its own covers and
its own record of where you stopped, and
know nothing about the copies in your
other apps. Read on three devices and
you keep three libraries that disagree.

**Kavita is a reading server.** It is
one program that runs on a computer in
your house — a small server, a desktop
that stays on, a home-lab box. You point
it at the folders where your book and
comic files already live. It reads those
folders, builds a catalogue — series,
covers, authors, summaries, page counts
— and then *serves the books back to
you*: in a web page on any browser in
the house, and through **OPDS**, the
standard catalogue feed that e-reader
apps and library apps speak. The files
never move and are never copied into a
silo. Kavita's database holds the
catalogue and each reader's progress;
the books stay ordinary files on disk,
yours, readable without Kavita at all.

That separation is the feature. One
library, kept in one place, read from
everywhere: start a chapter on the
laptop, finish it on a tablet, and the
server — not your memory — knows the
page. Add a reader for each person in
the house and each gets their own
progress, their own shelves, and only
the libraries you gave them (chapter 8
checks that wall from both sides).

## The household rule

Kavita serves what you feed it, to the
people you invite, and nothing else. It
has no shop, no built-in sources, and no
way to fetch books you do not already
have. So the rule of this guide, stated
before any procedure depends on it:
**only put in books you own and have the
right to keep, and share them the way
you would share a physical shelf** — with
your household, not the internet. A
Kavita server is a bookcase with a good
catalogue, not a distribution channel.

## A first taste

After installing (chapter 3) and making
the first account (chapter 4), the
server answers on port 5000. The
plainest possible check that it is
alive:

```bash
curl http://127.0.0.1:5000/api/health
```

```text
Ok
```

And the library it serves is ordinary
web traffic — a browser pointed at
`http://127.0.0.1:5000` gets the reading
room itself. Everything in this guide
after chapter 4 is, underneath the web
interface, that same traffic: the lab
drove it through Kavita's API so every
step could be shown and checked.

## What it is not

Kavita is not a bookshop and not a
source: it cannot find, buy, or download
books. It is not a converter or a repair
shop — it reads EPUB, PDF, CBZ/CBR and
image files as they are, and files that
are broken or protected stay unreadable
(chapter 12). It is not a DRM tool, in
either direction: it neither adds nor
removes protection, and protected files
simply will not open. It is not a public
library platform for strangers — user
accounts are invitations you send, and
registration closes itself after the
first account (the lab tried; chapter
8). And it is not the only way to read:
chapter 11 is honest about the plain
folder and the desktop reader, which for
one person and one machine may be all
anyone needs.

## Who it is for

The household with books scattered
across three computers and a NAS. The
comics reader whose collection outgrew
folders-with-thumbnails. The manga
reader who wants volumes in order and a
server that remembers the chapter. The
parent who wants the children to have
the family library but not the horror
shelf — libraries are granted per reader
(chapter 8). The common thread is the
same as the tool's design: many files,
more than one reader or device, and a
wish for one catalogue that knows where
everybody stopped.
