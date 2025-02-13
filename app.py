from flask import Flask, render_template, request
import openai
import http.client
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
openai_api_key = os.getenv("OPENAI_API_KEY")  # Securely load API key


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image_url = None  # Initialize the image URL variable
    if request.method == "POST":
        prompt = request.form["prompt"]
        try:
            # Generate text-based response using GPT (same as before)
            response = openai.Completion.create(
                model="gpt-3.5-turbo-instruct",  # GPT model for text response
                prompt=prompt + "You are a knowledgeable psychologist trained in the theories of Carl Jung. A user has shared a dream with you. Your task is to provide a detailed analysis of the dream from a Jungian perspective in three sentences. Focus on interpreting symbolic elements such as figures, actions, and settings. Explore potential meanings related to the unconscious, archetypes, the self, and any repressed or unresolved aspects of the dreamer’s psyche. Ensure that your response is thoughtful, reflective, and centered on Jung’s core principles of individuation, the integration of opposites, and the exploration of the personal and collective unconscious.",
                max_tokens=100
            )
            result = response.choices[0].text.strip()

            # Generate image using OpenAI's Image API (via http.client)
            conn = http.client.HTTPSConnection("api.openai.com")
            payload = json.dumps({
                "prompt": prompt + "create the image in the style of the 60 psychedelic movement calling surreal and colorful vibes",
                "n": 1,
                "size": "1024x1024"
            })
            headers = {
                'Authorization': f'Bearer {openai_api_key}',  # Use the API key securely
                'Content-Type': 'application/json'
            }

            conn.request("POST", "/v1/images/generations", payload, headers)
            res = conn.getresponse()
            data = res.read()
            image_data = json.loads(data.decode("utf-8"))

            # Get the image URL from the response
            if "data" in image_data and len(image_data["data"]) > 0:
                image_url = image_data["data"][0]["url"]

        except Exception as e:
            result = f"Error: {str(e)}"
    
    return render_template("index.html", result=result, image_url=image_url)


if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing







