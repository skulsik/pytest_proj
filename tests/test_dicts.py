from utils import dicts


def test_val_list_key():
    data = {'planet': 'mars', 'girl': 'nice', 'dog': 'bad'}
    assert dicts.val(data, 'girl') == 'nice'


def test_val_list_key_default():
    data = {'planet': 'mars', 'girl': 'nice', 'dog': 'bad'}
    assert dicts.val(data, 'girl', 'dirty') == 'nice'


def test_val_key_default():
    data = {}
    assert dicts.val(data, 'dog', 'dirty') == 'dirty'


def test_val_key():
    data = {}
    assert dicts.val(data, 'planet') == 'ooops!'
