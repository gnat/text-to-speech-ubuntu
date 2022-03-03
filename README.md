# Text to Speech (TTS) Shortcut Ubuntu 22.04

For speed reading, researching, programming, editing and writing.

1. `sudo apt install espeak-ng xsel -y`
2. **System Settings** ➡ **Keyboard** ➡ **Keyboard Shortcuts** ➡ **Custom Shortcuts** ➡ **+**
3. **Speak** `bash -c "espeak-ng -s260 -g0 -p40 -v en-us \"$(xsel | sed -e :a -e '$!N;s/\n/ /;ta')\""`
4. **Stop Speaking** `bash -c "killall espeak-ng"`

Recommended keys **SUPER + R** (Speak) and **SHIFT + SUPER + R** (Stop Speaking)

### Screenshot

![screenshot](https://github.com/gnat/text-to-speech-ubuntu/blob/main/screenshot.png)

Tested on Ubuntu 22.04 LTS and higher, but may work on other distributions. `xsel` required so espeak can read from clipboard. `espeak` will also work but most distributions are moving to `espeak-ng`.

### Options
* `-s260` Set higher for faster speed.
* `-g0` No delay.
* `-p40` Pitch (50 is normal).
* `-v en-us` Voice pack.

### Why?
Because my favorite TTS reader [gespeaker](https://github.com/muflone/gespeaker) (python frontend to espeak) is unmaintained, and most other options suck or are browser only.
