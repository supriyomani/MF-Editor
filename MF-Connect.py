import socket
import ftplib
import re
from ftplib import FTP

global RAWfile
port=21
ip="10.1.111.249"
user = 'TKMAAIT'
password = 'mani0109'



def ExpandCopy(CopyName):
    try:
        s=socket.socket()
        s.connect((ip,port))
        print("port",port,"is open")
    except:
        print("port",port,"is closed")

    ftp = FTP(ip)
    ftp.login(user,password)
    ftp.retrlines('RETR \'PKMO.DP.SRCLIB(%s)\'' %CopyName,COBwrite)

def COBwrite(RAWtxt):
    global RAWfile
    RAWfile.write(RAWtxt + '\n')
    COBtxt = RAWtxt[6:72]
    ##COBfile.write(COBtxt + '\n')
    match = re.search('COPY[\s]+(\w[\S]*)\.',COBtxt)
    if match:
        print(match.group(1))
        ExpandCopy(match.group(1))

def main():
    global RAWfile
    try:
        s=socket.socket()
        s.connect((ip,port))
        print("port",port,"is open")
    except:
        print("port",port,"is closed")

    ftp = FTP(ip)
    ftp.login(user,password)
    RAWfile = open('E:\\RAWtxt.txt', 'w')
    ##COBfile = open('E:\\COBtxt.txt', 'w')
    ftp.retrlines('RETR \'PKMO.DP.SRCLIB(EPKUT116)\'',COBwrite)
    RAWfile.close()
    ##COBfile.close()

if __name__ == '__main__':
    main()
