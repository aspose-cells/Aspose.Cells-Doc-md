---
title: Importación y colocación inteligente de datos con marcadores inteligentes en Python a través de .Net
linktitle: Marcadores inteligentes
type: docs
weight: 190
url: /es/python-net/using-smart-markers/
description: Importación y colocación inteligente de datos según la plantilla de archivos de Excel con Aspose.Cells para Python a través de la biblioteca .Net.
---
## **Introducción**
**Marcadores inteligentes**se utilizan para que Aspose.Cells sepa qué información colocar en una hoja de cálculo de Microsoft diseñador de Excel. Los marcadores inteligentes le permiten crear plantillas que contienen solo información y formato específicos.
## **Diseñador de hojas de cálculo y marcadores inteligentes**
Las hojas de cálculo de Designer son archivos estándar de Excel que contienen formato visual, fórmulas y marcadores inteligentes. Pueden contener marcadores inteligentes que hacen referencia a una o más fuentes de datos, como información de un proyecto e información de contactos relacionados. Los marcadores inteligentes se escriben en las celdas donde desea la información.

 Todos los marcadores inteligentes comienzan con &=. Un ejemplo de marcador de datos es &=Party.FullName. Si el marcador de datos da como resultado más de un elemento, por ejemplo, una fila completa, las siguientes filas se mueven hacia abajo automáticamente para dejar espacio para la nueva información. Por lo tanto, los subtotales y los totales se pueden colocar en la fila inmediatamente después del marcador de datos para realizar cálculos basados en los datos insertados. Para hacer cálculos en las filas insertadas, use**fórmulas dinámicas**.

 Los marcadores inteligentes consisten en la**fuente de datos** y**nombre del campo**piezas para la mayoría de la información. También se puede pasar información especial con variables y matrices de variables. Las variables siempre llenan solo una celda, mientras que las matrices de variables pueden llenar varias. Solo use un marcador de datos por celda. Los marcadores inteligentes no utilizados se eliminan.

El marcador inteligente también puede contener parámetros. Los parámetros le permiten modificar cómo se presenta la información. Se agregan al final del marcador inteligente entre paréntesis como una lista separada por comas.
### **Opciones de marcador inteligente**
 &=FuenteDeDatos.NombreDeCampo
 &=[Fuente de datos].[Nombre de campo]&=$Nombre de variable
 &=$VariableArray
 &==Fórmula dinámica
&=&=Fórmula dinámica repetida
### **Parámetros**
Se permiten los siguientes parámetros:

- **no agregar** - No agregue filas adicionales para ajustar los datos.
- **saltar: n** - Saltar n número de filas para cada fila de datos.
- **ascendente:n** o**descendente:n** - Ordenar datos en marcadores inteligentes. Si n es 1, entonces la columna es la primera clave del clasificador. Los datos se ordenan después de procesar la fuente de datos. Por ejemplo: &=Tabla1.Campo3(ascendente:1).
- **horizontal** - Escriba los datos de izquierda a derecha, en lugar de arriba a abajo.
- **numérico** - Convertir texto a número si es posible.
- **cambio** - Desplace hacia abajo o hacia la derecha, creando filas o columnas adicionales para ajustar los datos. El parámetro shift funciona de la misma manera que en Microsoft Excel. Por ejemplo, en Microsoft Excel, cuando selecciona un rango de celdas, haga clic con el botón derecho y seleccione**Insertar** y especificar?**cambiar las celdas hacia abajo**, **desplazar celdas a la derecha** y otras opciones. En resumen, el**cambio** El parámetro cumple la misma función para marcadores inteligentes verticales/normales (de arriba a abajo) u horizontales (de izquierda a derecha).
- **estilo de copia** - Copie el estilo de la celda base a todas las celdas de esa columna.

Los parámetros noadd y skip se pueden combinar para insertar datos en filas alternas. Debido a que la plantilla se procesa de abajo hacia arriba, debe agregar noadd en la primera fila para evitar que se inserten filas adicionales antes de la fila alternativa.

Si tiene varios parámetros, sepárelos con comas, pero sin espacios: parámetroA, parámetroB, parámetroC

Las siguientes capturas de pantalla muestran cómo insertar datos en filas alternas.

|**Archivo de plantilla**|**Archivo de salida**|
|:- |:- |
|![todo:imagen_alternativa_texto](using-smart-markers_1.jpg)|![todo:imagen_alternativa_texto](using-smart-markers_2.jpg)|
### **Fórmulas dinámicas**
Las fórmulas dinámicas le permiten insertar fórmulas de Excel en celdas incluso cuando la fórmula hace referencia a filas que se insertarán durante el proceso de exportación. Las fórmulas dinámicas pueden repetirse para cada fila insertada o usar solo la celda donde se coloca el marcador de datos.

Las fórmulas dinámicas permiten las siguientes opciones adicionales:

- r - Número de fila actual.
- 2, -1 - Desplazamiento al número de fila actual.

Por ejemplo:

{{< highlight "java" >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

En el marcador de fórmula dinámica, "-1" indica el desplazamiento de la fila actual en las columnas B y C, respectivamente, que se configurará para la operación de división, el parámetro de omisión es una fila. Además, debemos especificar el siguiente carácter:

{{< highlight "java" >}}

 "~"

{{< /highlight >}}

como carácter separador para aplicar más parámetros en fórmulas dinámicas.

Las siguientes capturas de pantalla ilustran una fórmula dinámica repetitiva y la hoja de cálculo de Excel resultante.

|**Archivo de plantilla**|**Archivo de salida**|
|:- |:- |
|![todo:imagen_alternativa_texto](using-smart-markers_3.jpg)|![todo:imagen_alternativa_texto](using-smart-markers_4.jpg)|
 Cell "C1" contiene la fórmula**= A1*B1** , la celda "C2" contiene**= A2*B2** y la celda "C3" contiene**= A3*B3**.

Es muy fácil procesar los marcadores inteligentes. Lo que sigue es un fragmento de código en Python a través de .Net, que muestra cómo se hace.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "SmartMarker-SimpleProcess.py" >}}


