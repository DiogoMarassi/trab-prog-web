from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

class JWTCookieMiddleware:
    """
    Este script permite que o Django leia os tokens JWT que salvamos nos Cookies sem JavaScript, 
    permitindo que decoradores como @login_required funcionem nativamente!
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Puxamos o cookie de nome 'access_token' setado na LoginView
        token = request.COOKIES.get('access_token')
        
        if token:
            try:
                # Instanciamos a biblioteca de JWT e validamos
                jwt_authenticator = JWTAuthentication()
                validated_token = jwt_authenticator.get_validated_token(token)
                
                # Puxamos a identidade real do usuario a partir do token
                user = jwt_authenticator.get_user(validated_token)
                
                # Sobrescrevemos o usuário falso "Anonimo" da requisição atrelando o User Mestre
                request.user = user
                
            except (InvalidToken, TokenError):
                # Se o Token expirou ou foi fraudado, engole o erro e o usuário segue Anônimo,
                # e o decorador de LoginRequired do Django fará seu trabalho de chutar pra tela de logar.
                pass
                
        response = self.get_response(request)
        return response
