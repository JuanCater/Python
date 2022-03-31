texto = """ 
Un domingo por la mañana José María estaba 
muy enojado porque su mamá le dijo que tenía que ir con ella al 
mercado que estaba en el centro de la ciudad.
Él nunca había ido a un mercado, sólo sabía que a ese lugar iba mucha gente.
Al llegar al mercado quedó sorprendido, nunca se imaginó lo que estaba viendo. 
"""

texto = texto.lower().split()
print (texto)
letra = input("Ingrese una letra: ")
for palabra in texto:
    if palabra.startswith(letra):
        print (palabra)
        


