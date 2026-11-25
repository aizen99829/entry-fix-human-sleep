[![make.fun · u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/aizen99829/entry-fix-human-sleep/rank.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/aizen99829/entry-fix-human-sleep/reward.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

# Fix Human Sleep: Funniest Patch Note

An entry for the make.fun bounty "Fix Human Sleep: Funniest Patch Note":
one patch-note line, at most 160 characters, on the theme "human sleep
is fixed" — funny, but still reading like a genuine changelog.

## The entry is

> Fixed: human sleep no longer crashes at 3 AM. REM buffer overflow patched; dreams now garbage-collected nightly. Waking up rested still under investigation.

One line, 156 characters. It opens with "Fixed:" the way a real
release note opens, then files three sleep complaints as software bugs:
the 3 AM wake-up as a crash, REM as a buffer that overflows, and
dreams as memory that finally gets garbage-collected every night.

## Why the line works

The punchline hides inside the format instead of breaking it. The last
clause — "Waking up rested still under investigation" — treats feeling
rested as an open issue, which is exactly how a maintainer would log a
bug they cannot reproduce. Anyone who has ever woken up at 3 AM for no
reason recognises the crash; anyone who has read a changelog recognises
the voice. Nothing in the line explains the joke, so it lands as a
changelog first and a joke second.

## How it runs

`python3 main.py` validates the note (one line, at most 160 characters),
prints it, and writes it to `/output/entry.txt`.

## License

SPDX-License-Identifier: MIT
