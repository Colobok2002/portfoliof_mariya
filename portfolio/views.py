from django.shortcuts import redirect

def admin_redirect(request):
    return redirect('/admin')