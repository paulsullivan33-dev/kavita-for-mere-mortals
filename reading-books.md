# Reading Books in Kavita

By the end of this chapter you have read
a book in Kavita the way the server
actually serves it — chapter by chapter,
as ordinary web pages — and you know how
your place is kept. The lab had no
browser screen to admire, so it read the
book the way the browser does: by
fetching exactly what the reader asks
for. The evidence is unusually direct.

## Opening a book

From a series page, **Read** opens the
book reader. Underneath, the reader
loads the book one piece at a time from
the server. When the lab asked Kavita
for the first piece of *The Clockwork
Garden*, this is what came back — the
chapter itself, as HTML:

```text
GET /api/Book/13/book-page?page=0  ->  200

<div class=" "><h1>Chapter 1</h1><p>The garden behind the
workshop had not been watered in nineteen years, and yet
it bloomed. Mara found the first gear on a Tuesday...</p>...
</div>
```

That is the whole trick of the book
reader: the server unpacks the EPUB and
hands the browser its chapters as web
text, and the browser dresses them up —
font, size, margins, light or dark — to
your saved preferences. The dressed-up
appearance is the part the lab could not
grade from a headless bench, and this
guide does not pretend otherwise; what
it can promise is the substance, because
the substance is what you just saw.

## What a "page" is, in a book

A book's page count in Kavita is not
printed pages. The lab's EPUB had two
chapters (two XHTML files in its spine),
so the series shows **2 pages** — one
per chapter-sized piece — and your
progress is measured against those
pieces. The reader moves you through
the text continuously; the pieces are
the server's bookkeeping, not your
reading experience.

Two numbers the scanner adds are worth
knowing:

- **Word count.** Kavita counts the
  book's words from its text — 122 for
  the lab's little book, 78 for its
  sibling — which feeds reading-time
  estimates on the series page.
- **Reading time.** Estimated from the
  word count, shown as the small "about
  N minutes" figures. Treat them as the
  scanner's arithmetic, not a promise.

## Your place is kept on the server

Progress is not a cookie. When the lab
recorded itself as having read the first
of the book's two pages, the series
answered differently from then on:

```text
The Clockwork Garden: pagesRead 1 of 2
continue-point -> chapter "The Clockwork Garden", pagesRead 1
```

The **continue point** is the server's
answer to "where was I?" — and it is
attached to your *account*, not your
browser. That is the payoff of the whole
design: close the book on the desktop,
open Kavita on a tablet, and Continue
Reading offers the same chapter, on the
same page count, because the server
kept the place. Each account keeps its
own (chapter 8's invited reader starts
every book at page 0, untouched by the
admin's progress).

Marking progress by hand — as the lab
did, through the API — is not a thing
you will do at home. In the interface,
reading is the marking: turn pages and
the server follows along.

## Downloads and the book as a file

The reader is one way out; the file is
another. A series can be **downloaded**
from its page, and what arrives is the
original file from your folder — the
EPUB as the EPUB, ready for any other
reader. Kavita is a server, not a vault:
nothing is converted or locked in on the
way in or out. Chapter 10 covers the
third way out — OPDS — for reader apps
that fetch books themselves.
