# S14_PyETL_StarterFile.py  v4
#  K.Schmitz (c) 2022, 2023, 2024, 2025
#  Starter File for CIS2010 Session 14, Structured Query Language
##################Initialization information, do not modify ################
from cis2010utils5 import StartHere, EndHere, runsql 
#from colorama import Fore
import pandas as pd
import sqlite3
############################################################################
# Open up the database  ########## Do not modify these instructions#########
db_name =  "irs18.db"
db_conn = sqlite3.connect(db_name)
sqltxt = "SELECT COUNT(zipcode) FROM irsz" ; zz = pd.read_sql(sqltxt, db_conn) ; print("\nnumber of zipcodes\n", zz)
sqltxt = "pragma table_info('irsz')" ; t1 = pd.read_sql(sqltxt, db_conn) ; print("irsz table\n", t1)
sqltxt = "pragma table_info('zco')" ; t2 = pd.read_sql(sqltxt, db_conn) ; print("zco table\n", t2)
############################################################################
#
# Task 2a
StartHere( "Ibrahim", "S14w", "Fal")
#
# Task w2b
sqlw2b = """
SELECT state, zipcode, n1
FROM irsz
"""
w2b = runsql( sqlw2b, db_conn, False, "task w2b")

# Task w2c
sqlw2c = """
SELECT state, zipcode, n1, numdep, a00100*1000, schf
FROM irsz
"""
w2c = runsql( sqlw2c, db_conn, False, "task w2c")

# Task w2d
sqlw2d = """
SELECT state, zipcode, n1, numdep, a00100*1000, schf,
  a06500*1000, a19700*1000
FROM irsz
"""
w2d = runsql( sqlw2d, db_conn, False, "task w2d")

# Task w3a
w2d.to_csv('x2d.csv', sep=',')

# Workshop END
#
###########################################################
# Individual Challenge
#
# S14icq Q1
StartHere( "Ibrahim", "S14wic", "Fal")

#
# S14icq Q2
sqlic2 = """
SELECT state, zipcode, n1, numdep, a00100*1000, schf,
  a06500*1000, a19700*1000
FROM irsz
WHERE zipcode > 1000
AND zipcode < 99999
"""
ic2 = runsql( sqlic2, db_conn, False, "task ic2")

#
# S14icq Q3
sqlic3 = """
SELECT state, zipcode, n1, numdep, a00100*1000, schf,
  a06500*1000, a19700*1000
FROM irsz
WHERE zipcode > 1000
AND zipcode < 99999
AND state = 'GA'
"""
ic3 = runsql( sqlic3, db_conn, False, "task ic3")

#
# S14icq Q4
sqlic4 = """
SELECT state, zipcode, n1, numdep, a00100*1000, schf,
  a06500*1000, a19700*1000, elderly, n2
FROM irsz
WHERE zipcode > 1000
AND zipcode < 99999
AND state = 'GA'
"""
ic4 = runsql( sqlic4, db_conn, False, "task ic4")

#
# S14icq Q5
ic4.to_csv("ic4.csv",sep=',')


# Cleanup, Save and End
db_conn.close()
EndHere( globals())
###########################################################
#Atr`$*,ROTJ%XYZIJSY}N=OP4R$/6Vo30z@[QL{lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
#Atr`$&+ENGWFMNRjklM}N=OP4R$/6Vo30z@[QL{lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
