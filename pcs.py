#! /bin/python3

import subprocess,argparse, os, multiprocessing, time
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
            
    def GUI_imgui(self):
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
        
    def GUI(self):
        
        def run_server():
            os.system('python3 core/gui/manage.py runserver')

        def run_qt():
            time.sleep(8)
            os.system('python3 core/qt')


        server = multiprocessing.Process(target=run_server)
        qt = multiprocessing.Process(target=run_qt)
        server.start()
        qt.start()
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='GUI or Text')
    parser.add_argument('-m', dest='m', metavar='-m',help='pcs.py -m gui or text')
    args = parser.parse_args()
    os.system('clear')
    if args.m.lower() == 'text':
        PCS().text()

    elif args.m.lower() == 'gui':
        PCS().GUI()

    else:
        print('pcs.py -m gui or text')
