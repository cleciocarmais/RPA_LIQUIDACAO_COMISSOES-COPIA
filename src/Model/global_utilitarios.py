glob_contas_gerenciais = {
    'NOVALUZ WS' : '41160',
    'CDA' : '41110',
    'CONTERRANEA MATRIZ' : '41120',
    'CONTERRANEA MOSSORO' : '41121',
    'CONTERRANEA MACAIBA' : '41122',
    'JANGADA AUTOMOTIVE' : '41150',
    'JANGADA VEICULOS' : '41135',
    'NATIVA' : '41139',
    'NISSAN MATRIZ' : '41130',
    'NISSAN FILIAL' : '41131',
    'NOSSAMOTO MATRIZ' :'41143',
    'NOSSAMOTO CAUCAIA' : '41144',
    'NOSSAMOTO BATURITE' :'41145',
    'NOSSAMOTO SIQUEIRA' : '41146',
    'NOVALUZ BS' : '41160',
    'NOVALUZ SD' : '41160',
    'NOVALUZ SUL' : '41178',
    'SANAUTO' : '41155',
    'VOUGA' : '41172'


}
glob_nomes_empresas_Delear = {
    'NOVALUZ WS' : 'aguafria',
    'CDA' : 'CDA',
    'CONTERRANEA MATRIZ' : 'CONTERRANEA (MATRIZ) ',
    'CONTERRANEA MOSSORO' : 'CONTERRANEA (FILIAL)',
    'CONTERRANEA MACAIBA' : 'CONTERRANEA (MACAIBA)',
    'JANGADA AUTOMOTIVE' : 'JANGADA AUTOMOTIVE',
    'JANGADA VEICULOS' : 'JANGADA VEICULOS E PEÇAS LTDA',
    'NATIVA' : 'NATIVA',
    'NISSAN MATRIZ' : 'JANGADA IMPORT LTDA - MATRIZ',
    'NISSAN FILIAL' : 'JANGADA IMPORT LTDA - FILIAL 2 (WS)',
    'NOSSAMOTO MATRIZ' :'NOSSAMOTO LTDA (MATRIZ)',
    'NOSSAMOTO CAUCAIA' : 'NOSSOMOTO LTDA (FILIAL CAUCAIA)',
    'NOSSAMOTO BATURITE' :'NOSSAMOTO LTDA BATURITE',
    'NOSSAMOTO SIQUEIRA' : '(NOSSOMOTO SIQUEIRA)',
    'NOVALUZ BS' : 'NOVALUZ',
    'NOVALUZ SD' : 'TERRALUZ SDUMONT',
    'NOVALUZ SUL' : 'NOVALUZ SUL VEICULOS E PECAS LTDA',
    'SANAUTO' : 'SANAUTO',
    'VOUGA' : 'VOUGA'


}

def escreva(text):
    if text == 'Titulo não Encontrado':
        return f'<b style="color: red;">{text}</b>'
    elif text == 'Cliente não Encontrado':
        return f'<b style="color: red;">{text}</b>'
    elif text == 'Valor Divergente no Dealer':
        return f'<b style="color: red;">{text}</b>'
    else:
        return f'<b style="color: green;">{text}</b>'
        



