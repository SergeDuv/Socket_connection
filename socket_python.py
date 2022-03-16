import socket

#create a socket connection
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#dial the server on port 80 
mysock.connect(('data.pr4e.org', 80))

#Data sent on the internet is sent as UTF, inside of Python script the data is in Unicode, use more compresses UTF with .encode()
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

#send the request out to the server
mysock.send(cmd)

while True:
  data = mysock.recv(512)
  if len(data) < 1:
    break
  print(data.decode(), end='')
  
mysock.close()
