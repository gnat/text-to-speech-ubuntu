# Text to Speech (TTS) Shortcut Ubuntu 22.04

1. `sudo apt install espeak-ng xsel -y`
2. **System Settings** ➡ **Keyboard** ➡ **Keyboard Shortcuts** ➡ **Custom Shortcuts** ➡ **+**
3. **Speak** `bash -c "espeak-ng -s260 -g0 -p30 -v en-us \"$(xsel | sed -e :a -e '$!N;s/\n/ /;ta')\""`
4. **Stop Speaking** `bash -c "killall espeak-ng"`

### Screenshot

![screenshot](https://github.com/gnat/text-to-speech-ubuntu/blob/main/screenshot.png)

Tested on Ubuntu 22.04 LTS and higher, but may work on other distributions.
