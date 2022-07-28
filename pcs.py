import subprocess,argparse, os
import dearpygui.dearpygui as dpg

class PCS:
    def startTor(self):
        os.system('sudo service tor start')
        
    def text(self):
        self.startTor()
        username = os.popen('id -u -n').readline().strip()
        Exit = False
        
        while not Exit:
            c = input(f'\033[1;32;40m {username}>')
            if c.lower() in ['exit', 'quit']:
                Exit = True
            os.system(f"proxychains {c}")
            
    def GUI(self):
        dpg.create_context()
        
        def Run():
            output = subprocess.check_output(['proxychains'] + dpg.get_value('command').split()).decode()
            print(output)
            dpg.add_text(output, parent='output')
            

        with dpg.window(label="ProxyChainsShell", width=600, height=300):
            dpg.add_input_text(label='Command', tag='command')
            dpg.add_button(label='Run', callback=Run)
            with dpg.window(label="output", width=200, height=300, tag='output', pos=(100, 100)):
                dpg.add_text('output:')
            
            
        dpg.create_viewport(title='ProxyChainsShell', width=200, height=200)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='GUI or Text')
    parser.add_argument('-m', dest='m', metavar='-m',help='GUI or Text')
    args = parser.parse_args()
    os.system('clear')
    if args.m.lower() == 'text':
        PCS().text()

    elif args.m.lower() == 'gui':
        PCS().GUI()

    else:
        print('./pcs.py -m gui or text')
