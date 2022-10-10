import random
import lightbulb

bot = lightbulb.BotApp(token=open('tokens/token_ds.txt', 'r').read(),
                       default_enabled_guilds=(int(open('tokens/ds_channel_id.txt', 'r').read())))

# Mensagem de boas vindas


@bot.command
@lightbulb.command('msg_asmv', 'Saudação Asimov Academy')
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond('*Olá, comunidade Asimov Academy!*')

# Piada

p1 = "O que o pato disse para a pata? \nR.: Vem Quá!"
p2 = "Porque o menino estava falando ao telefone deitado? \nR.: Para não cair a ligação."
p3 = "Qual é a fórmula da água benta? \nR.: H Deus O!"
p4 = "Qual é a cidade brasileira que não tem táxi? \nR.: Uber lândia."
p5 = "Qual é a fruta que anda de trem? \nR.: O Kiwiiiii"
p6 = "O que é um pontinho preto no avião? \nR.: Uma aeromoça."
p7 = "Como o Batman faz para entrar na Bat-caverna? \nR.: Ele bat-palma."
p8 = "Por que o pão não entende a batata? \nR.: Porque o pão é francês e a batata é inglesa."
p9 = "O que o zero disse para o oito? \nR.: Belo cinto!"
p10 = "Por que os elétrons nunca são convidados para festas? \nR.: Porque eles são muito negativos."

piadas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]


@bot.command
@lightbulb.command('piada', 'Bot contador de piadas')
@lightbulb.implements(lightbulb.SlashCommand)
async def joke(ctx):
    n = random.randint(0, 9)
    await ctx.respond(f'*{piadas[n]}*')


# Cálculadora

@bot.command
@lightbulb.command('calculadora', 'Bot que calcula')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_calculator(ctx):
    pass

# ============================= Soma =====================================
@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('soma', 'Operação de soma')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def soma(ctx):
    r = ctx.options.n1 + ctx.options.n2
    await ctx.respond(f'*O resultado é **{r}***')

# ============================= Subtração =====================================
@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('subtracao', 'Operação de subtração')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def soma(ctx):
    r = ctx.options.n1 - ctx.options.n2
    await ctx.respond(f'*O resultado é **{r}***')

# ============================= Multiplicação =====================================
@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('multiplicacao', 'Operação de multiplicação')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def soma(ctx):
    r = ctx.options.n1 * ctx.options.n2
    await ctx.respond(f'*O resultado é **{r}***')

# ============================= Divisão =====================================
@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('divisao', 'Operação de divisão')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def soma(ctx):
    r = ctx.options.n1 / ctx.options.n2
    await ctx.respond(f'*O resultado é **{r}***')

# %%
# ============================= Temperatura =====================================
import requests
import string

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
API_KEY = open('tokens/api_weather_key.txt','r').read()

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def create_url(pais,cidade):
    cidadePais = string.capwords(cidade)+','+pais[0:2]
    return BASE_URL+'q='+cidadePais.lower()+'&APPID='+API_KEY

#%%
@bot.command
@lightbulb.option('pais', 'País', type=str)
@lightbulb.option('cidade', 'Cidade', type=str)
@lightbulb.command('temperatura','Informe uma cidade e seu país para saber as condições climáticas atuais')
@lightbulb.implements(lightbulb.SlashCommand)
async def temperatura(ctx):

    response = requests.get(create_url(ctx.options.pais,ctx.options.cidade)).json()

# %%
    temp_kelvin = response['main']['temp']
    umidade = response['main']['humidity']
    vento = response['wind']['speed']

    temp_celsius = str(round(kelvin_to_celsius(temp_kelvin)))

    await ctx.respond(f'```A temperatura atual em {string.capwords(ctx.options.cidade)} é de {temp_celsius} ºC\nUmidade do ar: {umidade}%\nVentos: {vento} m/s```')


# %%
bot.run()
 