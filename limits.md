# Limits

What Kavita will not do, stated as
plainly as the rest of the guide. Most
of these are the edges of its design
rather than defects — but an edge you
know about is a tool; an edge you
discover is a bug report.

## It serves files; it does not improve them

Kavita reads the books it is given, as
they are. It will not fix a broken EPUB,
rebuild a garbled table of contents,
convert a PDF into a book, remove DRM,
or fetch a missing cover from the
internet's imagination. Metadata can be
corrected in the interface, field by
field — but the scanner's harvest is
only ever as good as your files and
folders (chapter 5), and bulk repair is
a workbench's job (chapter 11).

## The scanner's quality is your folders' quality

Grouping is by folder, structure by
filename, facts by embedded metadata. A
collection that ignores those rules gets
the shelf it describes, not the shelf
you meant: series split by stray
folders, volumes out of order for want
of `v01` markers, summaries missing for
want of a `ComicInfo.xml`. The scanner
is fast and consistent; it is not
telepathic.

## PDFs are second-class

A PDF is served whole and read whole —
and that is all. In the lab it earned no
word count, no chapters, no reflow: it
is a document in a bookcase. Libraries
whose heart is PDFs will find Kavita a
shelf, not a reading system.

## Watching is not instant, and not a promise

Folder watching is a convenience layered
on scans. In the lab, with watching
switched on, a new book had still not
appeared after twenty seconds; the
manual scan that followed added it
immediately. Workflows that need "the
book is there *now*" should call the
scan — in the interface or the API —
and not wait on the watcher.

## One server, one database

The catalogue lives in one SQLite
database in one config folder. That is
exactly right for a household and a hard
ceiling beyond one: there is no cluster,
no read replica, no multi-server story.
Likewise the backup story is the folder
copy of chapter 11's recipe — sound, and
entirely your responsibility.

## Sharing stops where accounts stop

Everything about sharing rides on
accounts you create and libraries you
grant. There is no anonymous browsing,
no public link for "just this one book",
no federation with anyone else's server.
An OPDS address is a personal key, not a
share link (chapter 10). If your sharing
need is "send a stranger a book", Kavita
is the wrong tool — and chapter 1's rule
says that need deserves a second thought
anyway.

## Reading quality is the client's business

Kavita serves chapters as HTML and pages
as the original images — verified byte
for byte (chapters 6, 7) — but fonts,
layout, and reading comfort belong to
the browser or app doing the reading,
and the lab's headless bench could not
grade them. A reader who lives by
typography will judge Kavita by its
reader apps as much as by Kavita.

## The email is not built in

Invites, password resets, and notices
want a mail server Kavita can use. With
none configured — the common home case —
the server does not fail; it hands the
admin the link (chapter 8). But anything
that assumes working email, like a
reader resetting a forgotten password
unaided, assumes a setup step you may
not have done.
