#!/usr/bin/python
dic = {}
fd = open("/etc/passwd","r")
texto = fd.read()
lineas= texto.split("\n")
for linea in lineas:
	conf = linea.split(":")
	usuario = conf[0]
	shell = conf[-1][:-1]
	dic[usuario] = shell
try:
	print "El usuario root usa la shell",dic["root"]
	print "El usuario imaginario usa la shell","\n",dic["imaginario"]
except KeyError:
	print  "ERROR:La palabra clave introducida es incorrecta"








#print "El usuario:", usuario,"usa esta shell: ",dic[usuario]
#longitud = len(dic)
#print "Hay", longitud, "usuarios"
