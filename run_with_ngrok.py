from pyngrok import ngrok
import os

# Set the port Streamlit will run on
port = 8501

# Start ngrok tunnel
public_url = ngrok.connect(port)
print(" * Ngrok tunnel URL:", public_url)

# Start the Streamlit app
os.system(f"streamlit run app.py --server.port {port}")
