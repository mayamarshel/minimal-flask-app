
My web app aims to create art and creative Jungian interpretations of dreams using basic Jungian psychology and a 1960’s art style. I went through a few hurdles while completing this project. First of which I spend way too much time on trying to figure out how to engage with virtual environments on a Windows computer. The best option ended up being using Google Colab which could support Linux commands. Then I was able to continue with further development of the interface using inline CSS with chatGPT. The biggest struggle however was in realizing that ChatGPT would not have up-to-date documentation on their own API version so I ended up writing the entire program in a version that was not supported by what would be downloaded on the server. Running the program locally I was able to force install the older version and work the program successfully but this did not carry to Render.com. I tried multiple different fixes such as including a requirements.txt file with the old version of Openai on it, attempting to install the correct version within the app.py code, and even buying an upgrade to Render.com that would allow me to update the version with a terminal. So I ended up cutting my losses and turning in the project without the web service compatibility. The force version update does however run locally which I will demonstrate. Images of the local page are in the document labeled Jungian Dream Images.

Below I have attached images of the program running locally. I wrote the prompts to generate 60’s style of psychedelic imagery. Carl Jung died in 1961, right at the beginning of the Western world’s exploration of human-centered psyche exploration. Expressionism and Dada were transforming into new forms of art that bypassed rigid realism to explore how abstraction would almost better represent certain feelings and experiences. I wanted to put these thought processes together in order to create beautiful, colorful landscapes that held personal truths within them. My prompt for the text generation portion of the model was much more extensive. I wanted to give the model more context in its way of responding and make sure that a detailed and applicable answer was given. 
Prompt generation for things like the CSS was interesting because I would have to go through a few iterations of designs before finding one I liked, changing things ever so slightly in order to find what I was looking for. I found that I was able to include instructions like “keep in mind that the user will want to see the background image” and it would give me a design that has a translucent border. I still had to manually adjust some aspects but that worked pretty well. 

There are a few possible improvements I would like to implement if given the time. Besides updating the code to work with the correct version of course I would have liked to make the text box fit with the differing amounts of text. That way I wouldn’t have had to limit the text response to only three sentences. I also would have liked to play around with condensing and creating prompts with actual literature made by Jung to provide more applicable answers. I found some of the answers to be a little vague and involve key words that initially come to mind when you think about Jungian philosophy, instead of being insightful interpretations based on an entire school of through. I’m not sure how long prompts can be without losing the intended value so playing around with that would have taught me more about that limit. I would also play around with the roles more as that is where you can have more interesting fine tuning in the cadence of the model’s response. I would not change the prompt for the image generation however, I really enjoyed the images that were created with that prompt. I also would like to learn more about google colab and github as it was difficult to figure out how to easily commit new versions to Git Hub from google colab. 

Answer/text prompt-   "You are a knowledgeable psychologist trained in the theories of Carl Jung. A user has shared a dream with you. Your task is to provide a detailed analysis of the dream from a Jungian perspective. Focus on interpreting symbolic elements such as figures, actions, and settings. Explore potential meanings related to the unconscious, archetypes, the self, and any repressed or unresolved aspects of the dreamer’s psyche. Ensure that your response is thoughtful, reflective, and centered on Jung’s core principles of individuation, the integration of opposites, and the exploration of the personal and collective unconscious."
Image Prompt- "Create the image in the style of the 60 psychedelic movement calling surreal and colorful vibes"



# minimal-flask-app
Minimal code for Flask app making calls to the OpenAI API


```
# Create virtual environment
python3 -m venv ./venv

# Activate your virtual environment
source venv/bin/activate

# Install the required packages. For example
pip3 install flask openai python-dotenv

# Rename the file .env-bup to .env. 
# Add your OPENAI_API_KEY to the .env file.

# Run the app
python3 app.py
```
