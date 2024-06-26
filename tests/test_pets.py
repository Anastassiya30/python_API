import os.path

import pytest
import requests

from api import Pets

pt = Pets()


def test_post_register():
    status = pt.post_register()
    assert status == 200


def test_get_token():
    status = pt.get_token()[1]
    token = pt.get_token()[0]
    assert token
    assert status == 200


def test_user_id():
    status = pt.get_user_id()[0]
    my_id = pt.get_user_id()[1]
    assert status == 200
    assert my_id


def test_post_pet():
    status = pt.post_pet()[1]
    pet_id = pt.post_pet()[0]
    assert status == 200
    assert pet_id


def post_pet_list():
    status = pt.post_pet_list()[0]
    assert status == 200


def test_get_photo():
    status = pt.get_pet_photo()[0]
    link = pt.get_pet_photo()[1]
    assert status == 200
    assert link


def test_patch_pet():
    status = pt.patch_pet()[0]
    pet_id = pt.patch_pet()[1]
    assert status == 200
    assert pet_id


def test_put_pet_like():
    status = pt.put_pet_like()[1]
    pet_id = pt.put_pet_like()[0]
    assert status == 200
    assert pet_id


def test_delete_pet():
    status = pt.delete_pet()[1]
    pet_id = pt.delete_pet()[0]
    assert status == 200
    assert pet_id
