import time
import random
#UTILIZO LA FUNCION ".strip()" para eliminar los espacios en blanco dentro de los input
countt=0
lispregts=["¿Cuál de estas opciones no es una banda de rock?","¿Quién es el creador del lenguaje de programación Python?"]
tuplaresp1=("a-The Beatles","b-Queen","c-Corazon Serrano","d-Linkin Park")
tuplaresp2=("a-Guido Vann Rosum","b-Guiño Ven Rosa","c-Guido Von Rose","d-Guiso Von Rossem","f-Guido Van Rossum","?-")
repe=True
listarnombres=[];listarpuntos=[] #DATOS DEL JUGADOR
lisres=["respuesta1","respuesta2","respuesta3","respuesta4"];lisacml=["a","b","c","d"] #OPCION 'AGREGAR PREGUNTA'

while repe==True:
	lisptjtotal=[]
	countt=countt+1
	if countt<=1:
		print("\033[32m¡Bienvenid@ a mi trivia!\033[39m")
		time.sleep(1)
		print("Aquí verás la lista de jugadores y sus puntuaciones\n...")
		time.sleep(2)
		print("\033[33mPor el momento no tenemos ningún registro\033[39m")
		time.sleep(1)		
	else:
		print("\033[32m¡Bienvenid@ a mi trivia una vez más!\033[39m")
		time.sleep(1)
		print("Este es el historial de los jugadores y sus puntuaciones:")		
		for i in range(len(listarnombres)):
			print("\033[34mEl puntaje del jugador",listarnombres[i],"es",listarpuntos[i],"\033[39m")
		time.sleep(1)	
	print("\n\033[36mEste es el número de veces que has realizado la trivia -> ",countt," <- \033[39m\n")
	time.sleep(2)
	nombre=input("Ingresa tu nombre, por favor: ").strip()
	print("...")
	listarnombres.append(nombre)
	time.sleep(1)
	contpreg1=0
	contpreg2=0
	while nombre in (""):
		nombre=input("\033[33mNo has ingresado ningún caracter, ingresa tu nombre, por favor: \033[39m\n").strip()
		print("...")
		time.sleep(1)
	print("¡Hola "+nombre+", a continuación te haré una serie de preguntas!\nTu puntuación actual es de",contpreg1,", irás ganando puntos si respondes bien.")
	time.sleep(1)
	print("\n\033[31m",lispregts[0],"\033[39m")
	time.sleep(1)
	for i in range(len(tuplaresp1)):
		print("\n",tuplaresp1[i])
	respuesta=input("\nTu respuesta es: ").lower().strip()
	time.sleep(1)
	while respuesta not in ("a","b","c","d"):
		respuesta=input("\033[33mPor favor "+nombre+", ingresa solo una letra entre a,b,c o d: \033[39m\n").lower().strip()
		time.sleep(1)
	if respuesta=="c":
		print("¡\033[32mTu respuesta es correcta, "+nombre+"!\033[39m")
		contpreg1+=2
		time.sleep(1)
		print("\033[34mEsta es tu puntuación por el momento: ",contpreg1,"\033[39m\n")
		time.sleep(1)
		print("\033[33m¡Ten cuidado! la siguiente pregunta tiene puntos en contra, se te restará puntos si respondes mal\033[39m")
		print("\nNota: Hay una opción secreta relacionada a una serie de expedientes que te puede dar una gran cantidad de puntos.\n");time.sleep(3)	
	else:
		print("\033[33mTu respuesta es incorrecta, "+nombre+"\033[39m")
		contpreg1+=0
		time.sleep(1)
		print("\033[34mEsta es tu puntuación por el momento: ",contpreg1,"\n\033[39m")
		time.sleep(1)
		print("\033[33m¡Ten cuidado! la siguiente pregunta tiene puntos en contra, se te restará puntos si respondes mal\033[39m")
		print("\nNota: Hay una opción secreta relacionada a una serie de expedientes que te puede dar una gran cantidad de puntos.\n");time.sleep(3)

	lisptjtotal.append(contpreg1)			
	input("Presiona Enter para continuar a la pregunta \n")
	print("\n\033[31m",lispregts[1],"\033[39m")
	time.sleep(1)
	for i in range(len(tuplaresp2)):
		print("\n",tuplaresp2[i])
	respuesta2=input("\nTu respuesta es: ").lower().strip()
	time.sleep(1)
	while respuesta2 not in ("a","b","c","d","f","x"):
	  respuesta2=input("\033[33mPor favor "+nombre+", ingresa solo una letra entre a,b,c, d o f: \033[39m\n").lower().strip()
	  time.sleep(1)
	if respuesta2=="a":
	  print("\033[33mTu respuesta es incorrecta, \033[39m"+nombre+", pero te has acercado bastante así que has ganado 1 punto")
	  time.sleep(1)
	  contpreg2+=1
	elif respuesta2=="b":
	  print("\033[33mTu respuesta es incorrecta, "+nombre+", has perdido 2 puntos\033[39m")
	  time.sleep(0.5)
	  contpreg2-=2	  
	elif respuesta2=="c":
	  print("\033[33mTu respuesta es incorrecta, \033[39m"+nombre+", pero te has acercado un poco, no se te restarán puntos")
	  time.sleep(0.5)
	  contpreg2+=0
	elif respuesta2=="d":
	  print("\033[33mTu respuesta es incorrecta, "+nombre+", has perdido 1 punto\033[39m")
	  time.sleep(0.5)
	  contpreg2-=1  
	elif respuesta2=="x":
	  print("\033[35m¡Felicidades, "+nombre+", has encontrado la respuesta secreta!\n¡Has ganado 5 puntos!\033[39m")
	  time.sleep(0.5)
	  contpreg2+=5 
	else:
	  print("\033[32mTu respuesta es correcta, "+nombre+", has ganado 2 puntos\033[39m")
	  time.sleep(0.5)
	  contpreg2+=2


	lisptjtotal.append(contpreg2)			
	  

	contpreg3=0

	if len(lispregts)==3:
		print("Hemos detectado que has añadido una pregunta");time.sleep(1)
		input("Presiona Enter para pasar a la pregunta ")
		print("\n\033[31m",lispregts[2],"\033[39m")
		time.sleep(1)
		for i in range(len(lisres)):
			print("\n"+lisacml[i]+"-"+lisres[i]+"\n",end=" ")
		respuesta3=input("\nTu respuesta es: ").lower().strip()
		time.sleep(1)
		while respuesta3 not in lisacml:
			respuesta3=input("\033[33mPor favor "+nombre+", ingresa solo una letra entre a,b,c o d: \033[39m\n").lower().strip()
			time.sleep(1)
		if respuesta3=="a":
			print("¡\033[32mTu respuesta es correcta, "+nombre+"!\033[39m")
			contpreg3+=2
			lisptjtotal.append(contpreg3)
			print("\033[34mEsta es tu puntuación final: ",sum(lisptjtotal),"\033[39m")
		else:
			print("\033[33mTu respuesta es incorrecta, "+nombre+"\033[39m")
			contpreg3+=0
			lisptjtotal.append(contpreg3)
			print("\033[34mEsta es tu puntuación final: ",sum(lisptjtotal),"\033[39m")

	else:
		print("\033[34mEsta es tu puntuación final: ",sum(lisptjtotal),"\033[39m")

	time.sleep(1)
	if sum(lisptjtotal)<=0:
		puntajeruleta = random.randint(-5,10)
		fi=input("Tienes 0 puntos o menos... \033[31m¿Quieres intentar aumentar tus puntos en una ruleta aleatoria?\033[39m\nRecuerda que podrías perder más puntos también\nResponde Si/No: ").lower().strip()
		time.sleep(1)
		while fi not in ("si","no"):
			fi=input("\033[33m¡Incorrecto! Responde una alternativa válida entre\033[39m Si y No, por favor: \n").lower().strip()
			time.sleep(1)
		if fi==("si"):
			print("\033[35mGirando...")
			time.sleep(2)
			print("Este es el valor de la ruleta: \033[39m", puntajeruleta)
			sumapnts=sum(lisptjtotal)+puntajeruleta
			print("Procesando...")
			time.sleep(1)
			print("\033[34mEsta es tu puntuación final: ", sumapnts,"\033[39m")
			listarpuntos.append(sumapnts)
		else:
			print("\033[34mEsta es tu puntuación final: ", sum(lisptjtotal),"\033[39m")
			listarpuntos.append(sum(lisptjtotal))
	else:		
		puntajeruleta2 = random.randint(-10,20)
		fi=input("\033[31m¿Quieres intentar aumentar tus puntos en una ruleta aleatoria?\033[39m\nRecuerda que podrías perder puntos también\nResponde Si/No: ").lower().strip()
		time.sleep(1)
		while fi not in ("si","no"):
			fi=input("\033[33m¡Incorrecto! Responde una alternativa válida entre\033[39m Si/No, por favor: \n").lower().strip()
			time.sleep(1)
		if fi==("si"):	
			print("\033[35mGirando...")
			time.sleep(2)
			print("Este es el valor de la ruleta: \033[39m", puntajeruleta2)
			sumapnts=sum(lisptjtotal)+puntajeruleta2
			print("Procesando...")
			time.sleep(1)
			print("\033[34mEsta es tu puntuación final: ", sumapnts,"\033[39m")
			listarpuntos.append(sumapnts)
		else:
			print("\033[34mEsta es tu puntuación final: ", sum(lisptjtotal),"\033[39m")
			listarpuntos.append(sum(lisptjtotal))		
	time.sleep(1.5) 

	
	def continuee2():
		global repe
		continuar=input("\033[31m¿Deseas volver a repetir la trivia?\033[39m Si/No\n").lower().strip();time.sleep(1)
		while continuar not in ("si","no"):
		   continuar=input("\033[33m¡Incorrecto! por favor, ingrese una respuesta válida:\033[39m Si/No\n").lower().strip();time.sleep(1.5)
		if continuar=="no":
			print("\nEste es el historial de los jugadores y sus puntuaciones:")
			for i in range(len(listarnombres)):
				print("\034[36mEl puntaje del jugador",listarnombres[i],"es",listarpuntos[i],"\033[39m")
			print("¡Gracias por jugar mi trivia!")
			print("El programa ha finalizado")
			repe=False		
		else:
			print("Procesando, espere por favor...")
			time.sleep(2)


	def continuee():
		global repe
		continuar=input("\033[31m¿Deseas volver a repetir la trivia?\033[39m Si/No...\nO tienes una opción para agregar tu propia pregunta, escribe 'pro' para acceder\n").lower().strip();time.sleep(1)
		while continuar not in ("si","no","pro"):
			continuar=input("\033[33m¡Incorrecto! por favor, ingrese una respuesta válida: \033[39mSi/No o 'pro'\n").lower().strip();time.sleep(1.5)
		if continuar=="no":
			print("\nEste es el historial de los jugadores y sus puntuaciones:")
			for i in range(len(listarnombres)):
				print("\033[34mEl puntaje del jugador",listarnombres[i],"es",listarpuntos[i],"\033[39m")
			print("¡Gracias por jugar mi trivia!")
			print("El programa ha finalizado")
			repe=False
			

		elif continuar=="pro":
			if len(lispregts) <= 2:
				print("Hola ",nombre,"a continuación puedes añadir tu pregunta, con sus respectivas respuestas: ");
				print("Recuerda que solo puedes agregar una sola pregunta")
				time.sleep(1)	
				preg=input("Ingresa la pregunta: ")
				input("\033[33mA continuación ingresarás tu respuesta correcta, seguida de las incorrectas: \033[39m\nPresiona enter para continuar ")
				respst1=input("Ingresa la respuesta correcta: ")
				respst2=input("Ingresa la respuesta incorrecta: ")
				respst3=input("Ingresa la respuesta incorrecta: ")
				respst4=input("Ingresa la respuesta incorrecta: ")
				lispregts.append(preg)
				lisres[0]=respst1
				lisres[1]=respst2	
				lisres[2]=respst3	
				lisres[3]=respst4		
				print("\033[32mPregunta Añadida\033[39m")
				continuee2()					
			else:
				print("Ya has añadido tu pregunta")
				editar=input("\033[31m¿Deseas editar tu pregunta?\033[39m Si/No\n").lower().strip()
				while editar not in ("si","no"):
					editar=input("\033[33m¡Incorrecto! responde solo \033[39mSi/No\n").lower().strip()
				if editar=="si":
					preg=input("Ingresa la nueva pregunta: ")
					input("\033[39mA continuación ingresarás tu respuesta correcta, seguida de las incorrectas: \033[39m\nPresiona enter para continuar ")				
					respst1=input("Ingresa la nueva respuesta correcta: ")
					respst2=input("Ingresa la nueva respuesta incorrecta: ")
					respst3=input("Ingresa la nueva respuesta incorrecta: ")
					respst4=input("Ingresa la nueva respuesta incorrecta: ")
					lispregts[2]=preg
					lisres[0]=respst1
					lisres[1]=respst2	
					lisres[2]=respst3	
					lisres[3]=respst4		
					print("\033[33mPregunta Editada\033[39m")
					continuee2()
				else:		
					continuee2()
		else:
			print("Procesando, espere por favor...\n")
			time.sleep(2)
	
	continuee()