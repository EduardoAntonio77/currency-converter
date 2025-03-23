import requests

# Coletando dados do usuario
de_moeda = input('De qual moeda de deseja converter?: ')
para_moeda = input('Para qual moeda deseja converter?: ')
quanto = int(input('Quantos {} deseja converter para {}?: '.format(de_moeda, para_moeda)))

def convercao(demoeda, paramoeda, quantidade):

    # criando uma variavel que recebe a url da api substituindo as informações das moedas na url da api conforme os dados informados pelo usuario
    api_url = "https://economia.awesomeapi.com.br/json/last/{}-{}".format(demoeda, paramoeda)

    # criando uma variavel que recebe a requisição da da url da api
    requisicao = requests.get(api_url)

    status = requisicao.status_code
    if status != 200:
        print(f'Ocorreu um erro {status} na requisição, tente novamente ')

    # criando uma variavel que recebe em formato json o conteudo da variavel "requisicao"
    requisicaojson = requisicao.json()

    # criando uma variavel que recebe uma referencia para usa-la ao requisitar a lista em json com os parametros das moedas selecionadas pelo usuario
    chave = f"{demoeda}{paramoeda}"

    # criando uma variavel que esta recebendo a lista json requisitava na variavel "requisicaojson" mas com os valores recebidos pela variavel "chave" junto ao parametro "high" que neste caso esta requisitando a cotação entre as duas moedas selecionadas pelo usuario (pelo amor de Deus, nao esqueça do float se não, o print com o resultado final ira printar a cotaç)
    cotacao =  float(requisicaojson[chave]["high"])

    # fazendo a conversão da cotação com a quantiade escolhida pelo usuario
    valor_final = cotacao * quantidade

    # Exibe na tela as moedas que o usuario escolheu, a quantidade e como resultado final, o valor total da conversão
    print("A conversão de {}{} para {}, ${:.2f}".format(quantidade, paramoeda, demoeda, valor_final))
convercao(de_moeda, para_moeda, quanto)