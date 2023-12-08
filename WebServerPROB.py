# Import socket module
import socket   # Changed from 'from socket import *' to optimize

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# HOSTNAME = socket.gethostname()
HOSTIP = 'localhost' # socket.gethostbyname(HOSTNAME)
PORT = 6789
QUEUESIZE = 256
RECVSIZE = 4096

serverSocket.bind((HOSTIP, PORT))
serverSocket.listen(QUEUESIZE)
print(HOSTIP)

# Server should be up and running and listening to the incoming connections
while True:
	print('Ready to serve...')
	   
    # Set up a new connection from the client
	# addr is touple of (ip, port)
	connectionSocket, addr = serverSocket.accept()
	print(f'Connection accepted from {addr[0]}:{addr[1]}')
	
	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed
	try:
		# Receives the request message from the client
		message = connectionSocket.recv(RECVSIZE)
		
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		filename = message.split()[1]

		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		f = open(filename[1:], "rb")

		# Store the entire contenet of the requested file in a temporary buffer
		outputdata = f.read() 

		# Send the HTTP response header line to the connection socket		
		connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
		# The following may or may not be required
		# Content-Type: <MIME-type>
		# Content-Length: <length>
		connectionSocket.send("\r\n".encode()) # Closes Header

		# Send the content of the requested file to the connection socket
		connectionSocket.sendall(outputdata) # Altered from multiple send() calls
		connectionSocket.send("\r\n".encode()) # Closes data
		
		# Close the client connection socket
		connectionSocket.close()

	except IOError:
		print("Exception made")
		# Send HTTP response message for file not found
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
		# The following may or may not be required
		# Content-Type: <MIME-type>
		# Content-Length: <length>
		connectionSocket.send("\r\n".encode()) # Closes Header
        
		# Send possibly required HTML Content
		connectionSocket.send("<html><head>404 Not Found</head><body>404 Not Found</body></html>".encode())
		connectionSocket.send("\r\n".encode())

		# Close the client connection socket
		connectionSocket.close()

serverSocket.close()  
