import os
import sys
import subprocess
import threading
import http.server
import socketserver
import json
import time
import psutil

def kill_process_on_port(port=8000):
    for conn in psutil.net_connections():
        if conn.laddr.port == port:
            pid = conn.pid
            if pid:
                p = psutil.Process(pid)
                print(f"Killing process {pid} ({p.name()}) on port {port}")
                p.kill()

kill_process_on_port(8000)

PORT = 8000

class ModHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(length)
        try:
            data = json.loads(post_data)
        except Exception:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Invalid JSON')
            return

        if self.path == '/launch':
            folder = data.get('folderPath')
            exe = data.get('exeName')
            if not folder or not exe:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Missing folderPath or exeName')
                return
            exe_path = os.path.join(folder, exe)
            if os.path.isfile(exe_path):
                try:
                    subprocess.Popen([exe_path], cwd=folder)
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b'Mod launched successfully.')
                except Exception as e:
                    self.send_response(500)
                    self.end_headers()
                    self.wfile.write(f'Error launching mod: {e}'.encode())
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'Executable not found.')
        elif self.path == '/open-folder':
            folder = data.get('folderPath')
            if not folder or not os.path.isdir(folder):
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Invalid or missing folderPath')
                return
            try:
                os.startfile(folder)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Folder opened successfully.')
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f'Error opening folder: {e}'.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Unknown POST endpoint.')

def run_server():
    with socketserver.TCPServer(("", PORT), ModHandler) as httpd:
        print(f"Serving on http://localhost:{PORT}")

        # Open Chrome in app mode after a short delay so server is ready
        def open_chrome_app():
            time.sleep(1)  # wait 1 sec for server ready
            chrome_path = (
                r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            )
            if not os.path.isfile(chrome_path):
                chrome_path = (
                    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                )
            if not os.path.isfile(chrome_path):
                print("Chrome not found! Please install Chrome or update the path.")
                return

            url = f"http://localhost:{PORT}"
            args = [
                chrome_path,
                "--app=" + url,
                "--window-size=1200,800",
                "--window-position=50,50"
            ]
            subprocess.Popen(args)

        threading.Thread(target=open_chrome_app, daemon=True).start()

        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
