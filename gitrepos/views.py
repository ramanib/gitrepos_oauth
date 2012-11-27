
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from social_auth.db.django_models import UserSocialAuth
from pygithub3 import Github
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout


def login(request):

    if request.method == 'GET':
        c = {}
        c.update(csrf(request))
        return render_to_response('login.html', c)


@login_required        
def home(request):
    user = UserSocialAuth.objects.get(user=request.user)
    
    if request.session.has_key('access_token'):
        print "Hi"
    else:
        print request.user
    return render_to_response('home.html', {})


@login_required        
def gitrepos(request):
    user = UserSocialAuth.objects.get(user=request.user)
    utoken=user.extra_data['access_token']
    gh = Github(token=utoken)
    r=gh.repos.list().all()
    number_of_user_repos = len(r)
    if request.session.has_key('access_token'):
        print "Hi"
    else:
        print request.user
    #variables = RequestContext(request, {'form': form})
        c = {'user_repos':r,'user_name':request.user,'number_of_user_repos':number_of_user_repos}
    return render_to_response('repos.html', c)


#def logout_view(request):
#   request.session.items = []
#   request.session.modified = True
#    SOCIAL_AUTH_EXPIRATION = 'expires'
#    logout(request)

  
