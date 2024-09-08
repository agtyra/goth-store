from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'goth-store',
        'name': 'Kezia Salsalina Agtyra Sebayang',
        'class': 'PBD KKI'
    }

    return render(request, 'main.html', context)