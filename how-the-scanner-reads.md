# How the Scanner Reads Your Files

By the end of this chapter you can look
at a folder of files and predict what
the scanner will make of it — and, when
a book is missing or wrong, you can name
which rule produced that result. The
scanner is the part of Kavita with
opinions. It does not ask questions; it
reads arrangement and metadata and
decides. These are its rules, as the lab
verified them.

## Rule 1: the folder is the series

Under a library root, **each folder is
one series**, named after the folder.
Everything inside the folder belongs to
that series:

```text
Comics/
  Starlight Ferry/      <- the series
    Starlight Ferry v01.cbz
    Starlight Ferry v02.cbz
  Moon Post Office/     <- another series
    Moon Post Office.cbz
```

Books follow the same rule: one folder
per book, the EPUB or PDF inside it.
Loose files directly in the library root
are the exception the scanner tolerates
least happily — give everything its own
folder and the grouping is never in
doubt.

## Rule 2: filenames carry the structure

Inside a series folder, the scanner
reads filenames for the structure it
cannot see:

- **Volumes** come from volume markers:
  `Starlight Ferry v01.cbz` and
  `Starlight Ferry v02.cbz` became
  Volume 1 and Volume 2 of the series,
  each a chapter of 4 pages. The `v01`
  pattern — and chapter markers like
  `c001` or `#003` in other collections —
  is the language filenames speak.
- A file with **no numbers** in its name
  is a single, standalone chapter:
  `Moon Post Office.cbz` became a
  one-volume, one-chapter series of 4
  pages.
- For books, one file is one chapter of
  the book, whatever its name; the
  folder names the book.

Series with messy names are usually
filename problems, not Kavita problems:
the fix is on disk, then a rescan.

## Rule 3: metadata comes from inside the files

What the scanner knows *about* a book it
reads out of the book:

- **EPUB** files carry their own
  catalogue card, and Kavita reads it:
  the lab's EPUB declared its title,
  author, description and language, and
  the series appeared with all four —
  the author as a *writer*, the
  description as the summary, and a word
  count (122 words) the scanner counted
  itself from the text.
- **Comic archives** speak through an
  optional **`ComicInfo.xml`** file
  zipped inside them. The lab's *Moon
  Post Office* carried one, and its
  series shows that file's summary and
  writer — while *Starlight Ferry*,
  which had none, has no summary at all.
  Same scanner, same afternoon: the
  difference is entirely what the files
  brought with them.
- **Covers** come from the content: the
  comic's cover is its first page; the
  EPUB's cover is the cover image inside
  the file.

Fields can be corrected afterwards in
the web interface, and each field has a
**lock**: lock it, and later scans leave
your correction alone instead of
re-reading it from the file. Metadata
quality is therefore a choice you make
in your files once, or in the interface
book by book — the scanner itself
invents nothing.

## Rule 4: a library only sees its file groups

The rule that bit the lab. Every library
accepts a set of **file groups**, and a
file in any other group does not exist
as far as that library is concerned.
The groups, as the lab mapped them by
experiment (one group at a time, one
scan each):

| Group | What it admits |
| --- | --- |
| Archives | CBZ/CBR and other archive files |
| EPUB | `.epub` books |
| PDF | `.pdf` files |
| Images | folders of loose page images |

A books library wants EPUB and PDF
switched on; a comics library wants
Archives (and Images, for loose pages).
With only PDF switched on, the lab's
EPUB folders logged the scanner's
plainest sentence:

```text
[ScannerService] /library/Books/The Clockwork Garden is empty or has no matching file types
```

"Empty" meant *empty of anything this
library accepts*. If the file is on
disk, spelled right, in its own folder,
and missing from the shelf — check the
library's file groups before anything
else.

## Rule 5: the library type sets the shape

The type chosen at creation (Book,
Manga, Comic, Image, Light Novel) sets
the scanner's expectations for how a
series is built — volumes and chapters
for manga-shaped shelves, single books
for book-shaped ones — and even constrains
setup: the metadata source Kavita offers
differs per type, and the lab was flatly
refused (`invalid-metadata-provider`)
when it tried to hand the manga library
the books library's setting. Type is not
a label; it is the scanner's brief.
Choose it to match the folder's contents
and leave it alone.

## The scan itself

A scan walks, groups, reads, counts,
and writes — in that order, and the log
narrates each step. It runs when a
library is created, when you choose
**Scan Library**, and on the server's
schedule. A scan never writes to your
book files; everything it produces goes
into `config/`. When in doubt about what
the scanner thought of a folder, the log
is the honest witness — `config/logs/`
keeps the daily files, and chapter 13
shows which lines to grep.
