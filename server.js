const express = require('express');
const multer = require('multer');
const upload = multer({dest: __dirname + '/image_cache'});

const app = express();
const PORT = 3000;

app.use(express.static('public'));

app.post('/upload', upload.single('photo'), (req, res) => {
    if(req.file) {
        res.req.file;
    }
    else throw 'error';
});

app.listen(PORT, () => {
    console.log('Listening at ' + PORT );
});
