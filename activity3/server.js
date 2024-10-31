const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3000;

function serveFile(res, filePath, contentType, statusCode = 200) {
    fs.readFile(filePath, (err, data) => {
        if (err) {
            res.writeHead(500, { 'Content-Type': 'text/plain' });
            res.end('Erro interno do servidor');
        } else {
            res.writeHead(statusCode, { 'Content-Type': contentType });
            res.end(data);
        }
    });
}

const server = http.createServer((req, res) => {
    let filePath = path.join(__dirname, 'public', req.url === '/' ? 'index.html' : req.url);
    const extname = path.extname(filePath);

    let contentType = 'text/html';
    switch (extname) {
        case '.jpg':
            contentType = 'image/jpeg';
            break;
        case '.mp4':
            contentType = 'video/mp4';
            break;
        case '.css':
            contentType = 'text/css';
            break;
        case '.js':
            contentType = 'application/javascript';
            break;
    }

    fs.exists(filePath, (exists) => {
        if (exists) {
            serveFile(res, filePath, contentType);
        } else {
            res.writeHead(404, { 'Content-Type': 'text/plain' });
            res.end('404: Arquivo não encontrado');
        }
    });
});

// Rodar o comando node .\server.js e acessar http://IPDOSERVIDOR:3000
const os = require('os');
const interfaces = os.networkInterfaces();

let localIP;
for (const interfaceName in interfaces) {
    for (const iface of interfaces[interfaceName]) {
        // Checa se é um endereço IPv4 e não é interno (não é localhost)
        if (iface.family === 'IPv4' && !iface.internal) {
            localIP = iface.address;
            break;
        }
    }
    if (localIP) break;
}

server.listen(PORT, '0.0.0.0', () => {
    console.log(`Servidor rodando em http://${localIP}:${PORT}`);
});
