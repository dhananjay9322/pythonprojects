const express = require('express');
const nodemailer = require('nodemailer');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Email transporter setup
const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'abcd@gmail.com',         // your email
        pass: 'pqrs abcd wxyz ffgh'                 // use App Password, not your Gmail password
    }
});

// GET route to test if server is running
app.get('/', (req, res) => {
    res.send('✅ Email backend is running. Use POST /send-email to send emails.');
});

// API endpoint to send emails
app.post('/send-email', (req, res) => {
    const { to, subject, text } = req.body;

    const mailOptions = {
        from: 'youremail@gmail.com',
        to: to || 'receiveremail@gmail.com',
        subject: subject || 'Default Subject',
        text: text || 'Hello from Node.js + Nodemailer!'
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error(error);
            return res.status(500).json({ success: false, error: error.message });
        }
        res.status(200).json({ success: true, message: 'Email sent: ' + info.response });
    });
});

// Start server
const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
    console.log(`🚀 Server running on http://localhost:${PORT}`);
});
