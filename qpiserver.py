import client_socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip, bind_port)

def handle_client(client_socket):
    
    request = client_socket.recv(1024)

    try:
    	text_file = open("output.txt", "a") 				# append instead of w = write
    	text_file.write("Received: %s" % request)
    	text_file.close()
    except:
    	print("Error while receiving")
    
    print "[*] Received: %s" % request
    
    client_socket.send("ACK!")
    
    client_socket.close()
    

while True:
    
    client, addr = server.accept()
    
    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])
    
    client_handler = threading.Thread(target=handle_client,args=(client,))
    
    client_handler.start()