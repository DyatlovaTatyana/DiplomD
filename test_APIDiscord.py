import pytest
import requests


@pytest.mark.usefixtures ("message_id")
# Получить созданное сообщение
def test_get_message(base_url, channel_id, headers, message_id):
    url = f"{base_url}/channels/{channel_id}/messages/{message_id}"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json().get('id') == str(message_id)
    # print("Созданное сообщение: " + response.json()['content'])

# Получить список сообщений
def test_get_messages_list(base_url, channel_id, headers, message_id):
    url = f"{base_url}/channels/{channel_id}/messages"
    params = {
        "limit": 5
    }
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    messages_list = response.json()
    assert isinstance(messages_list, list)
    assert len(messages_list) != 0


# Создание сообщения с вложением
def test_message_with_file(base_url, channel_id, headers):
    url = f"{base_url}/channels/{channel_id}/messages"
    files = {
        'files[0]': ('test_image.png', open('test_image.png', 'rb'))
    }

    data = {
        'content': "Авада Кедавра!!"
    }

    # Убираем Content-Type
    headers.pop('Content-Type', None)
    response = requests.post(url, headers=headers, files=files, data=data)
    assert response.status_code == 200
    message_id = response.json().get('id')
    assert message_id != 0
    assert 'attachments' in response.json()


# Создание сообщения с упоминанием
def test_mention (base_url, channel_id, headers):
    url = f"{base_url}/channels/{channel_id}/messages"
    mention_user_id = "1184210129537732679"
    data = {
        "content": f"Добрый вечер, <@{mention_user_id}>"
    }
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json()["mentions"][0]["id"] == mention_user_id

#Поставить реакцию на сообщение и потом удалить ее
def test_reaction(base_url, channel_id, headers, message_id):
    emoji = "🔥"
    emoji_encoded = requests.utils.quote(emoji)
    url = f"{base_url}/channels/{channel_id}/messages/{message_id}/reactions/{emoji_encoded}/@me"
    add_reaction = requests.put(url, headers=headers)
    assert add_reaction.status_code == 204

    remove_reaction_url = f"{base_url}/channels/{channel_id}/messages/{message_id}/reactions/{emoji_encoded}/@me"
    delete_reaction = requests.delete(remove_reaction_url, headers=headers)
    assert delete_reaction.status_code == 204


#Негативные проверки
def test_empty_content_message(base_url, channel_id, headers):
    url = f"{base_url}/channels/{channel_id}/messages"
    data = {
        "content": "       "
    }
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 400
    assert response.json()["message"] == "Cannot send an empty message"

def test_non_exist_id_message(base_url, channel_id, headers):
    invalid_message_id = "89"
    url = f"{base_url}/channels/{channel_id}/messages/{invalid_message_id}"
    response = requests.get(url, headers=headers)
    assert response.status_code == 404
    assert response.json()["message"] == "Unknown Message"

def test_add_reaction_to_non_exist_message(base_url, channel_id, headers):
    invalid_message_id = "89"
    emoji = "🔥"
    emoji_encoded = requests.utils.quote(emoji)
    url = f"{base_url}/channels/{channel_id}/messages/{invalid_message_id}/reactions/{emoji_encoded}/@me"
    response = requests.put(url, headers=headers)
    assert response.status_code == 404
    assert response.json()["message"] == "Unknown Message"