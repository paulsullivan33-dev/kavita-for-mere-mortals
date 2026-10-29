# Reading Comics and PDFs

By the end of this chapter you know how
Kavita serves pictures as faithfully as
it serves text: page by page, byte for
byte — and where the PDF sits in the
family, which is a step below its
siblings.

## The image reader

Open a comic and you are in the image
reader: the pages of the volume, one
after another, with the ordinary comforts
of the form (single or double page,
direction, fit) in the interface. What
the lab could check from its bench is
what the reader is *fed* — and it is
exactly the right thing. The first page
of *Starlight Ferry* volume 1, served by
the reader's own route:

```text
GET /api/Reader/image?chapterId=2&page=0  ->  200, image/png, 11028 bytes
first page inside Starlight Ferry v01.cbz ->  11028 bytes
SHA-256 (both): 0f644e0735e87a53...
```

**Identical bytes.** Kavita did not
re-encode, shrink, or watermark the
page; it took the image out of the CBZ
and served it as found. Whatever quality
your scans have is the quality you read
— the server adds nothing and takes
nothing away. That is the strongest
claim this guide makes about reading,
and it is the one with the strongest
evidence.

## Volumes, and moving through a series

A volume is one chapter (chapter 2), so
a series reads as a chain: finishing
volume 1 offers volume 2, and progress
is kept per volume just as it is for
books. The cover you browse by is the
first page of the first volume — the
lab's was served back as a 320×455 PNG,
small enough for a shelf grid, made from
the real page.

For loose-page series — a folder of
numbered images in an Images-group
library — the same reader serves the
folder's images in order. The shape is
identical; only the container differs.

## PDFs: the plain sibling

The lab's one PDF — a single page,
*A Short Paper on Rain* — scanned in as
a series with 1 page, and its reading
route hands back the **original PDF
itself**:

```text
GET /api/Reader/pdf?chapterId=14  ->  200, application/pdf, 681 bytes
file begins: %PDF-1.4
```

The web interface renders that PDF in
its viewer; other tools get the file.
But notice what the PDF did *not* get:
a word count (0, where the EPUBs got
real counts) and chapter structure —
there is nothing inside a simple PDF for
the scanner to count or split. PDFs work
in Kavita, honestly and completely, as
whole documents. They do not get the
book machinery. If a document matters to
you as *text* — searchable, countable,
reflowable — it wants to be an EPUB
(chapter 11 names the workbench for
that conversion); as a fixed document, a
PDF is at home here.

## Bookmarks and downloads

Pages can be bookmarked in either
reader, and a chapter or series can be
downloaded from its page as the original
file — the CBZ comes back as the CBZ,
byte for byte the file in your folder,
like the EPUB in chapter 6. The readers
are a way to read your files, not a toll
booth on them.
