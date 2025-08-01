<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>

<h1>Groq Chatbot using Streamlit</h1>

<p>
This is a simple AI chatbot web app built using <strong>Streamlit</strong> and powered by <strong>Groq LLMs</strong>. 
You can interact with advanced models such as <code>Mixtral</code>, <code>LLaMA3</code>, and <code>Gemma</code> through an easy-to-use interface.
</p>

<h2>Features</h2>
<ul>
    <li>Clean and responsive Streamlit interface</li>
    <li>Groq LLM support: <code>mixtral-8x7b</code>, <code>llama3-70b</code>, <code>gemma-7b</code></li>
    <li>Secure Groq API key input via sidebar</li>
    <li>Displays full chat history</li>
</ul>

<h2>Installation</h2>
<pre><code>pip install streamlit groq</code></pre>

<h2>How to Get Your Groq API Key</h2>
<ol>
    <li>Visit <a href="https://console.groq.com" target="_blank">https://console.groq.com</a></li>
    <li>Create an account or log in</li>
    <li>Generate your API key from the dashboard</li>
    <li>Paste it into the Streamlit sidebar input</li>
</ol>

<h2>How to Run the App</h2>
<pre><code>streamlit run chatbot_app.py</code></pre>

<h2>Code Functionality Overview</h2>
<ul>
    <li>User enters a prompt in the text box</li>
    <li>Groq API is called with the selected model</li>
    <li>Response from model is shown in chat format</li>
    <li>All messages are stored in session history</li>
</ul>

<h2>Project Structure</h2>
<pre><code>├── chatbot_app.py
└── README.html  ← (This file)</code></pre>

<footer>
    © 2025 Talha Zulfiqar — AI-Powered Chatbot | Built with Groq & Streamlit
</footer>

</body>
</html>
