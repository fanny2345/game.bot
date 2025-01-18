import discord
from discord.ext import commands
import random

# Configuración básica
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} ha iniciado sesión')
    
# Juegos Lingüísticos
@bot.command()
async def ahorcado(ctx):
    print("ingreso")
    palabras = ["Cheese", "Orange", "Elephant", "Bicycle", "Bicycle", "Water","book","moon","tree"]
    palabra = random.choice(palabras)
    letras_adivinadas = [".... " for _ in palabra]
    intentos = 6
    letras_usadas = []

    await ctx.send("¡Bienvenido a Ahorcado! Adivina la palabra letra por letra.")
    await ctx.send("Palabra: " + ' '.join(letras_adivinadas))
    await ctx.send(f"Tienes {intentos} intentos.")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and len(m.content) == 1

    while intentos > 0 and ".... " in letras_adivinadas:
        try:
            msg = await bot.wait_for('message', check=check, timeout=30)
            letra = msg.content.lower()

            if letra in letras_usadas:
                await ctx.send("Ya usaste esa letra. Intenta con otra.")
            elif letra in palabra:
                letras_usadas.append(letra)
                for i, l in enumerate(palabra):
                    if l == letra:
                        letras_adivinadas[i] = letra
                await ctx.send("¡Correcto! " + ' '.join(letras_adivinadas))
            else:
                letras_usadas.append(letra)
                intentos -= 1
                await ctx.send(f"Incorrecto. Te quedan {intentos} intentos.")
        except:
            await ctx.send("Se acabó el tiempo. Escribe más rápido la próxima vez.")
            break

    if ".... " not in letras_adivinadas:
        await ctx.send(f"¡Felicidades! Adivinaste la palabra: {palabra}")
    else:
        await ctx.send(f"Perdiste. La palabra era: {palabra}")

@bot.command()
async def trivia(ctx):
    preguntas = [
        {"pregunta": "¿Cómo se dice 'manzana' en inglés?", "opciones": ["a) Apple", "b) Orange", "c) Banana"], "respuesta": "a"},
        {"pregunta": "¿Cómo se dice 'libro' en inglés?", "opciones": ["a) paper", "b) book", "c) pen"], "respuesta": "b"},
        {"pregunta": "¿Cómo se dice 'caballo' en inglés?", "opciones": ["a) cow", "b) sheep", "c) horse"], "respuesta": "c"},
        {"pregunta": "¿Cómo se dice 'montaña' en inglés?", "opciones": ["a) mountain", "b) valley", "c) lake"], "respuesta": "a"},
        {"pregunta": "¿Cómo se dice 'oso' en inglés?", "opciones": ["a) lion", "b) bear", "c) tiger"], "respuesta": "b"},
    ]
    pregunta = random.choice(preguntas)

    await ctx.send(pregunta["pregunta"])
    for opcion in pregunta["opciones"]:
        await ctx.send(opcion)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', check=check, timeout=30)
        if msg.content.lower() == pregunta["respuesta"]:
            await ctx.send("¡Correcto!")
        else:
            await ctx.send("Incorrecto.")
    except:
        await ctx.send("Se acabó el tiempo.")

bot.run("token") 