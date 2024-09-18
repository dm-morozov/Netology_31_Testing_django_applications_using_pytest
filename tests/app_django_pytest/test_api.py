import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from app_django_pytest.models import Message
from model_bakery import baker

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user('dem2014')


@pytest.fixture
def message_factory():
    def factory(*args, **kwargs):
        return baker.make(Message, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_messages(client, user, message_factory):
    # Arrange
    # client = APIClient()
    # передает пользователя в хешированном виде,
    # в таком виде пароль и остальные данные будут зашифрованы,
    # что хорошо для безопасности.
    # user = User.objects.create_user('dem2014')

    # С помощью библиотеки model_bakery мы сделали 10 сообщений автоматически
    messages = message_factory(_quantity=10)

    # Раньше нам приходилось создавать по одному сообщению вручную
    # Message.objects.create(user_id=user.id, text='Hello')

    # Act
    response = client.get('/api/messages/')


    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(messages)
    # Проверку текста пока уберем. Так как мы автоматически создали их 10 шт.
    # assert data[0]['text'] == 'Hello'

    for index, message in enumerate(data):
        assert message['text'] == messages[index].text

@pytest.mark.django_db
def test_create_massege(client, user):
    count = Message.objects.count()
    responce = client.post(
        '/api/messages/',
        data={
            'user': user.id,
            'text': "Привет Мир!",
        },
        # format='json', # указали формат глобально
    )
    assert responce.status_code == 201
    assert Message.objects.count() == count + 1
