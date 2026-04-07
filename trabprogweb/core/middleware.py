from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError
from django.contrib.auth import get_user_model

User = get_user_model()


class JWTCookieMiddleware:
    """
    Lê o access token JWT do cookie httpOnly e autentica o request.user.
    Roda após AuthenticationMiddleware e sobrescreve o usuário se o token for válido.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.COOKIES.get('access_token')
        if token:
            try:
                validated_token = AccessToken(token)
                user_id = validated_token['user_id']
                request.user = User.objects.get(id=user_id)
            except (TokenError, User.DoesNotExist):
                request.user = AnonymousUser()

        return self.get_response(request)
