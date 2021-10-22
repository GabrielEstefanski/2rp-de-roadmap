%pyspark


from pyspark.sql import functions as func

base = spark.table("work_dataeng.generation_gabriel_braga")


base = base.select(["generation","data_introduced"])

base = base.filter("data_introduced<'2002-11-21'")


base2 = spark.table("work_dataeng.pokemon_gabriel_braga")
base2 = base2.select(["generation","idnum", "name", "hp", "speed", "attack", "special_attack", "defense", "special_defense"])
base= base.withColumnRenamed('generation', 'pokememon_generation')

base = base.cache()

result = base.join(base2,
base.pokememon_generation == base2.generation, 'inner')



result.write.insertInto("work_dataeng.pokemons_oldschool_gabriel_braga")