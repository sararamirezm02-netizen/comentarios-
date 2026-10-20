Parte 2

<img width="565" height="741" alt="image" src="https://github.com/user-attachments/assets/95265f27-b32e-4f58-8e82-8011a6cdced8" />

Preguntas de análisis

1. ¿Qué diferencia existe entre aplicar lower() y modificar directamente un carácter
de la cadena?
Las cadenas no se pueden cambiar una vez modificadas, lower() lo que hace es entregar una copia en minúscula de la original sin modificarla , en cambio si intentas cambiar directamente un carácter digamos frase[0] ="s", lo que haría Python es mostrar un error ya que las cadenas no permiten cambiar un caracter una vez creadas.
2. ¿Por qué split() devuelve una lista y no una tupla?
el split() en el ejercicio devuelve ["sara"] , una lista , porque las listas se pueden modificar y adaptar a cualquier cantidad de palabras de palabras , mientras que una tupla como ("sara") quedaria fija y no se podria cambiar despues.
3. ¿Qué resultado se obtiene con "Hola hola".lower().count("hola")?
  primero queda "hola hola" y luego cuenta cuantas veces aparece "hola" entonces el resultado es dos
4. ¿Qué ocurriría si se intentara ejecutar resumen[0] = 100?
Ocurriría un error de tipo TypeError, porque resumen es una tupla y sus elementos no se pueden modificar después de crearla. En este ejercicio, resumen[0] almacena la cantidad de caracteres de la frase.
5. ¿En qué situación del ejercicio sería más conveniente una lista que una tupla?
Sería más conveniente utilizar una lista si necesitáramos modificar los datos del resumen, por ejemplo, cambiar la cantidad de caracteres o actualizar la cantidad de palabras en cambio a diferencia de una tupla, una lista permite modificar sus elementos después de crearla.



Pruebas de la parte 3


<img width="806" height="806" alt="image" src="https://github.com/user-attachments/assets/be89199d-50f0-4ae1-94f3-5a01c0b779c4" />
<img width="629" height="189" alt="image" src="https://github.com/user-attachments/assets/5af287ad-e13f-48de-83db-41f17e511965" />
<img width="650" height="242" alt="image" src="https://github.com/user-attachments/assets/50a11d20-3c8c-464d-9fc1-a4b86a6e5cea" />
<img width="573" height="274" alt="image" src="https://github.com/user-attachments/assets/529e7053-94f6-47c9-a7a6-15ba82450422" />
<img width="573" height="274" alt="image" src="https://github.com/user-attachments/assets/dd315a2a-2467-4ecd-be68-5469c155c2b4" />
<img width="646" height="345" alt="image" src="https://github.com/user-attachments/assets/52b1a6e3-6206-4443-bc15-a7105abd5ada" />


Conclusión 
En el desarrollo de este proyecto, el uso combinado de cadenas, listas y tuplas permitió estructurar y procesar de manera correcta los comentarios de los usuarios. Las cadenas de texto (str) fueron fundamentales para la lectura de los datos mediante métodos como strip(), lower() y split(), las listas proporcionaron lo necesario para almacenar y modificar la colección de comentarios a medida que el usuario los registraba y las tuplas jugaron un papel clave al guardar de forma segura y fija los datos de resumen de cada comentario (número de caracteres, palabras y apariciones), garantizando su inmutabilidad frente a modificaciones accidentales.






