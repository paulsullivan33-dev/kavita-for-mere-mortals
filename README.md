# Kavita for Mere Mortals

Books pile up as files. An EPUB from one
shop, a PDF from another, a folder of
comics in zip files with hopeful names —
and every reader app wants to import its
own copy into its own silo. **Kavita**
takes the other approach. It is a
**reading server**: one program, running
on a machine in your house, that watches
folders of book and comic files you
already own, organises them into a
browsable library, and serves them back
to you — in a web browser, or in any
reader app that speaks **OPDS**, the
catalogue protocol libraries use. Your
files stay where they are. Kavita keeps
the catalogue, the covers, and your
place in every book.

One rule belongs up front, because it is
the tool's whole shape: Kavita is a
server for books you already have and
have the right to keep. It has no shop
and no sources of its own. What you put
in is what it serves, to the people you
invite.

This guide explains the shape of the
thing — libraries, series, volumes, and
the scanner that reads your folders —
then installs it, builds a first library
from real files, and reads real books
out of it. The lab behind the guide ran
**Kavita 0.9.1.4**, the official Linux
release, and stocked it with a small
library it made itself: two short EPUB
books whose text was written for the
lab, a one-page PDF, and a drawn comic
series in CBZ files, one carrying a
`ComicInfo.xml` metadata file. Against
that library it registered the first
admin account, created two libraries,
watched the scanner succeed — and fail,
instructively, when a library had not
been told to accept EPUB files — read
an EPUB chapter and a comic page back
out of the server and compared the comic
page byte for byte with the page inside
the CBZ, invited a second reader and
checked exactly which books that reader
could and could not see, built a
collection and a reading list, and
walked the OPDS feed down to the book
entries an e-reader app would show.

What the lab could not do, it did not
fake. There was no browser in the lab,
so the readers were verified by what
they serve — the exact HTML of a book
chapter, the exact bytes of a comic
page — and how the pages *look* on a
screen is left to you. Email delivery of
invites needs a mail server the lab did
not have, so the invite was completed by
handing over the link Kavita produced;
that difference is stated where it
matters. `criteria.md` keeps the full
ledger of what was run and what was only
read.

## What this guide covers

- [**What Kavita is**](what-kavita-is.md) —
  the mental model: your files stay put,
  the server keeps the catalogue and your
  place, and the household rule about
  whose books belong here
- [**The moving parts**](the-moving-parts.md) —
  libraries, series, volumes, chapters,
  the scanner, and the organising tools —
  collections, reading lists, want to
  read — and which part holds what
- [**Installing Kavita**](installing-kavita.md) —
  the release download, the single
  executable, the config folder it grows,
  and the checks that prove it is up
- [**Your first library**](your-first-library.md) —
  the first account (which becomes the
  admin), pointing a library at a folder,
  and the scan that fills it
- [**How the scanner reads your files**](how-the-scanner-reads.md) —
  folders and filenames for comics, the
  metadata inside EPUB and ComicInfo
  files for books, the four file groups a
  library can accept, and the lab's own
  empty-library mistake
- [**Reading books in Kavita**](reading-books.md) —
  the book reader, what a "page" is in an
  EPUB, word counts, and how your place
  is kept
- [**Reading comics and PDFs**](reading-comics.md) —
  the image reader page by page, covers,
  and the PDF's simpler treatment
- [**Users and sharing**](users-and-sharing.md) —
  inviting readers, what an invited
  reader can see, and the library wall
  between accounts, checked from both
  sides
- [**Collections, reading lists and want to read**](collections-lists-and-want-to-read.md) —
  three different answers to "group some
  books": across libraries, in a set
  order, and on your own shelf
- [**OPDS and other readers**](opds-and-other-readers.md) —
  the catalogue feed e-reader apps speak,
  your personal API key as the password,
  and the feed walked down to real books
- [**Recipes**](recipes.md) — a household
  shelf, a comics folder tamed, a
  read-it-later shelf, and handing a
  guest reader one library only
- [**The neighbours**](the-neighbours.md) —
  the plain folder and the desktop
  reader, and Calibre: what each does
  that Kavita doesn't, and vice versa
- [**Limits**](limits.md) — files it
  cannot read, metadata it cannot invent,
  PDFs as second-class citizens, and a
  scanner whose quality is your folders'
  quality
- [**Troubleshooting**](troubleshooting.md) —
  the empty library, the book that never
  appears, the invite nobody received,
  the OPDS address that shows the website
  instead, and the traps this guide's lab
  fell into
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Finding or buying books — Kavita starts
where the files already exist. Removing
DRM, converting formats, and repairing
broken EPUBs are other tools' work;
Calibre, which has its own guide in this
series, is the usual workbench for all
three. Running a public book service for
strangers is out of scope and against
the household rule above: this is a home
library server, sized and shaped for
one.

## How to use this guide

Read chapter 1 for the model and chapter
2 before installing anything — knowing
which part holds what turns later
confusion into a named problem. Chapters
3 and 4 get you a running server with
real books in it in the same sitting.
Chapter 5 is the one to read slowly: the
scanner's rules explain nearly every
"why isn't my book there?" you will ever
ask. The lab's transcripts live in
`kavita-lab/transcripts/`, and the
script that made the lab's books is
`kavita-lab/make-books.py`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Calibre for Mere Mortals](https://paulsullivan33-dev.github.io/calibre-for-mere-mortals/)
- [PhotoPrism for Mere Mortals](https://paulsullivan33-dev.github.io/photoprism-for-mere-mortals/)
- [Jellyfin for Mere Mortals](https://paulsullivan33-dev.github.io/jellyfin-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/kavita-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/kavita-for-mere-mortals/blob/main/LICENSE-CODE).
