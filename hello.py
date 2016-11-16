def hello_wsgi(env, start_response):
    body = '\n'.join([p for p in env['QUERY_STRING'].split('&')])
    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ]

    start_response(status, response_headers)

    return [body]
