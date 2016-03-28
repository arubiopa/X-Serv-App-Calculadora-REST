#!/usr/bin/python
import webapp
import socket


class calcrest(webapp.webApp):

    def parse(self, request):

        metodo = request.split()[0]
        recurso = request.split()[-1]
        return(metodo, recurso)

    def process(self, parsedRequest):
        (metodo,  cuerpo) = parsedRequest

        resultado = 0
        if (metodo == "PUT"):
            self.operacion = cuerpo
            httpCode = '200 OK'
            htmlResp = "<html><body> Operacion: " + cuerpo + "</body></html>"
            return (httpCode,htmlResp)
        elif (metodo == "GET"):
            try:
                if (len(self.operacion.split('+')) == 2):
                    resultado = (float(self.operacion.split("+")[0]) +
                                 float(self.operacion.split("+")[1]))
                elif (len(self.operacion.split('-')) == 2):
                    resultado = (float(self.operacion.split("-")[0]) -
                                 float(self.operacion.split("-")[1]))
                elif (len(self.operacion.split('*')) == 2):
                    resultado = (float(self.operacion.split("*")[0]) *
                                 float(self.operacion.split("*")[1]))
                elif (len(self.operacion.split('/')) == 2):
                    resultado = (float(self.operacion.split("/")[0]) /
                                 float(self.operacion.split("/")[1]))
                return ("200 OK",
                        "<html><body>El resultado es: " +
                        str(resultado) + "</body></html>")
            except ValueError:
                httpCode = '404 Not Found'
                htmlResp = '<html><body>Metodo no soportado</body></html>'
                return (httpCode, htmlResp)
            except AttributeError:
                httpCode = '404 Not Found'
                htmlResp = '<html><body>Error: AttributeError</body></html>'
                return (httpCode, htmlResp)

        else:
            httpCode = '404 Not Found'
            htmlResp = '<html><body>Operacion incorrecta</body></html>'
            return (httpCode, htmlResp)

if __name__ == "__main__":
    calculadoraRest = calcrest(socket.gethostname(), 1234)
