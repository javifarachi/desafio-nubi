import gdown
import findspark
from pyspark.sql import SparkSession

# Descargo el documento:
# Accedí "a manopla" al archivo y obtuve     el vínculo (botón derecho). Obtuve lo siguente:
# url = 'https://drive.google.com/file/d/1mZV6T5p_YUnIPlkQzK1q9-rNJpgV6AIA/view?usp=sharing'
# Al probar con esa url, me tiró un warning sugiriendo usar esto:
url = 'https://drive.google.com/uc?id=1mZV6T5p_YUnIPlkQzK1q9-rNJpgV6AIA'
output = 'Sellers.json'
gdown.download(url, output, quiet=False)

# Inicio sesión de spark
findspark.init()
spark = SparkSession.builder.getOrCreate()

# Cargoel contenido en un df y hago el select
df = spark.read.json("/content/Sellers.json")
#TODO: Renombrar columnas
#TODO: Justificar a izquierda los valores
df.select(df.body.site_id, df.body.id, df.body.nickname, df.body.points).show()