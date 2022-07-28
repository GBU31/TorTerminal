from django.shortcuts import render
import subprocess

def win(request):
    if request.method == 'POST':
        try:
            output = subprocess.check_output(['proxychains'] + request.POST['command'].split()).decode()
            return render(request, 'win.html', {'out':output})
        except:
            pass
        
    return render(request, 'win.html')
