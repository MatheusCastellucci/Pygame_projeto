dicionario = {
    'PONTUAÇÃO':0,
    'VIDAS':3,
    'BACK_WIDTH' : 700,
    'BACK_HEIGHT' : 700,
    'PROFESSOR_WIDTH' : 60,
    'PROFESSOR_HEIGHT' : 50,
    'INSPER_WIDTH' : 80,
    'INSPER_HEIGHT' : 68,
    'NAVE_WIDTH' : 60,
    'NAVE_HEIGHT' : 50,
    'TIRO_WIDTH' : 10,
    'TIRO_HEIGHT' : 20
}

elementos = [
    ['Guzzo', 'jpg', 'PROFESSOR'],
    ['Humberto', 'png', 'PROFESSOR'],
    ['Leonidas', 'jpg', 'PROFESSOR' ],
    ['Sergio', 'jpg', 'PROFESSOR'],
    ['Hage', 'jpg', 'PROFESSOR'],
    ['Carlos', 'jpg', 'PROFESSOR'],
    ['background', 'png', 'BACK'],
    ['Insper', 'png', 'INSPER'],
    ['nave', 'png', 'NAVE'],
]

def informacoes_get(tipo):
    informacao = dicionario[tipo.upper()]
    return informacao

def informacoes_set(tipo, novo_valor):
    dicionario[tipo.upper()]=novo_valor


WIDTH = informacoes_get('BACK_WIDTH')
HEIGHT = informacoes_get('BACK_HEIGHT')
PROFESSOR_WIDTH = informacoes_get('PROFESSOR_WIDTH')
PROFESSOR_HEIGHT = informacoes_get('PROFESSOR_HEIGHT')
INSPER_WIDTH = informacoes_get('INSPER_WIDTH')
INSPER_HEIGHT = informacoes_get('INSPER_HEIGHT')
NAVE_WIDTH = informacoes_get('NAVE_WIDTH')
NAVE_HEIGHT = informacoes_get('NAVE_HEIGHT')
TIRO_WIDTH = informacoes_get('TIRO_WIDTH')
TIRO_HEIGHT = informacoes_get('TIRO_HEIGHT')