# kontur-api
Client libraries for API provided by SKB Kontur.

## Supported products
- Kontur.Focus with `FocusClient`

## Usage example
### Prepare virtual environemnt
```bash
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install git+https://github.com/agladkov/kontur-api.git
```
### Run some python code
```python
>>> from kontur import FocusClient
>>> cl = FocusClient("_YOUR_FOCUS_API_KEY_")
>>> orgs = cl.req(inn="_YOUR_INN_")
>>> print(orgs[0])
```

## Testing
You can run some tests with API key provided for testing purpose.
```bash
$ git clone git@github.com:agladkov/kontur-api.git
$ cd kontur-api
$ python3 -m venv venv
$ export FOCUS_API_KEY="_YOUR_FOCUS_API_KEY_"
$ bash ./test.sh
```
