from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    res1=00
    res2=00
    if a.isdigit() and b.isdigit():
        a, b  = int(a), int(b)
        res1 = a+b
        res2 = a*b
    else: 
        res1 = "error"
        res2 = "error"
    response_body = html % {
        'res1': res1,
        'res2': res2 
    } 
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
