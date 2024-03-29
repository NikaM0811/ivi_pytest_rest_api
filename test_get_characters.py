from requests.auth import HTTPBasicAuth
from pack import IviServerRequests
from pack import Characters
import requests


def test_0_reset():
    res = requests.post('http://rest.test.ivi.ru/reset', auth=HTTPBasicAuth('v.milchakova9887@gmail.com', 'hgJH768Cv23'))
    assert res.status_code == 200


def test_1_get_all_characters():
    """Тест получает всех персонажей БД, проверяет статус код
    """

    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests.IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    chars = Characters.Characters(iviReq)
    res = chars.get()
    code = res.code
    if code == 200:
        print(chars.arr)
    assert code == 200


if __name__ == "__main__":
    test_0_reset()
    test_1_get_all_characters()
