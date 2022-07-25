import os

class PCS:
    def startProxychains(self):
        os.system('sudo service tor start')
        
    def text(self):
        self.startProxychains()
        username = os.popen('id -u -n').readline().strip()
        Exit = False
        
        while not Exit:
            c = input(f'\033[1;32;40m {username}>')
            if c.lower() in ['exit', 'quit']:
                Exit = True
            os.system(f"proxychains {c}")
            
    def gui():
        ''


if __name__ == '__main__':
    PCS().text()

