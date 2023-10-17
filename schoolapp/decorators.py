from django.http import HttpResponse

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name 
            if group in allowed_roles: 
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Sorry, you are not allowed to view this page.Kindly, login using a proper account.")
        return wrapper_func
    return decorator