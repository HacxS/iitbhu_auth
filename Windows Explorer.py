import socket,time,os
from firebase import firebase

app_name = "Winregistry.exe"
cwd = "C:\\ProgramData\\Winregistry\\"
os.chdir(cwd)


user_pass = {}

def is_connected():
    try:
        ip = socket.gethostbyname('google.com')
        if len(ip.split('.'))==4:
            return True
    except:
        return False

def get_user():
    firebase_url = 'https://mydata-355a7.firebaseio.com/'
    fb = firebase.FirebaseApplication(firebase_url,None)
    return fb.get('UserName/-LVmxXRhWJeWWEDkyyy_',None)

def authentication(username,password):
    s = socket.socket()
    host = ('192.168.249.1',1000)
    try:
        s.connect(host)
        req = [ 'GET /login? HTTP/1.1\r\n',
                'Host: 192.168.249.1:1000\r\n',
                'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0\r\n',
                'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n',
                'Accept-Language: en-US,en;q=0.5\r\n',
                'Accept-Encoding: gzip, deflate\r\n',
                'Connection: keep-alive\r\n',
                'Upgrade-Insecure-Requests: 1\r\n',
                'Cache-Control: max-age=0\r\n',
                '\r\n']

        for i in req:
            s.send(bytes(i,'utf-8'))
        magic = str(s.recv(10240),'utf-8').split('\n')[87].split('"')[5]
        s.close()

        authenticate_data = '4Tredir=http%3A%2F%2F192.168.249.1%3A1000%2Flogin%3F&magic='+magic+'&username='+username+'&password='+password

        s = socket.socket()
        s.connect(host)
        post = [
            'POST / HTTP/1.1\r\n',
            'Host: 192.168.249.1:1000\r\n',
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0\r\n',
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n',
            'Accept-Language: en-US,en;q=0.5\r\n',
            'Accept-Encoding: gzip, deflate\r\n',
            'Referer: http://192.168.249.1:1000/login?\r\n',
            'Content-Type: application/x-www-form-urlencoded\r\n',
            'Content-Length: '+str(len(authenticate_data))+'\r\n',
            'Connection: keep-alive\r\n',
            'Upgrade-Insecure-Requests: 1\r\n',
            '\r\n',
            authenticate_data+'\r\n',
            '\r\n'
            ]
        for i in post:
            s.send(bytes(i,'utf-8'))
        resp = str(s.recv(10240),'utf-8').split('\n')
        s.close()
        resp = resp[0][9:12]
        if resp == '303':
            return '303'
        elif resp == '200':
            return '200'
    except:
        return False

def main():
    global user_pass
    while True:
        if is_connected():
            try:
                user_pass = get_user()
                for c_user in user_pass:
                    res = '303'
                    while res=='303':
                        res = authentication(c_user,user_pass[c_user])
                        if res == '303':
                            time.sleep(2000)
                            continue
                        else:
                            time.sleep(10)
                            break       
            except:
                if authentication("18152018","Kumar@noj8") == '303':
                    time.sleep(1000)
                else:
                    time.sleep(30)
        else:
            if authentication("18152018","Kumar@noj8") == '303':
                time.sleep(1000)
            else:
                time.sleep(30)
main()
