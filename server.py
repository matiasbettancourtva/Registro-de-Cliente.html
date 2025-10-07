import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor ejecutándose en http://localhost:{PORT}")
    print("Abriendo el dashboard en el navegador...")
    webbrowser.open(f'http://localhost:{PORT}/dashboard.html')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nCerrando servidor...")