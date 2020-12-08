import pytest
from django.urls import reverse

from ..models import Issue

users = (
    ('owner', 'owner'),
    ('manager', 'manager'),
    ('author', 'author'),
    ('guest', 'guest'),
    ('api', 'api'),
    ('user', 'user'),
    ('site', 'site'),
    ('anonymous', None),
)

status_map = {
    'list': {
        'owner': 200, 'manager': 200, 'author': 200, 'guest': 200, 'api': 200, 'user': 200, 'site': 200, 'anonymous': 401
    },
    'detail': {
        'owner': 200, 'manager': 200, 'author': 200, 'guest': 200, 'api': 200, 'user': 404, 'site': 200, 'anonymous': 401
    },
    'create': {
        'owner': 405, 'manager': 405, 'author': 405, 'guest': 405, 'api': 405, 'user': 405, 'site': 405, 'anonymous': 401
    },
    'update': {
        'owner': 405, 'manager': 405, 'author': 405, 'guest': 405, 'api': 405, 'user': 405, 'site': 405, 'anonymous': 401
    },
    'delete': {
        'owner': 405, 'manager': 405, 'author': 405, 'guest': 405, 'api': 405, 'user': 405, 'site': 405, 'anonymous': 401
    }
}

urlnames = {
    'list': 'v1-projects:issue-list',
    'detail': 'v1-projects:issue-detail'
}

site_id = 1
project_id = 1
project_count = 4

issue_status = ('open', 'in_progress', 'closed')


@pytest.mark.parametrize('username,password', users)
def test_list(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse(urlnames['list'])
    response = client.get(url)
    assert response.status_code == status_map['list'][username], response.json()

    if response.status_code == 200:
        assert isinstance(response.json(), list)
        if username == 'user':
            assert len(response.json()) == 0
        elif username in ['owner', 'site', 'api']:
            assert len(response.json()) == project_count
        else:
            assert len(response.json()) == 1


@pytest.mark.parametrize('username,password', users)
def test_detail(db, client, username, password):
    client.login(username=username, password=password)

    instances = Issue.objects.filter(project_id=project_id)
    for instance in instances:
        url = reverse(urlnames['detail'], args=[instance.pk])
        response = client.get(url)
        assert response.status_code == status_map['detail'][username], response.json()

        if response.status_code == 200:
            assert response.json().get('id') == instance.id


@pytest.mark.parametrize('username,password', users)
def test_create(db, client, username, password):
    client.login(username=username, password=password)

    url = reverse(urlnames['list'])
    response = client.post(url, {})
    assert response.status_code == status_map['create'][username], response.json()


@pytest.mark.parametrize('username,password', users)
def test_update(db, client, username, password):
    client.login(username=username, password=password)

    instances = Issue.objects.filter(project_id=project_id)
    for instance in instances:
        for status in issue_status:
            url = reverse(urlnames['detail'], args=[instance.pk])
            data = {
                'status': status
            }
            response = client.put(url, data, content_type='application/json')
            assert response.status_code == status_map['update'][username], response.json()


@pytest.mark.parametrize('username,password', users)
def test_delete(db, client, username, password):
    client.login(username=username, password=password)
    instances = Issue.objects.filter(project_id=project_id)

    for instance in instances:
        url = reverse(urlnames['detail'], args=[instance.pk])
        response = client.delete(url)
        assert response.status_code == status_map['delete'][username], response.json()
