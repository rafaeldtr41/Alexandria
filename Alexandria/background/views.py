from django.shortcuts import render
from django.views import generic
from django.template import loader




def View_404(request):

    return render(request, 'error/404.html', {'user':request.user.is_authenticated})


def View_403(request):

    return render(request, 'error/404.html', {'user':request.user.is_authenticated})


"""
    Return a list of users that who don't confirm their emails past 1 month
    Retorna una lista de usuarios que no confirmaron su correo en un mes de creada la cuenta
    """

"""
def get_bad_users():
    
    aux = ConfirmedEmails.objects.only('user').get(confirmed=False)
    date_aux = timezone.now().date - datetime.timedelta(weeks=4)
    return User.objects.get(id__in=aux, date_joined__bt=date_aux)

"""
