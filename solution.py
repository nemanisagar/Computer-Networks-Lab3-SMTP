from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Hello World"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    mailFrom = "MAIL FROM: <nemanisagar@gmail.com> \r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024)
    print(recv2)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send RCPT TO command and print server response.
    rcptTo = "RCPT TO: <sn3098@nyu.edu> \r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024)
    print(recv3)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send DATA command and print server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    print(recv4)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send message data.
    subject = "Subject: SMTP mail client testing \r\n\r\n"
    clientSocket.send(subject.encode())
    message = input("Enter your message: \r\n")
    clientSocket.send(message.encode())
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024)
    print(recv_msg.decode())
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send QUIT command and get server response.
    clientSocket.send("QUIT\r\n".encode())
    message = clientSocket.recv(1024)
    print(message)
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')