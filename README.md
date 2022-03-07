# Text to Speech (TTS) Shortcut Ubuntu 22.04

For speed reading, researching, programming, editing and writing.

1. `sudo apt install espeak-ng xsel -y`
2. **System Settings** ➡ **Keyboard** ➡ **Keyboard Shortcuts** ➡ **Custom Shortcuts** ➡ **+**
3. **Speak** `bash -c "espeak-ng -s260 -g0 -p40 -v en-us \"$(xsel | sed -e :a -e 'N;s/\n/ /;ta')\""`
4. **Stop Speaking** `bash -c "killall espeak-ng"`

Recommended keys **SUPER + R** (Speak) and **SHIFT + SUPER + R** (Stop Speaking)

With your mouse, select text you want read aloud, press your Speak key.

### Screenshot

![screenshot](https://github.com/gnat/text-to-speech-ubuntu/blob/main/screenshot.png)

Tested on Ubuntu 22.04 LTS and higher, but should work on similar distributions such as Mint, Debian, Pop OS. `xsel` required so espeak can read from clipboard. `espeak` will also work but most distributions are moving to `espeak-ng`.

### Options
* `-s260` Set higher for faster speed.
* `-g0` No delay.
* `-p40` Pitch (50 is normal).
* `-v en-us` Voice pack.

### Sed explainer.
The sed is required to replace newlines properly. Reference: https://linux.die.net/man/1/sed

* `-e :a` Sets `a` label for looping.
* `N` Read next line into substitute buffer ... or `$!N` (`$` go to EOL, `!N` exit if no more newlines to read)
* `;s/\n/ /` Substitute newlines with space.
* `;ta` Loop to label `a`.

### Why?
Because my favorite TTS reader [gespeaker](https://github.com/muflone/gespeaker) (python frontend to espeak) is unmaintained, and most other options suck or are browser only.
