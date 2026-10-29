# Glossary

**API key** — Each account's personal
key, used as the credential in that
account's OPDS address. Yours is shown
in your user settings; treat it like a
password.

**Archives** — The file group covering
comic archive files — CBZ, CBR, and
plain zip/7z of page images. One of the
four groups a library can accept.

**CBZ / CBR** — A comic book file: a ZIP
(CBZ) or RAR (CBR) archive containing
page images, read in filename order.

**Chapter** — One readable unit of a
series — in practice, one file. An EPUB
is one chapter; one CBZ volume is one
chapter whose pages are its images.
Progress is kept per chapter.

**Collection** — A named set of series,
made by an admin, visible to everyone,
allowed to span libraries. A grouping,
not a permission.

**ComicInfo.xml** — An optional metadata
file placed inside a comic archive:
series, number, writer, summary and
more. The scanner reads it when present.

**Config folder** — The `config/` folder
beside the Kavita executable, holding
the database (`kavita.db`), settings,
covers and logs. The server's memory;
backing it up backs up Kavita.

**Continue point** — The server's answer
to "where was I in this series?" — the
chapter and page your account last read.

**EPUB** — The standard ebook format: a
zip of XHTML chapters plus a metadata
block (title, author, description,
language) that Kavita reads at scan
time. One of the four file groups.

**File group** — A class of files a
library accepts: archives, EPUB, PDF, or
images. A file in a group the library
has not switched on is invisible to it.

**Images** — The file group for series
kept as folders of loose page images,
unnumbered by any archive.

**Invite** — The only way accounts after
the first are created: an admin sends a
link, scoped to chosen libraries and an
optional age limit; the reader sets
their own password from it.

**KOReader hash** — A fingerprint Kavita
stores for every book file, matching the
one KOReader devices compute, so KOReader
sync can recognise the same book.

**Library** — A named collection of root
folders with a type (Book, Manga, Comic,
Image, Light Novel), a set of accepted
file groups, and a list of readers
granted access to it.

**Metadata provider** — The outside
catalogue whose conventions a library's
metadata follows, chosen per library
type. A setup choice, not a data tap
this guide opens.

**OPDS** — Open Publication Distribution
System: the XML catalogue feeds through
which reader apps browse and fetch from
a book server. Kavita's feeds live under
`/api/opds/<your API key>/`.

**PDF** — The fixed-page document
format. In Kavita, a first-class file
but a second-class book: served whole,
with no word count or chapters. One of
the four file groups.

**Reading list** — An ordered list of
chapters, for reading across series in a
set order. Order is the point; the list
holds chapters, not series.

**Role** — What an account may do. The
first account is the **admin**; invited
accounts are ordinary readers (the API
calls the default role *Pleb*).

**Scanner** — The worker that turns
library folders into catalogue: grouping
files into series, reading metadata,
counting pages, extracting covers. It
never modifies book files.

**Series** — The named, browsable thing:
a book, a comic run, a manga. Carries
the metadata, the cover, and the volumes.

**Volume** — The grouping level between
series and chapter: Volume 1, Volume 2.
Books usually have one unnamed volume;
comics and manga live by them.

**Want to read** — Your private to-read
shelf of series, kept per account.

**Word count** — For EPUB books, the
scanner's own count of the text's words,
feeding reading-time estimates. PDFs get
none.
