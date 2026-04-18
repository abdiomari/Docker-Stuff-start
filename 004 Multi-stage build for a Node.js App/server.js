const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('<h1>Hello from Node.js in a Multi-stage Docker Build! 🎉</h1>');
});

app.get('/health', (req, res) => res.send('OK'));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
  console.log(`Environment: ${process.env.NODE_ENV || 'development'}`);
});