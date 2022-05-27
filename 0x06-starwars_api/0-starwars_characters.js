#!/usr/bin/node

const request = require('request');
if (process.argv.length === 3) {
  const inArgs = process.argv.slice(2);
  const url = 'https://swapi-api.hbtn.io/api/films/' + inArgs[0];
  const opt = { json: true };

  request(url, opt, async function (error, res, body) {
    if (error) {
      console.log(error);
    } else {
      for (const char of body.characters) {
        const ret = () => {
          return new Promise((resolve, reject) => {
            request(char, opt, function (error, res, body) {
              if (error) {
                console.log(error);
              } else {
                resolve(body.name);
              }
            });
          });
        };
        console.log(await ret());
      }
    }
  });
}
