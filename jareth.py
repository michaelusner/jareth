from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

c = [
	"You remind me of the babe",
	"The babe with the power",
	"What power",
	"The power of voodoo",
	"Who do",
	"You do",
	"Do what",
	"Remind me of the babe",
]
chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")
