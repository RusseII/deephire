#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import sys
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            os.pardir
        )
    )

    import apiai


# demo agent acess token: e5dc21cab6df451c866bf5efacb40178

CLIENT_ACCESS_TOKEN = 'c066ae29c94d42ac87e84edfec16e046'


def chat(msg):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    user_message = msg

    request = ai.text_request()
    request.query = user_message

    response = (request.getresponse().read())
   # print (response)
    response=json.loads(response)
#        response = json.loads(request.getresponse().read())

    result = response['result']
    action = result.get('action')
    actionIncomplete = result.get('actionIncomplete', False)

    return response['result']['fulfillment']['speech']


if __name__ == '__main__':
    main()
