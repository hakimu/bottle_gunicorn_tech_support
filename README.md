### This is a Bottle app being served by Gunicorn.

This is the WSGI appliction entry point.

```python
app = bottle.default_app()
```

The command to run the app with the Python agent is:

```
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn bottle_app:app
```
