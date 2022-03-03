# Text to Speech (TTS) Shortcut Ubuntu 22.04

For speed reading, researching, programming, editing and writing.

1. `sudo apt install espeak-ng xsel -y`
2. **System Settings** ➡ **Keyboard** ➡ **Keyboard Shortcuts** ➡ **Custom Shortcuts** ➡ **+**
3. **Speak** `bash -c "espeak-ng -s260 -g0 -p30 -v en-us \"$(xsel | sed -e :a -e '$!N;s/\n/ /;ta')\""`
4. **Stop Speaking** `bash -c "killall espeak-ng"`

Recommended keys **SUPER + R** (Speak) and **SHIFT + SUPER + R** (Stop Speaking)

### Screenshot

![screenshot](https://github.com/gnat/text-to-speech-ubuntu/blob/main/screenshot.png)

Tested on Ubuntu 22.04 LTS and higher, but may work on other distributions. `xsel` required so espeak can read from clipboard.

### Options
* `-s260` Set higher for faster speed.
* `-g0` No delay.
* `-p30` Pitch (50 is normal).
* `-v en-us` Voice pack.
