# Stack - Bootcamp de Data Science 2021 🔎🎲
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Apache Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)
### 📃 Descrição
O objetivo do projeto é desenvolver uma **aplicação de Recursos Humanos (RH)**, que permita predizer se um **colaborador deixará a empresa**. O projeto engloba desde a **extração dos dados** até a implantação de um **WebApp**.

O projeto foi elaborado pela **[Stack](https://stacktecnologias.com.br/)** no **bootcamp de Data Science** com algumas modificações minhas. Recomendo também o site **[Minerando Dados](https://minerandodados.com.br/)** de Data Science dos mesmos fundadores.

<p align="center"><img src="images/stack_bootcamp_overview.jpg" width="700"></p>

<p align="center">Imagem retirada do canal da <a href="https://www.youtube.com/c/Stack_tecnologias">Stack</a></p>

### 😵 Problema

O problema envolve o **setor de RH** de uma empresa, que deseja entender o que leva seus **colaboradores a deixarem**.

* **Quais fatores influenciam para um colaborador deixar a empresa?**
  * Pessoas insatisfeitas?
  * Ambiente de trabalho?
    * Cargo, Departamento...
  * Salário?
  * Tempo na empresa?
* **Podemos nos antecipar e saber se um determinado colaborador vai sair da empresa?**
  * Desempenho do colaborador.
  * Carga de trabalho.
* **Como diminuir o turnover?**

### 📚 Conteúdo
- Fonte de dados com MySQL e arquivos
- Data Lake com MinIO
- Automatização de Pipeline com Apache Airflow
- Conteinerização com Docker
- Análises e modelagem com Python e Jupyter Notebook
- WebApp com Streamlit

### 🎲 Entendendo a estrutura dos dados

* **Banco de dados**:
  * Projetos atribuídos a cada colaborador.
  * Data de contratação, acidente de trabalho.
  * Departamento, Salário e se o colaborador deixou a empresa.
* **Avaliação de desempenho:**
  * Satisfaction Level - O nível de satisfação do colaborador.
  * Last Evaluation - Nota atribuída ao colaborador na última avaliação de desempenho.
  * Com os dados de **registros de horas de trabalho**, podemos conseguir a quantidade de horas trabalhadas nos últimos meses.

<p align="center"><img src="images/stack_bootcamp_modelagem_dados.jpg" width="800"></p>

<p align="center">Imagem retirada do canal da <a href="https://www.youtube.com/c/Stack_tecnologias">Stack</a></p>

# Preparação do ambiente

1. Faça download do Anaconda no site: https://www.anaconda.com/products/individual#Downloads
2. Instalar o Docker Desktop no Windows ou no Linux: https://www.docker.com/get-started

1. Faça download do Visual Studio code: https://code.visualstudio.com/download

## Crie um diretório na sua máquina para armazenar scripts e outros artefatos, exemplo:

*C:\bootcampds*

*/home/<seunome>/bootcampds*

## **Instalação e Configuração do Mysql Server**

Se estiver usando Windows abra o **Powershell** e digite:

Crie o container do mysql habilitando a porta 3307:

```
docker run --rm --name mysqlbd1 -e MYSQL_ROOT_PASSWORD=bootcamp -p "3307:3306" -d mysql
```

Teste o acesso ao banco de dados usando o Visual Studio Code:

Abra o Visual Studio Code e instale a extensão: **Database Client**

![img](https://quark-wineberry-cc8.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff8300c92-6830-4afd-8f5f-2747899e0df8%2FCaptura_de_Tela_2021-10-17_as_15.23.12.png?table=block&id=f71d7a6b-9ef4-44e2-bbbe-200593d73ee9&spaceId=9450dd1e-983a-4fac-8310-e6a465d9ca38&width=1690&userId=&cache=v2)

Teste o acesso ao banco de dados Mysql:

Coloque as configurações:

**Host**: 127.0.0.1

**Username**: root

**Port**: 3307

**Password**: bootcamp

![img](https://quark-wineberry-cc8.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F2ee9380f-dc42-44c9-976a-fb48b57fd4b0%2FCaptura_de_Tela_2021-10-17_as_15.28.28.png?table=block&id=d15ac159-f5b7-43af-a8f2-d090b4598547&spaceId=9450dd1e-983a-4fac-8310-e6a465d9ca38&width=2000&userId=&cache=v2)

## **Instalação e Configuração do Data Lake com Minio Server**

Dentro do diretório bootcampds crie o diretório **datalake**.

Se estiver usando Windows abra o terminal do Powershell e execute o comando:

```
docker run -d -p 9000:9000 -p 9001:9001 -v "$PWD/datalake:/data" minio/minio server /data --console-address ":9001"
```

Teste o acesso ao Minio:

Abra o browser e digite: http://localhost:9001/login

**username**: minioadmin

**password**: minioadmin

## Instalação e Configuração do Airflow.

1. Dentro do diretório bootcampds crie o diretório **airflow**.

2. Navegue até o diretório airflow e crie o diretório **dags**.

3. Faça download da imagem e execute o container do Apache Airflow

   3a. Se estiver usando Windows abra o terminal do Powershell e execute o comando:

   `docker run -d -p 8080:8080 -v "$PWD/airflow/dags:/opt/airflow/dags/" --entrypoint=/bin/bash --name airflow apache/airflow:2.1.1-python3.8 -c '(airflow db init && airflow users create --username admin --password bootcamp --firstname Felipe --lastname Lastname --role Admin --email admin@example.org); airflow webserver & airflow scheduler'`

   3b. Instale as bibliotecas necessárias para o ambiente:

   Execute o comando abaixo para se conectar ao container do airflow:

   `docker container exec -it airflow bash`

   Em seguida instale as bibliotecas:

   `pip install pymysql` `xlrd` `openpyxl minio`

   3c. Se não der nenhum erro, acesse a interface web do Apache Airflow com o endereço (*Aguarde uns 5 minutos antes de abrir o terminal*):

   `https://localhost:8080`

   **Faça o login de acesso ao Apache Airflow**

Clique em Admin >> Variables

Crie as seguintes variáveis:

*data_lake_server = 172.17.0.4:9001* *data_lake_login = minioadmin* *data_lake_password = minioadmin*

*database_server = 172.17.0.2 ( Use o comando inspect para descobrir o ip do container: docker container inspect mysqlbd1 )* *database_login = root* *database_password = bootcamp* *database_name = employees*

![img](https://quark-wineberry-cc8.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F0985d7e4-764b-43c2-a72d-ba228396ed19%2FCaptura_de_Tela_2021-10-17_as_16.58.07.png?table=block&id=0d8e5eda-7f0f-45f9-a4fc-d94bfe6ecf4c&spaceId=9450dd1e-983a-4fac-8310-e6a465d9ca38&width=1890&userId=&cache=v2)

As variáveis criadas devem ficar como:

![img](https://quark-wineberry-cc8.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F5d460857-a041-483f-ad68-ff6a0b4a26ee%2FCaptura_de_Tela_2021-10-17_as_17.03.14.png?table=block&id=cb1f28f0-33d6-483b-b23e-dd2a7409ca0f&spaceId=9450dd1e-983a-4fac-8310-e6a465d9ca38&width=2000&userId=&cache=v2)



# Aula 1 - Modelagem de Dados - 19/10/2021

## Configurando o Data Lake

1. Acesse o link abaixo e faça download de todos os arquivos que usaremos nesta aula.

   1. link:  https://bit.ly/arquivos-bootcamp

2. Inicie o container do Minio com o comando:

   1. Abra o **Docker Desktop** para iniciar o docker engine

   2. Abra o Powershell (Windows) e execute o comando abaixo para iniciar o container do Minio: `docker container start <nome-do-container>`

   3. Em seguida acesse o console do minio no endereço: http://localhost:9001/login

   4. Crie os buckets *landing, processing e curated* como na imagem a seguir:

   5. Clique em **Buckets** em seguida clique em **create bucket**

      ![img](https://quark-wineberry-cc8.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F6917bff8-163a-437c-9582-b36b75fae352%2FCaptura_de_Tela_2021-10-19_as_14.43.00.png?table=block&id=bc9e4800-6242-4db9-8391-026b34f5da81&spaceId=9450dd1e-983a-4fac-8310-e6a465d9ca38&width=2000&userId=&cache=v2)

   6. Após criar os buckets clique no bucket landing e crie a pasta: **performance-evaluation** em seguida clique em Upload e carregue o arquivo: **employee_performance_evaluation.json** Veja a imagem abaixo:

      ![img](https://quark-wineberry-cc8.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F4accbcf3-0c03-49c6-a312-c4656acc1fa0%2FCaptura_de_Tela_2021-10-19_as_14.53.34.png?table=block&id=824ec7fc-4d1b-4618-8031-b0c256075a03&spaceId=9450dd1e-983a-4fac-8310-e6a465d9ca38&width=2000&userId=&cache=v2)

   7. Clique no bucket landing

   8. Crie outra pasta chamada **working-hours** e faça upload dos arquivos .xlsx veja como fica na imagem abaixo:

      ![img](https://quark-wineberry-cc8.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F14595a33-2b25-4938-b3ca-5a14c6c40033%2FCaptura_de_Tela_2021-10-19_as_14.56.03.png?table=block&id=8122be70-a713-482d-a3c6-c0a665b9b6af&spaceId=9450dd1e-983a-4fac-8310-e6a465d9ca38&width=2000&userId=&cache=v2)

   9. Ao clicar no bucket landing ficamos como:

   ![img](https://quark-wineberry-cc8.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Feefda08e-3ce4-4ed5-9011-1a3976d15699%2FCaptura_de_Tela_2021-10-19_as_14.57.12.png?table=block&id=11a9e54c-4669-417d-952b-3712983caaf9&spaceId=9450dd1e-983a-4fac-8310-e6a465d9ca38&width=1950&userId=&cache=v2)

# Subindo o banco de dados e carregando o banco de dados

1. Abra o Docker Desktop para iniciar o docker engine

2. Abra o console do Powershell (Windows) ou o terminal linux e execute o comando abaixo para iniciar o container do mysql: `docker container start mysqlbd1`

3. Em seguida abra o Visual Studio Code para carregar o arquivo .sql para dar carga no banco de dados:

4. Clique com o botão direito do mouse na conexão como mostrado na imagem abaixo

   ![img](https://quark-wineberry-cc8.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F5fc61f56-4801-4afc-a611-d3b0badc4f42%2FCaptura_de_Tela_2021-10-19_as_15.03.34.png?table=block&id=6227695b-d000-4b93-a8e1-dcee058c1478&spaceId=9450dd1e-983a-4fac-8310-e6a465d9ca38&width=1140&userId=&cache=v2)

5. Escolha a opção Import Sql

6. Aguarde o processo de importação. Após importar clique em atualizar a conexão para visualizar o banco de dados **employees** recém criado. Veja imagem abaixo:

   ![img](https://quark-wineberry-cc8.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbe2d137a-a387-4227-bb67-c8286ebc0d2b%2FCaptura_de_Tela_2021-10-19_as_15.07.17.png?table=block&id=c3f5559f-fe0c-4e73-b8b8-aa97b81fa4ab&spaceId=9450dd1e-983a-4fac-8310-e6a465d9ca38&width=1140&userId=&cache=v2)

# Subindo o Airflow e criando as Dags:

1. Descompacte os arquivos .py dentro do seu diretório usado no bootcamp, exemplo *C:\Felipe\bootcampds ou /home/felipe/bootcamps*

2. Mova os arquivos .py para o diretório **airflow/dags** como na imagem abaixo:

   ![img](https://quark-wineberry-cc8.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F394d8ab6-bc9a-4b57-a7e1-a0c8928a01e9%2FCaptura_de_Tela_2021-10-19_as_15.19.33.png?table=block&id=0a5ea23c-c66a-4437-92b5-5675f5e5f3b9&spaceId=9450dd1e-983a-4fac-8310-e6a465d9ca38&width=1740&userId=&cache=v2)

3. Atenção: Certifique que todos os arquivos estão dentro do diretório **airflow/dags**

4. Abra o console do Powershell (Windows) ou o terminal linux e execute o comando abaixo para iniciar o container do mysql: `docker container start airflow`

5. Aguarde uns 5 minutos e acesse o console do airflow no endereço: http://localhost:8080/

6. Faça o login com usuário admin e a senha bootcamp.

7. Ao clicar em Dags deve aparecer as dags criadas como na imagem abaixo:

   ![img](https://quark-wineberry-cc8.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fa8376905-dbd0-46f1-99b9-e4f33226ba2b%2FCaptura_de_Tela_2021-10-19_as_15.22.07.png?table=block&id=4a968b44-0fac-4077-8002-e27b6c6cf5d6&spaceId=9450dd1e-983a-4fac-8310-e6a465d9ca38&width=2000&userId=&cache=v2)

# Rodando as Dags:

1. **Atenção**: Antes de executar as dags verifique se o ip do mysql ou do minio alterou.
2. Para verificar use o comando: `docker container inspect mysqlbd1` e visualize o campo IP Address
