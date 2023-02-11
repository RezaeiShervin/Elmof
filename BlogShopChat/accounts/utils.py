from kavenegar import *


# use kavenegar ---------------------

def send_sms(receptor, token):
    try:
        api = KavenegarAPI('644B4D61645833352B725330312F786F6B6A715A346174437A4853457849785A46765764732B465A70364D3D')
        params = {
            'sender': '1000596446',      # optional
            'receptor': f'0{receptor}',  # multiple mobile number, split by comma
            'message': f'your otp code : {token}',
        } 
        response = api.sms_send(params)
        print(response, 30 * "*")
    except APIException as e: 
        print(e, 100 * "#")
    except HTTPException as e: 
        print(e, 100 * "#")
    



    
