# The SPCX parser

This project is a Python SPCX parsing package.

## Installation

    $ pip install spcxbutcher

## A small, fake SPCX file to play with

Download `small.spcx` [here](https://github.com/morannetser/SpcxButcher/raw/master/fixtures/small.spcx).

## Coverting SPCX files to MATLAB format

You will also need [SciPy](https://www.scipy.org/) for this. The following will take an SPCX file and produce many `*.mat` files, one per SPC. E.g.:

    $ spcx_to_matlab data/example.spcx data/some_prefix

will produce `some_prefix.0.mat, some_prefix.1.mat, some_prefix.2.mat,...` in the `data` directory.

## Coverting SPCX files to JSON format

The following will take an SPCX file and write a JSON representation of it to `stdout`.

    $ spcx_to_json small.spcx
    {"spcs": [{"events": [[0, 3, 47638]], "raw": 0, "timePerBin": 164610}, {"events": [[0, 6, 42779], [0, 6, 47325]], "raw": 0, "timePerBin": 164610}, {"events": [[0, 2, 47560], [0, 9, 47947], [0, 5, 48175]], "raw": 0, "timePerBin": 164610}]}

## Converting an SPCX file to text

Try this:

    $ spcx_view small.spcx
    === SPC ===
    raw: 0
    timePerBin: 164610
    lvttl   timestamp       gap
    3       47638   0
    === SPC ===
    raw: 0
    timePerBin: 164610
    lvttl   timestamp       gap
    6       42779   0
    6       47325   0
    === SPC ===
    raw: 0
    timePerBin: 164610
    lvttl   timestamp       gap
    2       47560   0
    9       47947   0
    5       48175   0


## Using SPCX Parser from your Python program

```python
import spcxbutcher.spcxparser

parsed = spcxbutcher.spcxparser.SPCXParser( 'some_file.spcx' )
for spc in parsed:
    for event in spc:
        print( event.timestamp, event.channel )
```

## Running Unit Tests

Clone this repository. From the top directory run:

    $ ./run_tests.sh
