<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Groq Chatbot with Streamlit</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f9fbfd;
            color: #222;
            line-height: 1.7;
            padding: 30px 40px;
            max-width: 900px;
            margin: auto;
        }
        h1 {
            color: #003d73;
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        h2 {
            color: #004c99;
            margin-top: 30px;
            font-size: 1.5rem;
        }
        pre {
            background-color: #eef5ff;
            padding: 15px;
            border-left: 5px solid #007acc;
            overflow-x: auto;
            font-size: 15px;
        }
        ul, ol {
            margin-left: 20px;
        }
        code {
            background: #eee;
            padding: 3px 6px;
            border-radius: 4px;
            font-family: monospace;
        }
        .highlight {
            color: #cc0066;
            font-weight: 600;
        }
        footer {
            margin-top: 50px;
            text-align: center;
            font-size: 14px;
            color: #555;
            border-top: 1px solid #ccc;
            padding-top: 15px;
        }
        a {
            color: #007acc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

<h1>Groq Chatbot using Streamlit</h1>

<p>
This is a simple AI chatbot web app built using <span class="highlight">Streamlit</span> and powered by <span class="highlight">Groq LLMs</span>. 
You can interact with advanced models such as <code>Mixtral</code>, <code>LLaMA3</code>, and <code>Gemma</code> through an easy-to-use interface.
</p>

<h2>🔧 Features</h2>
<ul>
    <li>Clean and responsive Streamlit interface</li>
    <li>Groq LLM support: <code>mixtral-8x7b</code>, <code>llama3-70b</code>, <code>gemma-7b</code></li>
    <li>Secure Groq API key input via sidebar</li>
    <li>Displays full chat history</li>
</ul>

<h2>📦 Installation</h2>
<pre><code>pip install streamlit groq</code></pre>

<h2>🔑 How to Get Your Groq API Key</h2>
<ol>
    <li>Visit <a href="https://console.groq.com" target="_blank">https://console.groq.com</a></li>
    <li>Create an account or log in</li>
    <li>Generate your API key from the dashboard</li>
    <li>Paste it into the Streamlit sidebar input</li>
</ol>

<h2>▶️ How to Run the App</h2>
<pre><code>streamlit run chatbot_app.py</code></pre>

<h2>🧠 Code Functionality Overview</h2>
<ul>
    <li>User enters a prompt in the text box</li>
    <li>Groq API is called with the selected model</li>
    <li>Response from model is shown in chat format</li>
    <li>All messages are stored in session history</li>
</ul>

<h2>📁 Project Structure</h2>
<pre><code>├── chatbot_app.py
└── README.html  ← (This file)</code></pre>

<footer>
    © 2025 Talha Zulfiqar — AI-Powered Chatbot | Built with Groq & Streamlit
</footer>

</body>
</html>
