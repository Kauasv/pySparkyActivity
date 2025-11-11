# linha que importa a SparkSession d modulo pyspark 
# No projeto a palavra "from" é usada  para indicar de onde vamos trazer algo 
# Aqui em baixo estamos disendo : do modulo pyspark.sql traga  "SparkSession"
# o SparkSession é uma classe fundamental para trabalhar como spark no pyspark  ele é como a porta de entrada para usar todas as fuçoes do spark 
# count : serve para contar registros 
# AVG : serve para calcular a media 
# essas funções ficam dentro do  modulo pyspark.sql.functions
# elas permitem que fassamos calculos diretamente em colunas de tabelas do spark .
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

# Aqui criamos a variavel chamada spark. poderiamos dar qualquer nome ,
# porem é uma conveição mundial chamar esta variaVel de spark para deixar o codigo claro e padronizado 
# spark = SparkSession.builder.appName("AnaliseHousing").getOrCreate()
# sparksection.builder inicia a construção de uma seção do spark 
# o metodo appName defiene um nome para a nossa aplicação : 
# ---> isso serve para indentificação 
# nos logs e em ambientes distribuidos . 
# mas aqui é apenas ilustrativo. 
# por fim , o metodo get our crate (Cria a seção se ela ainda não existir)
# ou reutiliza uma ja existente evitando erros de duplicação .  


df = spark.read.csv("housing.csv", header=True, inferSchema=True)

df.limit(5).toPandas().to_csv("amostra_5_linhas.csv", index=False)

resultados = df.groupBy("ocean_proximity").agg(
    count("*").alias("total_casas"),
    avg("median_house_value").alias("media_valor_casas")
)

resultados.toPandas().to_csv("resultados_analise.csv", index=False)

media_geral = df.agg(avg("median_house_value")).first()[0]
total_registros = df.count()

with open("resumo.txt", "w") as f:
    f.write(f"Total de registros: {total_registros}\n")
    f.write(f"Média geral de valores das casas: {media_geral:.2f}\n")

spark.stop()