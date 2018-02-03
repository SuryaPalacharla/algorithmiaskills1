import requests
import json


def main(data):

    try:
        url = "https://api.algorithmia.com/v1/algo/zza/EnhanceResolution/0.1.0"

        payload = "{\r\n  \"source\": \"" + data['payload']['source'] + "\"," +\
            "\r\n  \"dest\": \"" + data['payload']['dest'] + "\"," +\
            "\r\n  \"model\": \"" + data['payload']['model'] + "\"\r\n}"

        print payload
        headers = {
            'content-type': "application/json",
            'authorization': data['properties']['apiKey']
        }
        response = requests.post(url, data=payload, headers=headers)

        return {"payload": response.json()[u'result']}
    except Exception as e:
        raise
        return {"payload": {"text": "Error!", "message": "{}".format(e)}}


if __name__ == "__main__":
    with open('parameters.json') as json_data:
        data = json.load(json_data)
        main(data)
