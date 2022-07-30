from django.shortcuts import render
import subprocess, os

def win(request):
    if request.method == 'POST':
        try:
            if 'clear' in request.POST['command'].split():
                return render(request, 'win.html')

            if "cd" in request.POST['command'].split():
                print(request.POST['command'].split()[1])
                os.chdir(request.POST['command'].split()[1])
                return render(request, 'win.html')

            output = subprocess.check_output(['proxychains'] + request.POST['command'].split()).decode()
            return render(request, 'win.html', {'out':output})
        except:
            pass
        
    return render(request, 'win.html')


def root_privilege(request):
    if request.method == 'POST':
        try:
            if 'clear' in request.POST['command'].split():
                return render(request, 'win.html', {'root':True})

            if "cd" in request.POST['command'].split():
                print(request.POST['command'].split()[1])
                os.chdir(request.POST['command'].split()[1])
                return render(request, 'win.html', {'root':True})

            output = subprocess.check_output(['sudo', 'proxychains'] + request.POST['command'].split()).decode()
            return render(request, 'win.html', {'out':output, 'root':True})
        except:
            pass
        
    return render(request, 'win.html', {'root':True})

