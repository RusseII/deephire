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


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    while True:
        print(u"> ", end=u"")
        user_message = raw_input()

        if user_message == u"exit":
            break

        request = ai.text_request()
        request.query = user_message

        response = (request.getresponse().read())
        print (response)
        response=json.loads(response)
#        response = json.loads(request.getresponse().read())

        result = response['result']
        action = result.get('action')
        actionIncomplete = result.get('actionIncomplete', False)

        print(u"< %s" % response['result']['fulfillment']['speech'])

        if action is not None:
            print("#############################")
            print(action)
            if action==u"deephire.traitquestion":
                print(u"> ", end=u"")
                traits = raw_input().split(" ")
#                traits = response['result']['resolvedQuery'].split(" ")
                for t in traits:
                    print(u"< %s" % "Please elaborate what you mean by " + t)
                    print(u"> ", end=u"")
                    traits = raw_input().split(" ")

            if action == u"send_message":
                parameters = result['parameters']

                text = parameters.get('text')
                message_type = parameters.get('message_type')
                parent = parameters.get('parent')

                print (
                    'text: %s, message_type: %s, parent: %s' %
                    (
                        text if text else "null",
                        message_type if message_type else "null",
                        parent if parent else "null"
                    )
                )

                if not actionIncomplete:
                    print(u"...Sending Message...")
                    break

if __name__ == '__main__':
    main()
