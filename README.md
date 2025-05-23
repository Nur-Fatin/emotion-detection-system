# 🎯 Emotion Detection System

**Tech Stack:**  
🧠 Python · 🌐 Flask · 🤖 IBM Watson NLP · 🔗 HTTP POST · 📦 Requests

---

## 💡 Purpose

This system analyzes **customer feedback or reviews** to detect and classify the **emotions expressed**.  
It helps generate **data-driven insights** to improve products and services.

> ✨ Imagine: You're a product manager reading a thousand reviews — now, this tool tells you which reviews express *joy*, *anger*, *fear*, and more... instantly.

---

## 🧠 How It Works

- The system uses IBM’s **Watson NLP – Emotion Predict API**
- It sends the user’s text input to the Watson API via a `POST` request
- Returns a set of **emotion scores**:
  - `anger`
  - `disgust`
  - `fear`
  - `joy`
  - `sadness`
- It identifies and highlights the **dominant emotion**

---

## ⚙️ Dependencies

```bash
pip install requests flask
```

- requests –> to send HTTP POST requests to Watson NLP API

- flask –>  to run a local web server for interacting with the app via browser


```bash
python3 server.py
```


Open your browser and visit:
http://localhost:5000

---

✅ Example Output
Input:

"I am really happy with your service!"

Output:

'anger': 0.01, 'disgust': 0.02, 'fear': 0.03, 'joy': 0.94, 'sadness': 0.00
The dominant emotion is: joy

---

🛡️ Error Handling
If the input is blank, the system returns:

Invalid text! Please try again!

If there's a network or API issue, it shows a descriptive error message
