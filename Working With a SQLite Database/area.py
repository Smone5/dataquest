import sqlite3 as sql

conn = sql.connect("factbook.db")
c = conn.cursor()
area_land = c.execute("SELECT SUM(area_land) from facts WHERE area_land != "";)

area_water = c.execute("SELECT SUM(area_water) from facts WHERE area_water != "";)

print(area_land / area_water)
