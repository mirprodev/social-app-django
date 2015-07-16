import json

from social.tests.backends.oauth import OAuth2Test


class OrbiOAuth2Test(OAuth2Test):
    backend_path = 'social.backends.orbi.OrbiOAuth2'
    user_data_url = 'https://login.orbi.kr/oauth/user/get'
    access_token_body = json.dumps({
        'access_token': 'foobar',
    })
    user_data_body = json.dumps({
        'username': 'foobar',
        'first_name': 'Foo',
        'last_name': 'Bar',
        'name': 'Foo Bar',

        'imin': '100000',
        'nick': 'foobar',
        'photo': 'http://s3.orbi.kr/data/member/wi/wizetdev_132894975780.jpeg',
        'sex': 'M',
        'birth': '1973-08-03'

    })

    def test_login(self):
        self.do_login()

    def test_partial_pipeline(self):
        self.do_partial_pipeline()
