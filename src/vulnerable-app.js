const fs = require('fs');
const express = require('express');
const app = express();

// 1. 任意のコード実行の脆弱性 (Arbitrary Code Execution)
app.get('/execute', (req, res) => {
    const userInput = req.query.code; // ユーザー入力
    eval(userInput); // この行が脆弱です
    res.send('Code executed!');
});

// 2. パストラバーサルの脆弱性 (Path Traversal)
app.get('/readfile', (req, res) => {
    const filePath = req.query.file; // ユーザー入力されたファイルパス
    const data = fs.readFileSync(filePath, 'utf8'); // この行が脆弱です
    res.send(data);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
