# Users and Sharing

By the end of this chapter you have
invited a second reader, and you have
seen — from the reader's side of the
wall — exactly what library access
means. Sharing in Kavita is small and
deliberate: there is no public
registration, no discovery, no social
anything. There is an admin, the people
the admin invites, and the libraries
each invite carries.

## How an invite works

From **Settings → Users**, the admin
invites by email address and chooses,
at invite time:

- the **libraries** this person may see;
- an optional **age-rating limit**, with
  a choice about series whose rating is
  unknown;
- nothing else. There is one ordinary
  reader role; you are either an admin
  or a reader.

Kavita creates an **invite link**. If
you have configured an email server in
Kavita's settings, it mails the link. If
you have not — the lab had not — the
link is handed to the admin instead
(the lab's invite answered with the link
and the flags `emailSent: false`), and
you pass it to your reader by whatever
channel you already use. The reader
opens the link, sets a username and
password, and is in.

Two behaviours the lab verified about
the doors of this house:

- **Registration is closed.** After the
  first account exists, the register
  screen's API answers `400 Not allowed`.
  There is no sign-up page for strangers
  to find; the invite link is the only
  way in.
- **Wrong passwords are a dead end, on
  purpose.** A bad login answers
  `401 Your credentials are not correct`
  and nothing more useful — no hint
  about whether the username exists.

## The wall, checked from both sides

The lab's invited reader was granted
**Lab Books only**. Signed in as that
reader, the checks are:

```text
libraries  ->  [(2, 'Lab Books')]
series     ->  A Short Paper on Rain, Sea of Paper Boats, The Clockwork Garden
Starlight Ferry (a Lab Comics series)  ->  404 Not Found
```

Three things to notice. The reader sees
one library; the comics library does not
appear at all, not even as a locked
door. The three book series are fully
readable. And asking directly for a
comics series — guessing its address —
gets the same 404 as asking for
something that does not exist. Access in
Kavita is not a veil over the catalogue;
for that reader, the other library is
simply not there.

The reader also keeps entirely separate
progress: the admin had read half of
*The Clockwork Garden*; the invited
reader's copy starts at page 0, and
their reading will never move the
admin's place.

## Sharing, and the rule from chapter 1

Invites make sharing easy *inside* the
household, which is exactly the sharing
the rule in chapter 1 blesses: your
books, your people, your server on your
network. Kavita itself is neutral
plumbing — it will cheerfully serve an
invite link to anyone you send it to —
so the judgement lives with the admin,
where this guide is happy to leave it:
invite people you would hand a physical
book to, and give them the libraries you
would hand them, no more.

Practical notes for admins:

- **Removing a reader** is done from the
  same Users screen; their progress goes
  with the account.
- **Age limits** are only as good as the
  ratings in your metadata — a series
  with no rating is "unknown", and your
  include-unknowns choice at invite time
  decides which side of the line unknown
  falls on.
- Readers cannot change libraries,
  scans, or settings. Every sharp tool
  stays on the admin side of the wall.
