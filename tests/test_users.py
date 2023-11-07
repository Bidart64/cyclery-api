import pytest
from app.models.user import User
from app.resolvers.user_resolvers import create_user, get_user, get_users, update_user, delete_user

def test_create_user():
    user = create_user(username='test', email='test@test.com', password='test')
    assert isinstance(user, User)
    assert user.username == 'test'
    assert user.email == 'test@test.com'

def test_get_user():
    user = create_user(username='test', email='test@test.com', password='test')
    fetched_user = get_user(user.id)
    assert fetched_user.id == user.id

def test_get_users():
    user1 = create_user(username='test1', email='test1@test.com', password='test1')
    user2 = create_user(username='test2', email='test2@test.com', password='test2')
    users = get_users()
    assert len(users) == 2
    assert user1 in users
    assert user2 in users

def test_update_user():
    user = create_user(username='test', email='test@test.com', password='test')
    updated_user = update_user(user.id, username='updated', email='updated@test.com', password='updated')
    assert updated_user.id == user.id
    assert updated_user.username == 'updated'
    assert updated_user.email == 'updated@test.com'

def test_delete_user():
    user = create_user(username='test', email='test@test.com', password='test')
    delete_user(user.id)
    with pytest.raises(Exception):
        get_user(user.id)