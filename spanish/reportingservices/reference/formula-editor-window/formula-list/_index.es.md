---
title: Lista de Fórmulas
type: docs
weight: 10
url: /es/reportingservices/formula-list/
---

**Campos del informe**

|**Nombre del conjunto**|**Nombre de la fórmula**|**Descripción**|
| :- | :- | :- |
|Campos globales|ExecutionTime|La fecha y hora en que el informe comenzó a ejecutarse. |
| |ReportServerUrl|La URL del servidor de informes en el que se está ejecutando el informe. |
| |ReportName|El nombre del informe tal como se almacena en la base de datos del servidor de informes. |
| |ReportFolder|La ruta completa a la carpeta que contiene el informe. Esto no incluye la URL del servidor de informes. |
|Usuario|UserID|El ID del usuario que ejecuta el informe. |
| |Language|El ID de idioma del usuario que ejecuta el informe. |
**Campos del informe**

|**Nombre del conjunto**|**Descripción**|
| :- | :- |
|Parameters |La colección de parámetros contiene los parámetros del informe dentro del informe. Los parámetros se pueden pasar a consultas, usar en filtros o en otras funciones que alteren la apariencia del informe según el parámetro. |
|Campos|La colección de campos contiene los campos dentro del conjunto de datos actual. |
|Conjunto de datos| |
**Operadores**
Los operadores aritméticos se utilizan para combinar números, variables numéricas, campos numéricos y funciones numéricas para obtener otro número. Los operadores de comparación se utilizan generalmente para comparar operandos para una condición en una estructura de control como una declaración If. Los operadores booleanos se utilizan típicamente con operadores de comparación para generar condiciones para estructuras de control.

|**Nombre del conjunto**|**Nombre de la fórmula**|**Descripción**|
| :- | :- | :- |
|Aritmética|^|Exponenciación, por ejemplo 2^3. |
| |*|Multiplicación, por ejemplo 2*3. |
| |/|División, por ejemplo 2/3. |
| |\\\|División entera, por ejemplo 2\\\3. |
| |Mod|Módulo, por ejemplo 4 Mod 3. |
| |+ |Adición, por ejemplo 4 + 3. |
| |- |Resta, por ejemplo 4 - 3. |
|Comparación |< |Menor que, por ejemplo 4 < 3 falso. |
| |<= |Menor o igual, por ejemplo 4 <= 3 falso. |
| |> |Mayor que, por ejemplo 4 > 3 verdadero. |
| |>= |Mayor o igual, por ejemplo 4 >= 3 verdadero. |
| |= |Igual, por ejemplo 4 = 3 falso. |
| |<> |No igual, por ejemplo 4 <> 3 verdadero. |
| |Like |Compara una cadena con un patrón. Por ejemplo resultado = cadena Like patrón. |
| |Is |Compara dos variables de referencia de objeto, por ejemplo asp Is aspose. |
|Concatenación |& |Genera una concatenación de cadena de dos expresiones. |
| |+ |Agrega dos números o devuelve el valor positivo de una expresión numérica. También se puede usar para concatenar dos expresiones de cadena. |
|Lógico/Bit a bit |Y |Realiza una conjunción lógica en dos expresiones booleanas, o una conjunción bit a bit en dos expresiones numéricas. |
| |Not |Realiza la negación lógica en una expresión booleana, o la negación bit a bit en una expresión numérica. |
| |Or |Realiza una disyunción lógica en dos expresiones booleanas, o una disyunción bit a bit en dos expresiones numéricas. |
| |Xor |Realiza una exclusión lógica en dos expresiones booleanas, o una exclusión bit a bit en dos expresiones numéricas. |
| |Y además |Realiza una conjunción lógica de cortocircuito en dos expresiones. |
| |O también |Realiza una disyunción lógica inclusiva de cortocircuito en dos expresiones. |
|Desplazamiento de bits |>> |Realiza un desplazamiento aritmético a la izquierda en un patrón de bits. |
| |<< |Realiza un desplazamiento aritmético a la derecha en un patrón de bits. |

