---
title: Lista de fórmulas
type: docs
weight: 10
url: /es/reportingservices/formula-list/
---
**Campos de informe**

|**Escoger un nombre** |**Nombre de fórmula**|**Descripción**|
|:- |:- |:- |
| Campos globales| Tiempo de ejecución| La fecha y la hora en que comenzó a ejecutarse el informe.|
|| URL del servidor de informes| La URL del servidor de informes en el que se está ejecutando el informe.|
|| Reportar nombre| El nombre del informe tal como está almacenado en la base de datos del servidor de informes.|
|| InformeCarpeta| La ruta completa a la carpeta que contiene el informe. Esto no incluye la URL del servidor de informes.|
| Usuario| ID de usuario| El ID del usuario que ejecuta el informe.|
|| Idioma| El ID de idioma del usuario que ejecuta el informe.|
**Campos de informe**

|**Escoger un nombre**|**Descripción**|
|:- |:- |
| Parámetros| La colección Parámetros contiene los parámetros del informe dentro del informe. Los parámetros se pueden pasar a consultas, usarse en filtros o en otras funciones que alteran la apariencia del informe según el parámetro.|
| Campos| La colección Fields contiene los campos dentro del conjunto de datos actual.|
| conjunto de datos||
**Operadores**
Los operadores aritméticos se utilizan para combinar números, variables numéricas, campos numéricos y funciones numéricas para obtener otro número. Los operadores de comparación generalmente se usan para comparar operandos para una condición en una estructura de control como una instrucción If. Los operadores booleanos se utilizan normalmente con operadores de comparación para generar condiciones para estructuras de control.

|**Escoger un nombre**|**Nombre de la fórmula**|**Descripción**|
|:- |:- |:- |
| Aritmética|^ | Exponenciación, por ejemplo 2^3.|
||* | Multiplicación, por ejemplo 2*3.|
||/ | División, por ejemplo 2/3.|
||\\\ | División entera, por ejemplo 2\\\3.|
|| Modificación| Módulo, por ejemplo 4 Mod 3.|
||+ | Adición, por ejemplo 4 + 3.|
||- | Resta, por ejemplo 4 – 3.|
| Comparación|< | Menos que, por ejemplo 4< 3 false. |
||<= | Menor o igual, por ejemplo 4<= 3 false. |
||> | Mayor que, por ejemplo 4 > 3 verdadero.|
||>= | Mayor o igual, por ejemplo 4 >= 3 verdadero.|
||= | Igual, por ejemplo 4 = 3 falso.|
||<> | No es igual, por ejemplo 4<> 3 cierto.|
|| Me gusta|Compara una cadena con un patrón. Por ejemplo resultado = cadena Como patrón.|
|| Es| Compara dos variables de referencia de objeto, por ejemplo, asp Is aspose.|
| Concatenación|& | Genera una concatenación de cadenas de dos expresiones.|
||+ | Suma dos números o devuelve el valor positivo de una expresión numérica. También se puede utilizar para concatenar dos expresiones de cadena.|
| Lógico/bit a bit| Y| Realiza una conjunción lógica en dos expresiones booleanas o una conjunción bit a bit en dos expresiones numéricas.|
|| No| Realiza la negación lógica en una expresión booleana o la negación bit a bit en una expresión numérica.|
|| O| Realiza una disyunción lógica en dos expresiones booleanas o una disyunción bit a bit en dos expresiones numéricas.|
|| xor| Realiza una exclusión lógica en dos expresiones booleanas o una exclusión bit a bit en dos expresiones numéricas.|
|| Y también| Realiza una conjunción lógica de cortocircuito en dos expresiones.|
|| Si no|Realiza la disyunción lógica inclusiva de cortocircuito en dos expresiones.|
| Cambio de bits|>> | Realiza un desplazamiento aritmético a la izquierda en un patrón de bits.|
||<< | Realiza un desplazamiento aritmético a la derecha en un patrón de bits.|

