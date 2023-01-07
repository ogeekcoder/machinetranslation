from http.server import BaseHTTPRequestHandler, HTTPServer
import Translator  as TranslatorClass 

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html; charset=utf-8')
        self.end_headers()

        translator = TranslatorClass.Translator

        if self.path == '/english_to_french':
            english_to_french = translator.english_to_french("Your AI systems on the language of your industry")
            self.wfile.write(bytes("<b> Machine Translation !</b>"
                     + "<br><br>English to french: Your AI systems on the language of your industry ---> <b>" + english_to_french + "<b>", "utf-8"))
        elif self.path == '/french_to_english':
            french_to_english = translator.french_to_english("Watson est un programme informatique d'intelligence artificielle")
            self.wfile.write(bytes("<b> Machine Translation !</b>"
                     + "<br><br>French to english: Watson est un programme informatique d'intelligence artificielle  ---> <b>" + french_to_english + "<b>", "utf-8"))


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
