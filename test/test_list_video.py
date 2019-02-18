import onfido

onfido.configuration.api_key['Authorization'] = 'token=' + 'live_Kf7gtsfQyMaf-4dfVQJ11qWEFVrCqCMy'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'
api = onfido.DefaultApi()

test_applicant_id = '65e42db1-3132-46ba-9ece-371cf1823b16'

live_videos = api.list_live_videos(test_applicant_id)

print(live_videos)