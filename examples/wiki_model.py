"""
For this example, we create a model using the text found on a wikipedia page
containing a list of Pokemon characters, so we can recognize Pokemon
characters.
"""

import assemblyai
import wikipedia

aai = assemblyai.Client()

# phrases is a list or words or sentences
phrases = wikipedia.page("List of Pokemon characters").content.split('. ')

model = aai.train(phrases)
