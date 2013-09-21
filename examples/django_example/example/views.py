from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect


def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return redirect('done')
    return render_to_response('home.html', {}, RequestContext(request))


@login_required
def done(request):
    """Login complete view, displays user data"""
    return render_to_response('done.html', {'user': request.user},
                              RequestContext(request))


def signup_email(request):
    return render_to_response('email_signup.html', {}, RequestContext(request))


def require_email(request):
    if request.method == 'POST':
        request.session['saved_email'] = request.POST.get('email')
        backend = request.session['partial_pipeline']['backend']
        return redirect('social:complete', backend=backend)
    return render_to_response('email.html', RequestContext(request))
