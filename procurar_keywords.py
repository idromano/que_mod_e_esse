import nltk

# palavras_chave_cities_skylines = {
#     "ferramenta": ["mod", "construir", "fazer"],
#     "solução de problemas": ["mod", "carregar", "save", "bug", "erro"],
#
# }

mensagem = "qual o nome do mod para pintar terreno"

text = nltk.Text(nltk.word_tokenize(mensagem))

match = text.concordance('mod')
