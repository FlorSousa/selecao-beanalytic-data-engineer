# Selecao para engenheiro de dados jr da beAnalytic

## Baixar chromedrive `125.0.6422.60`
> Para utilizar o Chromedriver, é necessário que você baixe os binários executáveis nos links oficiais e, então, extraia os arquivos .zip
<br>
 
![chromedriver](https://github.com/FlorSousa/selecao-beanalytic-data-engineer/assets/58887452/4845f161-d0a4-4de7-a8f4-43615c8277d4)


### linux x64:

Use o comando abaixo no terminal
```
curl -o /tmp/chromedrive https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/linux64/chromedriver-linux64.zip
```
ou 

[Clique aqui para baixar para linux]("https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/linux64/chromedriver-linux64.zip")

### windows
### [Clique aqui para baixar para windows]("https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/win64/chromedriver-win64.zip")

## Arquivo de credenciais do google cloud

Para se conectar ao `BigQuery`, é preciso usar o arquivo de credenciais fornecido pelo Google Cloud. Use o arquivo .env e substitua a variável de ambiente PATH_TO_CLOUD_CREDENTIALS pelo caminho até o seu arquivo de credenciais.

Observação: Ao criar o arquivo de credenciais no google cloud, adicione ao perfil o acesso ao bigQuery

<br>
<br>

![screenshot](https://github.com/FlorSousa/selecao-beanalytic-data-engineer/assets/58887452/53b6e84f-710a-49ab-829d-1fba5c5210aa)


### Criando um arquivo .env
> No diretório deste repositório existe um arquivo chamado `.env.example` como layout das variáveis de ambiente. Execute o comando abaixo para criar um arquivo `.env` e coloque o caminho para o arquivo de credenciais.

```
cp -r .env.example .env
```

## Usando o scrip de automatização

### Instalar bibliotecas
Utilize o comando abaixo para instalar as bibliotecas python usadas

```
pip install -r requirements.txt
```

### executando
> Certifique-se de que o arquivo `.env` está com o caminho correto para o seu arquivo JSON de credenciais.
#### Linux
```
python3 main.py
```

#### Windows

```
python main.py
```

## Sobre o código

O script deste repositório usa o selenium junto com o Chromedriver para realizar web scraping da página https://steamdb.info/sales e armazena os dados da tabela HTML no serviço do Google Cloud BigQuery. Os dados da tabela do BigQuery estão também disponíveis em uma planilha do Google Sheets, que pode ser acessada  [clicando aqui]("")
