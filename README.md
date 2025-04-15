# Whois CLI Utility

## Overview

Whois is a command-line utility for querying domain availability.

## Installation

Clone the repository:

```sh
git clone https://github.com/sfmohassel/whois.git
cd whois

# install dependencies
python3 -m venv .venv
.venv/bin/activate
pip install -r requirements.txt
```

## How to run

All the commands explained:

```sh
# ensure venv is activated
.venv/bin/activate

# See list of commands
python3 main.py --help

# See options for whois command
python3 main.py whois --help

# Example usage:
python3 main.py whois --extensions 'com,ai,tech,studio' --domains 'cool-domain, good-domain'

# Example output:
+--------------------+-----------+-------+
|       Domain       | Available | Error |
+--------------------+-----------+-------+
|   cool-domain.ai   |    True   |  None |
| cool-domain.studio |    True   |  None |
|   good-domain.ai   |    True   |  None |
|  good-domain.tech  |    True   |  None |
| good-domain.studio |    True   |  None |
+--------------------+-----------+-------+
```

## License

This project is licensed under the Apache-2.0 License.

## Contributions

Feel free to submit issues or pull requests.
