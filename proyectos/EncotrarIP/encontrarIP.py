import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("el nombre de tu equipo es: " + hostname)
print("la IP de tu equipo es: " + ip)