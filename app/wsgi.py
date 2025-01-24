def application(environ, start_response):
    import json
    serializable_environ = {
        key: str(value) if not isinstance(value, (str, int, float, list, dict, bool, type(None))) else value
        for key, value in environ.items()
    }

    environ_str = json.dumps(serializable_environ, indent=2)

    environ_bytes = environ_str.encode('utf-8')

    status = '200 OK'
    headers = [('Content-Type', 'application/json'), ('Content-Length', str(len(environ_bytes)))]
    start_response(status, headers)

    return [environ_bytes]