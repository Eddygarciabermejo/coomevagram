""" Platzigram middleware catalog """

from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """ Profile completion middleware.
    Ensure every user that is interacting with the platform have their profile picture and biography.
    """

    def __init__(self, get_response):
        """
        Middleware initialization.
        :param get_response:
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each 'request' before the view is called.
        :param request:
        :return: update_profile or feed template
        """
        if not request.user.is_anonymous and not request.user.is_staff:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                # El método reverse() trae a través del nombre la url.
                if request.path not in [reverse('users:update'), reverse('users:logout')] \
                        and not request.path.startswith('/admin/'):
                    return redirect('users:update')

        # Si el usuario ya tiene en su perfil su foto y biografía, puede seguir el flujo normal,
        # incluso visualizar los posts.
        response = self.get_response(request)

        return response
