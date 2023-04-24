# Swagger Detector

The Swagger Detector accepts a URL or file containing URLs as input and checks each URL for the presence of a Swagger UI. If a Swagger UI is found, it will print a message to the console indicating the URL where the Swagger UI was found. Additionally, if the -o option is specified, the results will be saved to a file.

**The scanner uses a thread pool executor to send HTTP requests in parallel to reduce the overall scan time.**

## Requirements

- Python 3.x
- httpx
- bs4
- termcolor


# Installation

```bash

git clone https://github.com/ReverseTEN/SwagDetect.git
cd SwagDetect
pip install -r requirements.txt

```

# Usage

```bash

Usage: python swagdetect.py [-u <url>] [-f <file>] [-v] [-o <output>]

Options:
  -h, --help            show this help message and exit
  -u URL, --url=URL     Url to scan.
  -f FILE, --file=FILE  File to scan.
  -v, --verbose         Show the entered URL.
  -o OUTPUT, --output=OUTPUT
                        Save the result to a file.


```

# Examples


Scan a single URL for the presence of Swagger UI:

`python swagdetect.py -u http://example.com -v -o output.txt`

Scan a list of URLs from a file for the presence of Swagger UI:

`python swagdetect.py -f urls.txt -v -o output.txt`

