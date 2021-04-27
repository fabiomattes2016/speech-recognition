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
        frase = microfone.recognize_google(audio, language="pt-BR")

        # Retorna a frase pronunciada
        print("Você disse: " + frase)
        cria_audio(frase)

    # Caso não reconheca retorna a excessao
    except sr.UnknownValueError:
        print("Não entendi! Tente novamente!")

    return frase


ouvir_microfone()
