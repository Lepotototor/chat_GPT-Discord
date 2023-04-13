import openai

class GPT:
    def __init__(self, key):
        # Définir votre clé API
        openai.api_key = key

    def reponse_a_question(self, question):
        # Définir le modèle à utiliser
        model_engine = "text-davinci-002"
        #model_engine = "davinci"

        # Définir la phrase de départ pour générer du texte
        prompt = question

        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=250,
            n=1,
            stop=None,
            temperature=0.5,
            presence_penalty = 1
        )

        #print(completions)
        return completions.choices[0].text

        # Afficher la réponse
        print(response.choices[0].text)




test = GPT("OPENAI_API_KEY")

"""
question = "Qui est tu ?"

while question != "exit":
    print(test.reponse_a_question(question))
    question = input("Quelle est votre question ? ")
"""
