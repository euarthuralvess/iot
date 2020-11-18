# IoT 

# Praticar os conceitos do protocolo MQTT, implementando um cenário simulado de comunicação, 
mostrando como seria o uso de circuitos com sensores e atuadores. 
Esta atividade deverá ser feita em duplas. Vocês devem colocar o código de vocês em um repositório estilo GitHub e enviar o link do repositório, assim como dos canais thingspeak 
usados no trabalho. 

# Especificação do problema

Automate House S&A está divulgando seu novo produto de automação de casas e decidiu que você deverá construir um protótipo. 
Nesse protótipo iremos detectar se alguém abriu a geladeira. 
Se esse evento acontecer você deve registrar em um canal do ThingSpeak a informação “ABRIU”. 
Essa informação irá gerar um comportamento em outro local da casa, que irá tocar uma música qualquer e um tweet com a frase “Gatuno na Geladeira #novatecpar” em um perfil do Twitter que você pode criar. 

#Dessa forma você deverá implementar:

Um publicador que simula a detecção de movimento. Nesse caso, se você usar Python, gere um número inteiro aleatório, entre 0 e 1, sendo 1 significando que teve movimento.
Quando isso ocorrer, publique em um canal do thingspeak e ajuste o React e o ThingTweet para realizar o que se pede;
Um subscritor que irá observar se foi publicado no canal a informação ABRIU e em seguida tocar uma música da sua escolha. Pesquisa como tocar sons mp3 ou equivalentes em Python
