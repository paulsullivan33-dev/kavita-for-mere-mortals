# Collections, Reading Lists and Want to Read

By the end of this chapter you have
built one of each organiser on a real
shelf, and you can say which of the
three a given job wants. They rhyme —
all three group books — but they answer
different questions, and chapter 2's
definitions now get their evidence.

## Collections: the label across libraries

A **collection** is a set of *series*
with a title, made by an admin and
visible to everyone. Its distinguishing
power: it ignores library boundaries.
The lab's collection, *Lab Picks*, holds
one EPUB from Lab Books and one comic
from Lab Comics:

```text
search "Lab Picks" -> collection id 1, itemCount 2, owner labadmin
```

Reach for a collection when the grouping
is a *recommendation* — "Start here",
"Prize winners", "Katherine's shelf" (a
shelf of honour, not a permission: the
collection shows a reader only the
series their libraries already grant
them). Collections are the closest thing
Kavita has to a display table in a
bookshop: arranged by staff, browsed by
all.

## Reading lists: the order is the point

A **reading list** is an ordered list of
*chapters* — not series, chapters. The
lab built one called *Start Here* and
added two whole series to it; Kavita
laid their chapters into the list in
order:

```text
list "Start Here", itemCount 2, owner labadmin
  item 0: Sea of Paper Boats (chapter, 2 pages)
  item 1: The Clockwork Garden (chapter, 2 pages)
```

Adding by series is a shortcut; the list
itself is chapter-shaped, so a list can
also pick single chapters out of many
series — the crossover storyline that
runs through six series in a specific
order, a course of reading drawn from a
dozen books, the "read these chapters
before the meeting" list. Reading a list
walks you item to item, and your
progress across the list is the progress
of a single journey. Lists can also be
imported and exported in the standard
CBL (Comic Book List) format — a file
other tools in the comics world
understand.

## Want to read: your own shelf

**Want to read** is the private to-read
pile, kept per account. Any series can
be put on it from its menu; the lab put
*Sea of Paper Boats* there and the
server confirmed it two ways:

```text
is-want-to-read(series 9) -> true
want-to-read list         -> ['Sea of Paper Boats']
```

No admin involved, nobody else sees it,
nothing about the book changes. It is a
bookmark with ambition — and because it
is per account, the invited reader's
want-to-read and the admin's never mix.

## Which one, when

| You want… | Use |
| --- | --- |
| A staff-picks shelf everyone browses | Collection |
| These chapters, in this order, as one journey | Reading list |
| To remember a series for yourself, later | Want to read |
| To keep *other readers out* of a shelf | None of these — that is a library (chapter 8) |

That last row is the one mistake to
avoid: organisers group; libraries
*grant*. A collection containing a
series does not give anyone access to
it, and a reading list cannot smuggle a
book across the chapter 8 wall.
