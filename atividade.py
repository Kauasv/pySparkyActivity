#a linha abaixo importa a clase sprarky session do modulo pyspark.sql
# #no python, a palavra chave "from" e usada para indicar de onde vamos trazer algo.
# #aqui em baixo estamos dizendo: do modulo spark.sql traga "apanas a pysparksession.".
# #o spark session  e um classe fundamental para trabalhar com spark no pyspark ele e como a porta de entrada para usar todas as funções do spark

# from pyspark.sql import SparkSession
# #agora imortamos duas funções avg (calcula a media), count (para contar registros)
# #essas funções ficam dentro do modulo pyspark sql.functions
# #elas permitem que façamos calculos diretamente em colunas de tabelas do spark
#aqui criamos a variavel chamada spark poderiamos dar outro nome, 
# porem e uma convenção mundial chamar essa variavel de spark
# para deixar o codigo claro e padronizado
# sparksession.biulder inicia a construção de uma sessão sparko 
# metodo app.name nome para nossa aplicação 
# nos logs e em ambientes distribuidos , mais aqui e apenas ilustrativo,
# por fim o metodo get or creat o app name crai a sessão se ela não existir ou reutiliza 
# uma ja existente evitendo erros de duplicação
from pyspark.sql.functions import avg, count

spark = SparkSession.builder.appName("AnaliseHousing").getOrCreate()

#aqui usamos a variavel spark para acessaar o metodo read que e usado para acessar arquivos
#estamos lendo um arquivo no formato csv por isso usamos read.csv
# o parametro haussing.csv e o nome do arquivo, ele precisa estar na mesma pasta que esse codigo
# o reader igual true que a primeira linha do arquivo contem os nomes das figuras
#aqui usamos a variavel para acessar o arquivo 


df = spark.read.csv("housing.csv", header=True, inferSchema=True)

#aqui pegamos somente as 5 primeiras linhas do data frame usando limit,
#df e uma estrutura parecida com a tabela do banco de dados
#.toPandas converte o data frame 
#QUE E MAIS FACIL DE SALVAR EM CSV LOCALMENTE
#.to_csv salva o resultado em um novo arquivo chamado "amostra 5 linhas.csv"
#index igual a false significa que não adicionaremos numeração de linhas (trocar pra true)
#aqui fazemos uma operação de agrupamento usando groupby.
#vamos agrupar os registros pela coluna ocean_proximity
#depois usamos a avg para aplicar funções agregadoras: count e avg
#count("conta quantos registros existem em cada grupo")
#avg (midiam hose velope, calcula a media dos valores medianos por grupos)
#as serve pra dar nomes mais claros a colunas no resultado
#convertendo o resultado para pandas para salvar em csv, 
# este arquivo mostrara quantas casas existem em cada tipo de proximidade
#e o valor medio das casas nesses locais
#
df.limit(5).toPandas().to_csv("amostra_5_linhas.csv", index=False)

resultados = df.groupBy("ocean_proximity").agg(
    count("*").alias("total_casas"),
    avg("median_house_value").alias("media_valor_casas")
)

resultados.toPandas().to_csv("resultados_analise.csv", index=False)
#media geral vai receber nossos df,
#df .agg realiza uma congregassão sobre todo dataframe
#obtem o primeiro valor da primeira linha retornada
#ja que op resultado vem em formato estruturado
#aqui contamos quantos registros linhas existem no "dataset"


media_geral = df.agg(avg("median_house_value")).first()[0]
total_registros = df.count()
#agora abrimos um arquivo chamado resumo .txt
#no modo de escrita"w"
#com o as f: vamos definir para f redefine uma variavel pra algo
#usamos write para escrever duas linhas: o total de registro, depois a media geral dos valores
#esta linha encerra a sessão em spark e como desligar o motor apos terminar o trabalho
with open("resumo.txt", "w") as f:
    f.write(f"Total de registros: {total_registros}\n")
    f.write(f"Média geral de valores das casas: {media_geral:.2f}\n")

spark.stop()