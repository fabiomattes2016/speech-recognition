import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


# Funcao responsavel por falar
def cria_audio(audio):
    tts = gTTS(audio, lang="pt-BR")

    # Salva o audio em mp3
    print("Estou aprendendo o que você disse...")
    tts.save("speech.mp3")

    playsound("speech.mp3")

def narradora(frase):
    tts = gTTS(frase, lang="pt-BR")

    # Salva o audio em mp3
    print("Processando sua escolha aguarde...")
    tts.save("she.mp3")

    playsound("she.mp3")

# Funcao para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilitando o microfone do usuario
    microfone = sr.Recognizer()

    # Usando o microfone
    with sr.Microphone() as source:
        # Chama o algoritmo de reducao de ruidos
        microfone.adjust_for_ambient_noise(source)

        # Diga algo com calma e em bom tom
        print("Diga alguma coisa")

        # Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

    try:
        # Passa a váriavel para o algoritmo reconhecedor de padroes
        frase = "Você disse: "
        frase = frase + microfone.recognize_google(audio, language="pt-BR")

        numero_um = "Você disse: número um"
        numero_dois = "Você disse: número dois"

        if frase == numero_um:
            narradora("Escolheu a opção número um")
        elif frase == numero_dois:
            narradora("Escolheu a opção número dois")

        # Retorna a frase pronunciada
        print(frase)
        cria_audio(frase)

        return frase

    # Caso não reconheca retorna a excessao
    except sr.UnknownValueError:
        print("Não entendi! Tente novamente!")
        cria_audio("Não entendi! Tente novamente!")


ouvir_microfone()
