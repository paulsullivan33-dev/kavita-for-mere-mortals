# The Moving Parts

By the end of this chapter you can name
every part of Kavita and say which part
holds what — so that when something
looks wrong later, you know which part
to interrogate. There are six parts:
the server, the library, the scanner,
the series shelf (series, volumes,
chapters), the readers' layer (accounts
and progress), and the organisers
(collections, reading lists, want to
read). OPDS rides on top of all of them.

## The server

Kavita itself is a single self-contained
program with a web application and an
API inside it. It keeps everything it
knows in one **config folder**: an
SQLite database (`kavita.db`), the cover
images it extracted, its logs, and its
settings file. Nothing else on the
machine is touched. Back up that folder
and you have backed up Kavita — the
books themselves are your own files, in
your own folders, backed up the way you
back up any files.

The server answers on **port 5000** by
default, on every network interface, and
the port can be changed in
`config/appsettings.json`. It is a home
server: it expects to sit on a network
you control.

## Libraries

A **library** is Kavita's unit of
organisation and of permission. Each
library has:

- a **type** — Book, Manga, Comic, Image
  or Light Novel — which tells the
  scanner what shapes of series to expect;
- one or more **root folders** on disk
  that it watches;
- a set of **file groups** it accepts —
  archives, EPUB, PDF, images. A file
  whose group is not switched on for
  that library is invisible to it
  (chapter 5 is built around this);
- switches for folder watching,
  dashboard visibility, and the
  organising tools below.

You might keep one library for books and
one for comics, as this guide's lab
does, or split by audience — the
children's library and the grown-ups'
library — because access is granted per
library (chapter 8).

## The scanner

The **scanner** is the worker that turns
folders into catalogue. It walks a
library's root folders, groups files
into series (chapter 5 gives its rules),
reads the metadata it can find — inside
EPUB files, inside `ComicInfo.xml`
files in comic archives, in filenames
and folder names — counts pages, pulls
or draws cover images, and writes it all
into the database. A scan runs when a
library is created, when you ask for
one, and on a schedule; folder watching,
where it is switched on, asks for scans
when files change. The scanner never
modifies your files.

## Series, volumes, chapters

Everything the scanner finds lands in a
three-level shelf:

- A **series** is the named thing a
  reader looks for: *The Clockwork
  Garden*, *Starlight Ferry*. It carries
  the metadata — summary, writers,
  genres, cover.
- A **volume** groups chapters. Comics
  and manga live here naturally (Volume
  1, Volume 2). A single book usually
  sits in one unnamed volume.
- A **chapter** is one readable unit —
  in practice, one file. One EPUB is one
  chapter. One CBZ volume is one chapter
  whose pages are the images inside it.
  Reading progress is kept per chapter.

This is why the same machinery serves a
novel and a manga shelf without caring
which is which: both are series of
chapters, and the differences are in how
the chapters are rendered (chapters 6
and 7).

## Readers: accounts and progress

Every person gets an **account**.
Accounts are created by invitation from
an admin (chapter 8); the first account,
created at first run, is the admin.
Each account has its own reading
progress, its own ratings, and its own
shelves — and sees only the libraries an
admin granted it. Progress is recorded
as pages read per chapter, which powers
the "continue reading" shelf and the
per-series page counters.

## The organisers

Three tools group books, and they are
easy to confuse because they rhyme:

- A **collection** is a labelled set of
  series — "Award winners", "Start here"
  — that can span libraries. Admins make
  them; everyone sees them.
- A **reading list** is an ordered list
  of *chapters* — a reading order, for a
  series-spanning storyline or a course
  of books. Order is the point.
- **Want to read** is your private
  to-read shelf: series you mean to get
  to, kept per account.

Chapter 9 puts one of each on the lab's
shelves and shows how they differ in
practice.

## OPDS

Underneath everything sits **OPDS**, the
Open Publication Distribution System: a
set of catalogue feeds — plain XML lists
of libraries, series and books with
download links — that reader apps
outside Kavita can browse. If the web
interface is Kavita's own reading room,
OPDS is the door through which other
reading rooms visit the same shelves.
Chapter 10 walks the feed.
