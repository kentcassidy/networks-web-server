# networks-web-server
This project was a collaboration between myself and a classmate who goes by Mynti, for our computer networking assignment.

This Python script demonstrates the creation of a basic TCP server capable of handling HTTP requests and serving files over a network.
The program is designed to process multiple requests through LAN without additional configurations, and serves any file found within the source directory.
In our example, we've provided a most simple "helloworld.html".
Our script showcases foundational concepts in network programming, server architecture, and Python scripting.

The TCP server uses Python's 'socket' module to bind a listener to localhost at port 6789.
Our server parses incoming HTTP requests, then appropriately constructs HTTP responses.
Our project includes basic error handling in the case of a faulty request, so that the program can operate continuously.
Should I decide to revisit this program, I would first implement other forms of validation including input sanitization to avoid attacks.
