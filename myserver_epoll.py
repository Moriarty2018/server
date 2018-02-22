# coding=utf-8
import select
import socket






def main():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('',9000))
    server_socket.listen(100)
    ab = select.epoll()
    ab.register(server_socket.fileno(),select.EPOLLIN|select.EPOLLET)
    connectlist ={}
    addrlist = {}
    while True:
        alertlist = ab.poll()
        for fd,addres in alertlist:
            if fd==server_socket.fileno():
                cnn,addr = server_socket.accept()
                print addr
                connectlist[cnn.fileno()] = cnn
                addrlist[cnn.fileno()] = cnn
                ab.register(cnn.fileno(),select.EPOLLIN|select.EPOLLET)


            else:
                text = connectlist[fd].recv(1024)
                if len(text)>0:
                    print text
                else:
                    connectlist[fd].close
                    ad.unregister(fd)


if __name__ =="__main__":
    main()


