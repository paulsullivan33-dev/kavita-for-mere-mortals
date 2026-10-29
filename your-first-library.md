# Your First Library

By the end of this chapter you have an
admin account, a library pointed at a
real folder of books, and a shelf of
series that the scanner built from
those files. This is the chapter the
whole guide hangs off; everything after
it is refinement.

The lab's shelf, so the numbers below
have something to stand on:

```text
library/
  Books/
    The Clockwork Garden/The Clockwork Garden.epub
    Sea of Paper Boats/Sea of Paper Boats.epub
    A Short Paper on Rain/A Short Paper on Rain.pdf
  Comics/
    Starlight Ferry/Starlight Ferry v01.cbz
    Starlight Ferry/Starlight Ferry v02.cbz
    Moon Post Office/Moon Post Office.cbz
```

One folder per series under each library
root — the arrangement chapter 5
explains. Your own folders can be
anywhere the server can read; only the
shape matters.

## Step 1: the first account is the admin

Open the server in a browser
(`http://127.0.0.1:5000` from the server
machine, or its address from another
machine on your network). The welcome
screen asks you to register: a username,
an email address, a password.

Register, and note what just happened:
**the first account on a Kavita server
becomes its admin** — the lab's
registration came back carrying the
Admin role alongside the ordinary login
role. From this moment, registration
closes. When the lab tried to register
a second account directly, the server
answered `400 Not allowed`. Everyone
after you joins by invitation (chapter
8). Choose this password like it
matters; it is the key to the whole
household's library.

## Step 2: create the library

As the admin, go to **Settings →
Libraries → Add Library** and give it:

- a **name** — the lab used *Lab Books*
  and *Lab Comics*;
- a **type** — Book for the books folder,
  Manga for the comics folder (the type
  tells the scanner what shapes to
  expect; chapter 5);
- the **folder** — the library's root on
  disk;
- the **file groups** it should accept.
  For a books library, switch on **EPUB**
  and **PDF**. For comics, **Archives**
  (CBZ, CBR, zip) and, if you keep loose
  page images in folders, **Images**.

That last choice is the one this guide
will keep returning to. The lab's first
books library was created *without* the
EPUB group switched on, and the scanner
walked straight past two perfectly good
EPUB files and reported their folders
"empty or has no matching file types".
Nothing was broken; the library simply
had not been told that EPUB is a kind of
file it may see. Chapter 13 tells the
full story — for now: if a book does not
appear, "is its file group switched on
for this library?" is the first question
to ask.

Save, and the library **scans itself
immediately** — creating a library and
scanning it are one motion.

## Step 3: read the shelf the scanner built

Open the library. The lab's two scans
produced five series:

| Series | Library | What the scanner found |
| --- | --- | --- |
| The Clockwork Garden | Lab Books | EPUB: 2 chapters, 122 words counted |
| Sea of Paper Boats | Lab Books | EPUB: 2 chapters, 78 words counted |
| A Short Paper on Rain | Lab Books | PDF: 1 page |
| Starlight Ferry | Lab Comics | 2 volumes, 4 pages each |
| Moon Post Office | Lab Comics | 1 volume, 4 pages, summary and writer from its ComicInfo.xml |

The server log tells the same story in
its own words, and it is worth reading
once, because every future scan reports
the same way:

```text
[Kavita] [Information] Kavita.Services.Scanner.ScannerService [ScannerService] Finished library scan of 3 files and 2 series in 7869 milliseconds for Lab Comics
```

Files in, series out, and the time it
took. Your check for this chapter: open
each series and see the cover Kavita
extracted (for the comic, its first
page; for the EPUB, the cover image
inside the file), the page counts, and
— on the books — the author and summary
the files carried in with them. If a
series is missing entirely, do not
reinstall anything: go to chapter 5 for
the scanner's rules, and chapter 13 for
the checklist.

## Adding more later

New files go in the same folders, in
the same shapes (chapter 5), and reach
the shelf by a scan: ask for one from
the library's menu (**Scan Library**),
or let folder watching notice the change
— the lab had watching switched on, and
a book dropped into the folder had still
not appeared after twenty seconds, while
a manual scan added it at once. Treat
watching as a convenience that usually
saves you the click, and Scan as the
verb you can rely on.
