var request = require('request');

/*Parsey McParseface is a language parsing tool that is fantastic at tagging
 word meanings within sentences and forming a parse tree (in Tree or Conll format)
 for other NLP algorithms to use.
*/

function main(params) {

    var options = {
        url: 'https://api.algorithmia.com/v1/algo/nlp/ProfanityDetection/1.0.0',
        headers:
            {
                'content-type': 'application/json',
                authorization: params.properties.apiKey
            },
        body: params.payload.input,
        json: true };

    return new Promise(function(resolve, reject) {
        request.post(options, function (error, response, body) {
            if (error) {
                reject({payload:{error}});
            }
            else {
                var response = body;
                resolve({payload:{response}});

            }


        });
    });

}