from django.shortcuts import redirect, render
import subprocess, os

def win(request):
    if request.method == 'POST':
        try:
            if 'clear' in request.POST['command'].split():
                return redirect("/")
                
            if "cd" in request.POST['command'].split():
                print(request.POST['command'].split()[1])
                os.chdir(request.POST['command'].split()[1])
                return redirect("/")
            output = subprocess.check_output(['proxychains'] + request.POST['command'].split()).decode()
            return render(request, 'win.html', {'out':output, 'User':os.popen('id -u -n').readline().strip()})
        except:
            pass
        
    return render(request, 'win.html', {'User':os.popen('id -u -n').readline().strip()})


def root_privilege(request):
    if request.method == 'POST':
        try:
            if 'clear' in request.POST['command'].split():
                return redirect('/root_privilege')

            if "cd" in request.POST['command'].split():
                print(request.POST['command'].split()[1])
                os.chdir(request.POST['command'].split()[1])
                return redirect('/root_privilege')
            output = subprocess.check_output(['sudo', 'proxychains'] + request.POST['command'].split()).decode()
            return render(request, 'win.html', {'out':output, 'root':True, 'User':os.popen('id -u -n').readline().strip()})
        except:
            pass
        
    return render(request, 'win.html', {'root':True, 'User':os.popen('id -u -n').readline().strip()})

