import logging, requests, yaml

with open('testdata.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

S = requests.Session()


def test_post_create(user_login):
    res = S.post(url=data['address_post'], headers={'X-Auth-Token': user_login},
                 data={'title': data['title'], 'description': data['description'], 'content': data['content']})
    logging.debug(f'Response is {str(res)}')
    assert str(res) == '<Response [200]>', 'test_post_create FAIL'


def test_check_post_create(user_login):
    result = S.get(url=data['api_address'], headers={'X-Auth-Token': user_login}).json()['data']
    logging.debug(f'get request return: {result}')
    list_description = [i['description'] for i in result]
    assert data['description'] in list_description, 'test_check_post_create FAIL'


def test_check_not_my_post(user_login):
    result = S.get(url=data['api_address'], headers={'X-Auth-Token': user_login}, params={'owner': 'notMe'}).json()[
        'data']
    logging.debug(f'get request return: {result}')
    result_title = [i['title'] for i in result]
    assert data['not_my_title'] in result_title, 'test_check_not_my_post FAIL'
