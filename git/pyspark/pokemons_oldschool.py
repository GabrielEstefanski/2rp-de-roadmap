%pyspark


from pyspark.sql import functions as func

base = spark.table("work_dataeng.generation_gabriel_braga")

base = base.select(["generation", "date_introduced"])

base = base.filter("date_introduced<'2002-11-21'")


base2 = spark.table("work_dataeng.pokemon_gabriel_braga")

base2 = base2.select(["idnum", "name", "hp", "speed", "attack", "special_attack", "defense", "special_defense", "generation"])


result = base.join(base2,\
base.generation == base2.generation, "inner")

result.show()
