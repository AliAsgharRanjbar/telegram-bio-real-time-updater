# telegram-bio-real-time-updater

telegram-bio-real-time-updater is a simple Python script to change telegram bio and name every minute by putting the current time in it.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
pip install -r requirements.txt
```
### Note
There's a *uvloop* package in requirements.txt file which does **NOT** support Windows.
If you'd like to run this script on Windows, make sure to comment lines including `uvloop.install()` and also make sure to remove the package name from requirements.txt file otherwise the installation of other packages will be ignored too.

## Usage

```python
# first of all make sure to add your own api_id and api_hash to the script. (and other personalizations)
python ./main.py

# or python3 ./main.py

# after running the script for the first time you need to provide your telegram phonenumber in order to get connected to your account.
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
