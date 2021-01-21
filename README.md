# SciBowlReader

An automated moderator for Science Bowl that reads questions from [US DOE's High School Sample Questions](https://science.osti.gov/wdts/nsb/Regional-Competitions/Resources/HS-Sample-Questions) and validates answers. This allows players to either practice alone, or as a team without having a designated player for reading.

## Installation

1. Make sure you have installed [Python 3.x](https://www.python.org/).
2. Clone or download this repository.
3. Navigate to the directory:
```sh
$ cd SciBowlReader
```
4. Install requirements:
```sh
$ pip install -r requirements.txt
```

## Usage
```sh
$ python play.py
```

Find a packet from [this list of sample questions](https://science.osti.gov/wdts/nsb/Regional-Competitions/Resources/HS-Sample-Questions) and paste it in to the terminal.

## Known Issues

Doesn't work yet for the packets that have a green bar at the top of the first page.