from http.server import HTTPServer, BaseHTTPRequestHandler
from time import strftime

class RequestHandler(BaseHTTPRequestHandler):

    def serve_file(self, filename):
        f = open(filename, 'rb')
        data = f.read()
        self.wfile.write(b'HTTP/1.1 200 OK\n')
        self.wfile.write(b"Server: Client's Server\n")
        self.wfile.write(bytes(f"Date: {strftime('%c')}\n", 'utf-8'))
        self.wfile.write(bytes(f"Connection: close\n", 'utf-8'))
        self.wfile.write(bytes(f"Cache-Type: max-age=5000\n", 'utf-8'))
        self.wfile.write(bytes(f"Content-Length: {len(data)}\n", 'utf-8'))
        self.wfile.write(bytes(f"Content-Type: text/html\n\n", 'utf-8'))
        self.wfile.write(data)
        f.close()

    def serve_image(self, filename):
        f = open(filename, 'rb')
        data = f.read()
        self.wfile.write(b'HTTP/1.1 200 OK\n')
        self.wfile.write(b"Server: Client's Server\n")
        self.wfile.write(bytes(f"Date: {strftime('%c')}\n", 'utf-8'))
        self.wfile.write(bytes(f"Connection: close\n", 'utf-8'))
        self.wfile.write(bytes(f"Cache-Type: max-age=5000\n", 'utf-8'))
        self.wfile.write(bytes(f"Content-Length: {len(data)}\n", 'utf-8'))
        self.wfile.write(bytes(f"Content-Type: image/jpeg\n\n", 'utf-8'))
        self.wfile.write(data)
        f.close()

    def serve_css(self, filename):
        f = open(filename, 'rb')
        data = f.read()
        self.wfile.write(b'HTTP/1.1 200 OK\n')
        self.wfile.write(b"Server: Client's Server\n")
        self.wfile.write(bytes(f"Date: {strftime('%c')}\n", 'utf-8'))
        self.wfile.write(bytes(f"Connection: close\n", 'utf-8'))
        self.wfile.write(bytes(f"Cache-Type: max-age=5000\n", 'utf-8'))
        self.wfile.write(bytes(f"Content-Length: {len(data)}\n", 'utf-8'))
        self.wfile.write(bytes(f"Content-Type: text/css\n\n", 'utf-8'))
        self.wfile.write(data)
        f.close()

    def redirect(self, location='/index.html'):
        self.wfile.write(b'HTTP/1.1 301 Moved Permanently\n')
        self.wfile.write(b"Server: Client's Server\n")
        self.wfile.write(bytes(f"Date: {strftime('%c')}\n", 'utf-8'))
        self.wfile.write(bytes(f"Location: {location}\n", 'utf-8'))
        self.wfile.write(b"\n")

    def do_GET(self):
        print(f"GET {self.path}")
        # SERVE STATIC HTML
        if self.path == '/index.html':
            self.serve_file('index.html')

        elif self.path == '/about.html':
            self.serve_file('about.html')

        elif self.path == '/tips.html':
            self.serve_file('tips.html')

        elif self.path == '/debugging':
            resp = bytes(f"""
HTTP/1.1 200 OK
Server: Client's Server
Date: {strftime('%c')}
Connection: close
Cache-Control: max-age=5000
Content-Type: text/html

<html>
    <head>
        <link type="text/css" href="/style.css" rel="stylesheet">
        <title>Debugging</title>
    </head>
    <body>
        <h1>Debugging</h1>""", 'utf-8')
            for header, value in self.headers.items():
                resp += bytes(f"<p>{header}: {value}</p>", 'utf-8')

            resp += bytes("""<p></p>
        <a href='/'>home</a>
    </body>
</html>
""", 'utf-8')
            self.wfile.write(resp)
            for header, value in self.headers.items():
                print(f"{header}: {value}")

        elif self.path == '/teapot':
            resp = bytes(f"""
HTTP/1.1 418 I'm a teapot
Server: Client's Server
Date: {strftime('%c')}
Connection: close
Cache-Control: max-age=5000
Content-Type: text/html

<html>
    <head>
        <link type="text/css" href="/style.css" rel="stylesheet">
        <title>Teapot</title>
    </head>
    <body>
        <h1>Teapot</h1>
        <p>I'm a little teapot short and stout... yay</p>
        <a href='/'>home</a>
    </body>
</html>
""", 'utf-8')
            self.wfile.write(resp)

        elif self.path == '/forbidden':
            resp = bytes(f"""
HTTP/1.1 403 Forbidden
Server: Client's Server
Date: {strftime('%c')}
Connection: close
Cache-Control: max-age=5000
Content-Type: text/html

<html>
    <head>
        <link type="text/css" href="/style.css" rel="stylesheet">
        <title>Forbidden</title>
    </head>
    <body>
        <h1>THIS PAGE IS FORBIDDEN</h1>
        <p>TURN BACK NOW WHILE YOU STILL HAVE A CHANCE...</p>
        <a href='/'>home</a>
    </body>
</html>
""", 'utf-8')
            self.wfile.write(resp)

        # SERVE FAVICON
        elif self.path == '/favicon.ico':
            self.serve_file('favicon.ico')

        # SERVE CSS FILE
        elif self.path == '/style.css':
            self.serve_css('style.css')

        # SERVE IMAGES
        elif self.path == '/dog.jpg':
            self.serve_image('dog.jpg')

        elif self.path == '/dance.jpg':
            self.serve_image('dance.jpg')

        elif self.path == '/food.jpg':
            self.serve_image('food.jpg')

        elif self.path == '/lady.jpg':
            self.serve_image('lady.jpg')

        # REDIRECTS
        elif self.path == '/':
            self.redirect()

        elif self.path.startswith('/bio'):
            self.redirect('/about.html')

        elif self.path.startswith('/tips'):
            self.redirect('/tips.html')

        elif self.path.startswith('/help'):
            self.redirect('/tips.html')

        elif self.path.startswith('/index'):
            self.redirect()

        # 404 RESPONSE
        else:
            resp = bytes(f"""
HTTP/1.1 404 Not Found
Server: Client's Server
        Date: {strftime('%c')}

<html>
    <head>
        <link type="text/css" href="/style.css" rel="stylesheet">
        <title>Not found</title>
    </head>
    <body>
        <h1>Error 404</h1>
        <p>The file you are trying to access is missing or not available.</p>
    </body>
</html>
""", 'utf-8')
            self.wfile.write(resp)


if __name__ == '__main__':
    server_address = ('localhost', 8000)
    print(f"Serving from http://{server_address[0]}:{server_address[1]}")
    print("Press Ctrl-C to quit\n")
    HTTPServer(server_address, RequestHandler).serve_forever()