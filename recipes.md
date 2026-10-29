# Recipes

Short, complete jobs. Each assumes the
chapters it builds on and says which
they are; each ends with the check that
it worked.

## A household shelf (chapters 4, 8)

**Goal:** the whole family reading from
one server, each with their own place.

1. Put the family's book folders on the
   server — one root folder per library
   you intend (chapter 4's shape).
2. Make one **library** per audience
   that differs: *Books*, *Comics*,
   *Children's Books*.
3. As admin, scan them all and spot-check
   the shelves (chapter 5's rules for any
   series that lands wrong).
4. **Invite** each reader with exactly
   the libraries they should have — a
   child gets *Children's Books* and
   *Comics*, with an age limit set on the
   invite for good measure.
5. Hand each person their invite link
   and their OPDS address (chapters 8,
   10) for the app on their device.

**Check:** sign in as the most
restricted reader. You should see their
libraries, none of the others, and every
book at page 0.

## A comics folder, tamed (chapter 5)

**Goal:** a messy download folder
becomes a clean manga shelf.

1. Make a folder per **series** under
   the library root; the folder name is
   the series name, so rename folders,
   not files, to fix titles.
2. Name files with volume markers —
   `Series Name v01.cbz`, `v02`, … — so
   volumes sort themselves.
3. If a series deserves a summary and
   credits, put a **`ComicInfo.xml`**
   inside one of its archives (any text
   editor can write one; the lab's is
   four fields and did the whole job).
4. Create or rescan the library — with
   **Archives** switched on — and read
   the log's verdict: files and series
   counted.

**Check:** the series page shows the
volumes in order, page counts per
volume, and — for the ComicInfo series —
the summary you wrote, word for word.

## The read-it-later shelf (chapters 6, 9)

**Goal:** recommendations stop getting
lost.

1. When a book is recommended, find its
   series and choose **Want to Read**
   from the series menu.
2. Work the shelf from the Want to Read
   page; starting a book moves it into
   Continue Reading on its own.
3. For a themed month — "everything by
   this author before her new one" — make
   it a **reading list** instead, so the
   order is part of the plan.

**Check:** the Want to Read page shows
exactly the unwatched pile, and your
housemate's pile (their account, their
shelf) is different from yours.

## A guest reader for one library (chapter 8)

**Goal:** a visiting friend may read the
comics, and nothing else.

1. **Invite** them with *Comics* as the
   only library on the invite.
2. Pass them the invite link; they set
   their own password.
3. Give them their OPDS address if they
   read in an app — their key opens
   *Comics* only.
4. When the visit ends, remove the
   account from **Settings → Users**.

**Check:** while the account exists, its
library list has exactly one entry;
after removal, its OPDS address stops
working.

## Backing up Kavita itself (chapter 2)

**Goal:** the catalogue, covers, user
accounts and every reader's progress,
safe against the server's disk dying.

1. Stop Kavita.
2. Copy the whole **`config/`** folder
   from beside the executable — database,
   settings, covers, logs.
3. Restart Kavita.
4. Back up your **book folders** with
   whatever you already use for files —
   they are ordinary files, and Kavita
   holds no copy.

**Check:** the copy of `config/` contains
`kavita.db`. A restore is the same shape
in reverse: unpack the release, put
`config/` back beside it, start, sign
in as the admin you remember.
