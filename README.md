# Text to Speech (TTS) GUI for Linux / Ubuntu / Kubuntu

![image](https://github.com/user-attachments/assets/42784801-a81f-4d81-9b5c-7a98eae66c5c)


## 🎁 Installation
1. Download [tts.py](https://raw.githubusercontent.com/gnat/text-to-speech-ubuntu/refs/heads/main/tts.py) to your Desktop.
2. Install dependencies: `sudo apt install espeak python3-pyqt6`
3. Make runnable: `cd ~/Desktop; chmod +x ./tts.py`
4. Create `tts.desktop`
```ini
#!/usr/bin/env xdg-open
[Desktop Entry]
Name=Text To Speech (espeak)
Exec=/usr/bin/python3 /home/$USER/Desktop/tts.py
Icon=audio-on
Terminal=false
Type=Application
Categories=Utility;
```

Short and sweet single Python script. Built in Qt 6. Supports both Wayland and X11

<br><br>

----

# 🪦 Old Method (Deprecated)

**Below is deprecated because Wayland has no support for retrieving selected text.**

## Text to Speech (TTS) Shortcut Ubuntu

For speed reading, researching, programming, editing and writing.

Tested on Ubuntu 24.04, 22.04, 22.10, 23.04, 23.10, but should work on similar distributions such as Mint, Debian, Pop OS. `xsel` required so espeak can read from clipboard. Works with `espeak` or `espeak-ng`.

1. `sudo apt install espeak xsel -y`
2. Set your custom shortcuts. See [Gnome](#gnome) or [KDE](#kde) below.
3. With your mouse, select text you want read aloud, press your Read keys.


### Gnome

* **System Settings** ➡ **Keyboard** ➡ **Keyboard Shortcuts** ➡ **Custom Shortcuts** ➡ **+**
* **Read** `bash -c "espeak -s260 -g0 -p40 -v english-us \"$(xsel | sed -e :a -e 'N;s/\n/ /;ta')\""`
* **Stop Reading** `bash -c "killall espeak"`
* Recommended keys **SUPER + R** (Read) and **SHIFT + SUPER + R** (Stop Reading)
* With your mouse, select text you want read aloud, press your Read keys.

![screenshot](https://github.com/gnat/text-to-speech-ubuntu/blob/main/screenshot.png)


### KDE
KDE is a little different because custom shortcuts have an issue with multiple commands in the same action, but this works:

* **System Settings** ➡ **Shortcuts** ➡ **Custom Shortcuts** ➡ **Edit .. New .. Global .. Command**
* **Read** `xsel > /tmp/speak.txt | espeak -s260 -g0 -p40 -v english-us -f /tmp/speak.txt`
* **Stop Reading** `killall espeak`
* Recommended keys **SUPER + R** (Read) and **SHIFT + SUPER + R** (Stop Reading)
* With your mouse, select text you want read aloud, press your Read keys.

![Screenshot_20231024_225433](https://github.com/gnat/text-to-speech-ubuntu/assets/24665/dcd36a3d-7ad1-4de3-bb8a-98202091d18e)


### Options
* `-s260` Speed of reading (260 is faster).
* `-g0` Delay between words (0 is no delay).
* `-p40` Pitch (50 is normal).
* `-v english-us` Voice pack (en-us for `espeak-ng`).

### Sed explainer.
The sed is required to replace newlines properly. Reference: https://linux.die.net/man/1/sed

* `-e :a` Sets `a` label for looping.
* `N` Read next line into substitute buffer ... or `$!N` (`$` go to EOL, `!N` exit if no more newlines to read)
* `;s/\n/ /` Substitute newlines with space.
* `;ta` Loop to label `a`.

### Using espeak-ng instead of espeak
Some distributions come with `espeak-ng` which can be used with only minor changes.

1. **Read** `bash -c "espeak-ng -s260 -g0 -p40 -v en-us \"$(xsel | sed -e :a -e 'N;s/\n/ /;ta')\""`
2. **Stop Reading** `bash -c "killall espeak-ng"`

### Killing espeak if needed.
* `ps -ef | grep "espeak" | tr -s ' ' | cut -d ' ' -f2 | xargs kill -9`

### Why?
Because my favorite TTS reader [gespeaker](https://github.com/muflone/gespeaker) (python frontend to espeak) is unmaintained, and most other options suck or are browser only.
