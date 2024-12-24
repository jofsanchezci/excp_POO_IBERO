#prueba Archivo
try:
  f = open("demofile.txt","a")
  try:
    f.write("Lorum Ipsum..,mnbvcxzsawertyui")
  except:
    print("Algo sale mal cuando se escribe en el archivo")
  finally:
    f.close()
except:
  print("Algo sale mal cuando se abre el archivo") 



