const http = require("http");
const fs = require("fs");

http
  .createServer((request, response) => {
    fs.readFile("index.html", (err, data) => {
      if (err) {
        response.writeHead(500, { "Content-Type": "text/plain" });
        response.end("500 Internal Server Error");
      } else {
        response.writeHead(200, { "Content-Type": "text/html" });
        response.end(data);
      }
    });
  })
  .listen(3000);
