# SEGURIDAD
# PRÁCTICA 1
## ALUMNO: Jhon Ismael Flores Pacheco
### CONCLUSIONES
1. Es un procedimiento que se aplica antes de usar el código de cifrado del texto plano, con la finalidad de que este último este listo para poder cifrarse
2. Existen varias técnicas para realizar el preprocesamiento.
3. Una de las técnicas usadas es la sustitución del alfabeto, es decir, intercambiar algunos caracteres por otros, esta técnica es aparentemente la más sencilla, su implementación no resulta complicada en la mayoría de los casos.
4. Otra técnica denominada reemplazo numérico, es la que aparentemente resulta más "segura" puesto que podría cambiar de forma total el texto plano, y la dificultad de su implemntación dependerá del lenguaje de programación usado.
5. El preprocesamiento es un paso muy importante antes de realizar el cifrado, porque permite que este último tenga una mayor solidez, o sea más resistente a ataques.
6. Podríamos considerar que el procesamiento es un proceso de "adaptación" del texto plano para realizar el cifrado.
7. Otra técnica usada en preprocesamiento es la eliminación de signos de puntuación y espacios en blanco, pareciera que no tienen mucha importancia, sin embargo, esta técnica ayuda mucho en el proceso de cifrado, sobretodo por la eliminación de espacios en blanco que hacen que el texto plano se convierta en una sola "palabra" que permite una mayor facilidad en el proceso de cifrado.
8. En general, la implementación de la mayoría de técnicas para realizar el preprocesamiento no generan mucha dificultad, siempre y cuanado se disponga del tiempo y paciencia necesarios. 

### CUESTIONARIO FINAL

#### 1. Describa los siguientes términos
* Protección y seguridad de datos: Como el mismo nombre lo indica es la protección de la privacidad digital, y que se aplica para evitar el acceso no autorizado a los datos almacenados.
* Criptografía: Conjunto de técnicas que permiten modificar o alterar mensajes o archivos con el objetivo de "ocultar" el mensaje y que no puedan ser leídos por personas ajenas.
* Seguridad y fortificación de redes: Es la capacidad de brindar seguridad y organizar de forma adecuada las redes que se usan, puede ser deuna empresa, institución, etc.
* Seguridad en aplicaciones informáticas, programas y bases de datos: Son las medidas de seguridad que se implementan a nivel de la aplicación o programa desarrollado, y también a nivel de la base de datos utilizada
* Gestión de seguridad en equipos y sistemas informáticos: Capacidad de garantizar la confidencialidad, integración y disponibilidad del sistema informático, así como el uso adecuado y seguro de los equipos que intervienen.
* Informática forense: Es el proceso de capturar, identificar, extraer y documentar una evidencia digital para su uso posterior en una demanda.
* Ciberdelito, ciberseguridad: El ciberdelito o delito informático es todo aquel acto ilegal realizado por un ciberdelincuente en el espacio digital a través de las redes informáticas y diversos dispositivos electrónicos, la ciberseguridad es el campo de la tecnología de la información asociado con la seguridad de los sistemas informáticos y la protección de datos, y en contra de ataques maliciosos o ataques informáticos en el mundo digital.
### 2. Describa los siguientes términos
* Gestión de la seguridad de la información: Un SGSI es un enfoque sistemático que permite establecer, implementar, operar, monitorear, revisar, mantener y mejorar la seguridad de la información de una organización
* Asesoría y auditoría de seguridad:  Permiten establecer soluciones para cada necesidad mediante un proceso de consultoría donde se pueda analizar toda la información relativa a los riesgos, amenazas y vulnerabilidades que puedan existir, con el fin de realizar un diagnóstico, y proponer un tratamiento y solución adecuado.
* Análisis y gestión de riesgos: El análisis de riesgos se compone de una serie de medidas que se deben tomar para prevenir la aparición, o incluso permitir la eliminación de estos peligros. Y la gestión de riesgos es un conjunto de procesos específicos y definidos con el fin de hacer todo lo posible para que no se produzcan los riesgos indicados.
* Continuidad de negocios: Es un conjunto de procedimientos y medidas que adopta una empresa o institución para garantizar que las funciones esenciales puedan continuar durante y después de cualquier incidente y que su operación no se vea afectada.
* Buen gobierno: Forma de ejercicio del poder caracterizada por rasgos como la eficiencia, la transparencia, la rendición de cuentas, la participación de los involucrados, que revela la determinación del gobierno de utilizar los recursos disponibles a favor del desarrollo económico y social.
* Comercio electrónico: Consiste en el marketing y venta de productos o servicios a través de Internet.
* Legislación relacionada con seguridad: Disposiciones que se otorgan en materia legal con respecto a la seguridad.
### 3. Describa alguna otra operación o función de preprocesamiento que se implemente sobre el texto claro en los criptosistemas, en que afecta la complejidad de estas funciones al desempeño del mismo
* Tokenización: La tokenización es un paso que divide cadenas de texto más largas en piezas más pequeñas o tokens. Los trozos de texto más grandes pueden ser convertidos en oraciones, las oraciones pueden ser tokenizadas en palabras, etc. El procesamiento adicional generalmente se realiza después de que una pieza de texto ha sido apropiadamente concatenada. La tokenización también se conoce como segmentación de texto o análisis léxico. A veces la segmentación se usa para referirse al desglose de un gran trozo de texto en partes más grandes que las palabras (por ejemplo, párrafos u oraciones), mientras que la tokenización se reserva para el proceso de desglose que se produce exclusivamente en palabras. Mientras más complejas sean las funciones de preprocesamiento, se utilizarán más recursos para poder desarrollar el preprocesado, pero del mismo modo, el cifrado será más seguro.
### 4. Describa la máquina enigma, luego muestre usando un simulador en internet la encriptación de la frase QUERIDA HIJA, para tres posiciones distintas de los rotores
La máquina Enigma utilizada por la mayor parte de las comunicaciones alemanas durante la guerra tenía un funcionamiento complejo. Se basaba en cinco rotores que variaban cada vez que se pulsaba una tecla, de manera que cada letra del alfabeto ofrecía un número altísimo de posibilidades. El Ejército alemán complicaba más las cosas cambiando la posición de los rotores una vez al mes. Los mandos alemanes de la época veían a Enigma como indescifrable. Esta máquina se conocía dentro de  la Fuerza como “Eins” (modelo uno) o “Wermarcht Enigma” (modelo W) y entró en servicio el 1 de Junio  de 1930. Era capaz de “mezclar” el texto de los mensajes de  200 quintillones de formas diferentes. Y  con la  clave correcta, volverlo a la normalidad. Se transformó rápidamente en el  código secreto indescifrable de las Fuerzas Armadas. O al  menos eso creían los alemanes. La clave del Enigma queda determinada por la  estructura interna de los rotores y por su posición inicial. Los  rotores podían ser de nueve tipos distintos, en los modelos empleados por el ejército alemán, y de cuatro tipos en  los modelos utilizados por la marina,  tenían que  sustituirse  con frecuencia  para evitar que los criptoanalistas enemigos consiguieran alguna pista.

![img](images/ENIGMA1.png)
![img](images/ENIGMA2.png)
![img](images/ENIGMA3.png)


### 5. Describa la aplicación de Unicode-8
UTF-8 es una codificación de caracteres de 8 bits para Unicode. La abreviatura “UTF-8” procede de “8-bit Unicode Transformation Format”, en español, formato de transformación Unicode de 8 bits. Se crea un número binario legible por ordenador que consta de uno a cuatro bytes, cada uno de los cuales está formado por ocho bits. Esta codificación se asigna a un carácter o a otro elemento textual. La estructura autosincronizada y la capacidad de generar 221 números binarios permite asignar de manera inconfundible todos y cada uno de los elementos lingüísticos y textuales de todos los idiomas del mundo.

