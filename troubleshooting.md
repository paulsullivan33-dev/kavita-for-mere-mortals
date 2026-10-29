# Troubleshooting

The failures this guide's lab actually
met, plus the ones its evidence explains,
in the order a new admin meets them.
Every entry: what you see, what it
means, what to do.

## The library is empty, though the folder is full

**You see:** a library with no series,
and a log line —

```text
[ScannerService] /path/to/Books/Some Book is empty or has no matching file types
```

**It means:** the library's **file
groups** do not include the group those
files belong to. The folder is full of
books Kavita has not been told it may
see. This is the lab's own first
mistake: a books library with EPUB
switched off walked past two good EPUBs
and called their folders empty.

**Do:** edit the library, switch on the
groups that match your files (EPUB and
PDF for books; Archives for CBZ/CBR),
and scan again. Chapter 5, rule 4.

## One series is missing; its neighbours are fine

**It means:** the scanner's other rules.
Work the checklist:

1. Is the file inside **its own folder**
   under the library root? (Rule 1.)
2. Is the file's group switched on for
   this library? (Rule 4.)
3. Is the file actually readable — not
   zero bytes, not DRM-protected, not an
   archive with a password?
4. What does the **log** say about that
   folder? `config/logs/` holds the daily
   log; grep it for the folder's name and
   read the scanner's own account of the
   visit.

## Volumes are out of order, or all one blob

**It means:** filename structure (rule
2). Give the files volume markers —
`Series v01.cbz`, `Series v02.cbz` — and
rescan. One file with no numbers is one
standalone chapter, by design.

## The summary or author is wrong — or missing

**It means:** the metadata came from the
file, and the file says that (rule 3).
Fix it in the file (a workbench job,
chapter 11) or correct the field on the
series page and **lock** it, so the next
scan does not re-read the file's version
over yours. A comic with no summary
usually has no `ComicInfo.xml`; adding
one and rescanning is the whole cure.

## The invite never arrived

**It means:** Kavita has no mail server
configured, most likely. Nothing is
broken: the invite link exists and was
handed to the admin (in the interface,
the invite flow offers the link when
email is not set up; the lab's API
invite answered with the link and
`emailSent: false`).

**Do:** pass the link to your reader
yourself. If you want real mail, add an
email server in Kavita's settings and
resend. A second invite to the same
address before the first is accepted is
refused — `User is already invited under
this email` — which is itself the sign
the first invite is still waiting.

## A reader says their password is wrong

The login failure is deliberately
uninformative — `401 Your credentials
are not correct` — and does not say
whether the username exists. Check the
username's spelling with the reader,
then reset the account from **Settings →
Users** (or re-invite). Do not go
hunting for a more detailed error; there
isn't one, by design.

## I can't register a second account from the login page

You are not meant to. After the first
account, registration answers `400 Not
allowed`. New readers arrive by invite
(chapter 8) — this is the server working
as designed, not a fault.

## The OPDS address shows the website instead of a feed

**It means:** the address is missing its
`/api`. `/opds/<key>/` is swallowed by
the web app; the feed lives at
`/api/opds/<key>/` (chapter 10). Fix the
address in the reader app. If the feed
itself answers 404, check the key
character by character — it is long, and
it is the whole credential.

## A new book has not appeared

Give the watcher a moment — then stop
waiting and press **Scan Library**. In
the lab the watcher had not picked up a
new EPUB after twenty seconds and the
manual scan added it at once. Also
confirm the book's folder sits under a
root folder *of that library*, and that
its file group is on (first entry).

## The library points at a folder that does not exist

Kavita accepts the library without
complaint — the lab created one against
a missing path and got a cheerful,
permanently empty library. If a library
has never shown anything, re-check the
folder path on the library's edit screen
against the disk, letter by letter.
Paths are the server's paths, on the
server's filesystem — not the paths as
your laptop sees them.

## For scripts: some API addresses are case-sensitive

A note for readers driving Kavita from
scripts, as this guide's lab did: in
0.9.1.4, most API routes ignore capital
letters and one family does not. The
want-to-read routes answer only in
lowercase — `/api/want-to-read/...` —
and return 404 in any other casing. If a
scripted call 404s against a feature the
interface uses happily, check the casing
of the address against the web client's
own spelling before doubting the
feature.
