from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from .tasks import send_welcome_email_task


class UserViewSet(viewsets.ViewSet):
    """
    Представление для создания пользователя сохранения
    их в базе данных и отправки email.

    Методы:
    create(self, request) -> Response — обрабатывает HTTP-запрос POST
        валидирует данные и отправляет письмо.

    Обработка ошибок:
    Если во время HTTP-запроса возникает ошибка,
    возвращается ответ 400 Bad request,
    содержащий сообщение об ошибке.
    """
    def create(self, request) -> Response:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_welcome_email_task.delay(user.email, user.username)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
