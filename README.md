# linux-bt-headset-connect

This tool should help keeping the connection to a Bluetooth headset alive.

It was developed and optimized for the use of
* Ubuntu 18.04 (running on a Lenovo T580)
* Bose SoundLink AE2

## Requirements

See ```requirements.txt``` for list of requirements. Install via

    pip3 install -U --user -r requirements.txt

## <a name="use">How to use it</a>

### Configure headset
Add the your headset *name* and the headset *MAC address* into `config.yaml`

To get the infos in Ubuntu 18.04:
 - connect your bluetooth headset in the bluetooth settings
 - in the bluetooth settigs, click on your headset to get the needed infos, or use `pactl list | grep  -i device.*bluez -B 2`

### Calling the program directly

You can call the program via

    ./bt-headset-connect.py

If you want the program to run until you manually cancel it, run

    ./bt-headset-connect.py -k True

If you want to have it available everywhere, run

    git clone https://github.com/SilverJan/linux-bt-headset-connect.git ~/dev/
    echo "PATH=$PATH:$HOME/dev/linux-bt-headset-connect/" >> ~/.bashrc

### Running the program as a daemon / on login

TBD

## Debugging

Can be one via `pacmd` or `pactl`.

TODO: Find out the difference

## Sources

The Bluetoothctl class mainly comes from https://gist.github.com/castis/0b7a162995d0b465ba9c84728e60ec01.

## TODOs

[ ] Check for sound output sink (e.g. Speakers / Headphone (in GUI)), see https://askubuntu.com/questions/71863/how-to-change-pulseaudio-sink-with-pacmd-set-default-sink-during-playback/72076#72076
