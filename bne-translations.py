#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:11:16 2026

@author: gustavo
"""
import json
import ijson

# we compute the total number of records with different values for lengua_pricipal and lengua_original
with open("monomodernas-JSON/mon/monomodernas-JSON.json", "rb") as f:
    count = 0
    for obj in ijson.items(f, "item"):
        #print(obj)
        #break
        if obj.get("lengua_principal") == "español" and \
          obj.get("lengua_original") != "español" and \
          obj.get("lengua_original") is not None:
           count = count +1
    print(count)

outfile = 'traducciones.json'
count = 0
with open('monomodernas-JSON/mon/monomodernas-JSON.json', "rb") as infile, open(outfile, "w") as outfile:
    outfile.write("[")
    first = True
    for obj in ijson.items(infile, "item"):
        if obj.get("lengua_principal") == "español" and \
          obj.get("lengua_original") != "español" and \
          obj.get("lengua_original") is not None:
            if not first:
                outfile.write(",")
            json.dump(obj, outfile)
            first = False
            count += 1
    outfile.write("]")

print("total items: " + str(count))

