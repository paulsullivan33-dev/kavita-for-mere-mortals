# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's books are short works written and drawn for the
   lab itself.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 12 names what the tool
   cannot do: no fixing, converting or unprotecting files,
   metadata only as good as the files carry, PDFs without word
   counts or chapters, folder watching that is not a delivery
   promise, one SQLite database in one config folder, and no
   sharing beyond invited accounts.
8. **The ethics rule is in the text, early.** Chapter 1 and the
   README state the household rule before any procedure depends
   on it — Kavita serves books you own and have the right to
   keep, to readers you invite, the way a physical shelf is
   shared — and the guide's lab honours it: every book on its
   shelves was written or drawn for the lab.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox,
shared with other work while the lab ran (timings are
therefore ranges, and the guide says so). Kavita **0.9.1.4**
— the latest release at build time, checked through the
project's release API — was installed from the official
`kavita-linux-x64.tar.gz` (117,675,081 bytes) and run
unmodified on loopback, port 5000. All of the lab's driving
was done through Kavita's own API, which is the traffic its
web interface itself uses; credentials in the transcripts
(admin `labadmin`, password `LabPass!234`; reader password
`ReaderPass!234`) are throwaways for a disposable instance,
and the tokens and API key in the raw captures were redacted
before the transcripts were kept. The transcripts live in
`kavita-lab/transcripts/`; the script that wrote and drew
the lab's books is `kavita-lab/make-books.py`.

The lab's library was stocked only with works made for the
lab: two short EPUBs (`The Clockwork Garden`, 3 paragraphs
in 2 chapters; `Sea of Paper Boats`, 2 paragraphs in 2
chapters) with full embedded metadata, one hand-written
one-page PDF with a title and author, a two-volume CBZ comic
(`Starlight Ferry`, 4 drawn pages per volume, no metadata),
and a one-shot CBZ (`Moon Post Office`) carrying a
`ComicInfo.xml`. A third EPUB (`Harbour Lights`) was added
later, live, for the folder-watching test (t12).

Run for real, with transcripts as evidence:

- First boot: config folder created, session key generated,
  migrations run, server self-reporting `Kavita - v0.9.1.4`
  and listening on port 5000; web root at HTTP 200 with
  `<title>Kavita</title>`; `GET /api/health` answering `Ok`
  (t00, t01).
- First registration returning the Admin role alongside
  Login; a second direct registration refused with
  `400 Not allowed`; a wrong-password login answered
  `401 Your credentials are not correct` (t02, t12).
- Library creation, including its traps: the create call's
  required fields, the metadata provider having to suit the
  library type (the books value refused for the manga
  library with `invalid-metadata-provider`), a duplicate
  name refused, and a library created against a nonexistent
  folder accepted silently and staying empty (t03, t12).
- The file groups mapped by experiment — one library per
  group, one scan each: archives admitted the CBZ files,
  group 2 the EPUBs, group 3 the PDF, group 4 a folder of
  loose page images; the first books library, created with
  the EPUB group off, logged its EPUB folders as "empty or
  has no matching file types", and switching the group on
  and rescanning produced the series (t04–t06).
- Scans building five series with the right shapes: EPUB
  chapters with word counts counted by the scanner (122 and
  78), EPUB description/author/language read into summary,
  writer and language; ComicInfo summary and writer read
  for the one-shot; the no-metadata comic's summary empty;
  `v01`/`v02` filenames becoming Volume 1 and Volume 2;
  covers extracted (the comic's served as a 320×455 PNG)
  and a KOReader hash recorded per file (t04, t07).
- Reading, byte-checked: the EPUB chapter served as HTML
  containing the lab's own first paragraph, verbatim; a
  comic page served **byte-identical** to the page inside
  the CBZ (11,028 bytes, SHA-256 prefixes equal); the PDF
  served back as the original 681-byte file (t08).
- Progress: page 1 of the EPUB's 2 recorded, the series
  answering `pagesRead 1 of 2` and the continue point
  returning that chapter (t09).
- Users: an invite issued for a second reader scoped to
  one library; with no mail server the response carried
  the confirmation link (`emailSent: false`); the account
  confirmed from the link with its own password, holding
  the ordinary reader role; signed in as that reader, only
  the granted library and its 3 series were visible, and a
  series from the other library answered 404 (t09).
- Organisers: a collection built across both libraries
  (2 items) and found again through search; a reading list
  created and filled by series, its items the two book
  chapters in order; a series put on want-to-read and read
  back as present (t09, t10).
- OPDS: enabled by default; the feed at `/api/opds/<key>/`
  returning the catalogue root (On Deck, Recently Added,
  Reading Lists, Want to Read, All Libraries, All
  Collections), the libraries feed naming both libraries,
  and the Lab Books feed listing all three books; the same
  address without `/api` returning the website instead
  (t11).
- Folder watching: with watching on, a new EPUB had not
  appeared after 20 seconds; a manual scan added it at
  once. The guide reports exactly that and recommends the
  manual scan as the dependable route (t12).
- An API quirk, recorded for script users: the
  want-to-read routes answer only in lowercase in this
  version; the CamelCase spelling returns 404 (t09).

Documented only — described from the project's
documentation, not run, and the text does not claim
otherwise:

- How the readers *look*: fonts, layout, themes, and
  reading comfort in a real browser. The lab had no
  browser; reading is verified by the bytes served, never
  by appearance.
- Email delivery of invites and password resets (no mail
  server in the lab; the link flow itself was run).
- Outside metadata matching and the external providers
  (the lab's libraries had matching switched off; every
  fact on its shelves came from its own files).
- KOReader device sync: the per-file hash Kavita stores
  was observed; no device was paired.
- Reading-list import/export files (CBL), smart filters,
  series metadata editing in the interface (the field
  locks were observed in the API's shape, not exercised),
  download of a series as a file, and deployment forms
  other than the plain binary (Docker, service units) —
  characterised, not run.
- The neighbour tools of chapter 11 (desktop readers,
  Calibre) — characterised from their documentation and
  this series' Calibre guide, not run here.

Fixtures are this guide's own and deliberately generic:
two tiny stories, a one-page paper, and two drawn comics,
all written or generated in the lab, with a single stock
author name, "Lab Author". No real book, person,
organisation or network appears anywhere in the lab.
