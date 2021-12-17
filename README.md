# `tw-timestamp`

`tw-timestamp` is a Python 3 application which converts any date format
understood by the `dateutil` parser into the form used internally by
[TiddlyWiki](https://tiddlywiki.com/static/Date%2520Fields.html).

While TiddlyWiki can _display_ dates in many formats, I prefer to store dates
in the internal format to take advantage of filters/macros which rely on dates,
such as [`timeline`](https://tiddlywiki.com/static/timeline%2520Macro.html).

## Installation

Eventually, I will release this on [PyPI](https://pypi.org), but for now:

```sh
pip3 install git+https://github.com/cr1901/tw-timestamp.git
```

To install a development snapshot, run the following:

```sh
git clone https://github.com/cr1901/tw-timestamp.git
cd tw-timestamp
pip3 install -e .
```

## Example Usage

When `tw-timestamp` is running in a terminal, if you copy the below text onto
your clipboard:

```
Dec 16 2021 at 7:23 PM EST
```

you should see the following text when you paste:

```
20211217002300000
```

Your date is ready to be pasted into a tiddler field!
