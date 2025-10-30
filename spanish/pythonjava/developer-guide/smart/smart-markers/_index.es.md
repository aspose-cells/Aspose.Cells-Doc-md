---
title: Importación y colocación inteligente de datos con marcadores inteligentes en Python mediante java
linktitle: Marcadores inteligentes
type: docs
weight: 10
url: /es/python-java/using-smart-markers/
description: Importación y colocación inteligente de datos de acuerdo con los archivos de plantilla de Excel con Aspose.Cells para la biblioteca de Python mediante java.
---

## **Introducción**
**Los marcadores inteligentes** se utilizan para informar a Aspose.Cells qué información colocar en una hoja de cálculo de Microsoft Excel diseñada. Los marcadores inteligentes le permiten crear plantillas que contienen solo información y formato específicos.
## **Hoja de cálculo de diseño y Marcadores inteligentes**
Las hojas de cálculo de diseño son archivos Excel estándar que contienen formato visual, fórmulas y marcadores inteligentes. Pueden contener marcadores inteligentes que hacen referencia a una o más fuentes de datos, como información de un proyecto e información de contactos relacionados. Los marcadores inteligentes se escriben en las celdas donde desea la información.

Todos los marcadores inteligentes comienzan con &=. Un ejemplo de marcador de datos es &=Party.FullName. Si el marcador de datos da como resultado más de un elemento, por ejemplo, una fila completa, entonces las filas siguientes se mueven automáticamente para dar cabida a la nueva información. De esta manera, los subtotales y totales pueden colocarse en la fila inmediatamente después del marcador de datos para realizar cálculos basados en la información insertada. Para realizar cálculos en las filas insertadas, utilice **formulas dinámicas**.

Los marcadores inteligentes consisten en las partes de **fuente de datos** y **nombre del campo** para la mayoría de la información. También se puede enviar información especial con variables y matrices de variables. Las variables siempre llenan solo una celda, mientras que las matrices de variables pueden llenar varias. Utilice solo un marcador de datos por celda. Los marcadores inteligentes no utilizados se eliminan.

El marcador inteligente también puede contener parámetros. Los parámetros le permiten modificar la disposición de la información. Se agregan al final del marcador inteligente entre paréntesis como una lista separada por comas.
### **Opciones de Marcador Inteligente**
&=DataSource.FieldName 
&=[Data Source].[Field Name] 
&=$VariableName 
&=$VariableArray 
&==DynamicFormula 
&=&=RepeatDynamicFormula
### **Parámetros**
Se permiten los siguientes parámetros:

- **noadd** - No agregar filas adicionales para ajustar los datos.
- **skip:n** - Omitir n filas por cada fila de datos.
- **ascending:n** o **descending:n** - Ordenar datos en marcadores inteligentes. Si n es 1, entonces la columna es la primera clave del ordenador. Los datos se ordenan después de procesar la fuente de datos. Por ejemplo: &=Tabla1.Campo3(ascending:1).
- **horizontal** - Escribir datos de izquierda a derecha, en lugar de arriba a abajo.
- **numérico** - Convertir texto a número si es posible.
- **shift** - Desplazar hacia abajo o a la derecha, creando filas o columnas adicionales para ajustar los datos. El parámetro de desplazamiento funciona de la misma manera que en Microsoft Excel. Por ejemplo, en Microsoft Excel, al seleccionar un rango de celdas, haga clic derecho y seleccione **Insertar** y especifique **desplazar celdas hacia abajo**, **desplazar celdas hacia la derecha** y otras opciones. En resumen, el parámetro **shift** cumple la misma función para marcadores inteligentes verticales/normales (de arriba a abajo) o horizontales (de izquierda a derecha).
- **copiarEstilo** - Copiar el estilo de la celda base a todas las celdas de esa columna.

Los parámetros noadd y skip se pueden combinar para insertar datos en filas alternas. Debido a que la plantilla se procesa de abajo hacia arriba, debe agregar noadd en la primera fila para evitar que se inserten filas adicionales antes de la fila alternativa.

Si tiene múltiples parámetros, sepárelos con comas, pero sin espacio: parámetroA,parámetroB,parámetroC

Las siguientes capturas de pantalla muestran cómo insertar datos en cada otra fila.

|**Archivo de plantilla**|**Archivo de salida**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|
### **Fórmulas dinámicas**
Las fórmulas dinámicas te permiten insertar fórmulas de Excel en celdas incluso cuando la fórmula hace referencia a filas que se insertarán durante el proceso de exportación. Las fórmulas dinámicas pueden repetirse para cada fila insertada o usar solo la celda donde se coloca el marcador de datos.

Las fórmulas dinámicas permiten las siguientes opciones adicionales:

- r - Número de fila actual.
- 2, -1 - Desplazamiento al número de fila actual.

Por ejemplo:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

En el marcador de fórmula dinámica, "-1" denota el desplazamiento a la fila actual en las columnas B y C respectivamente que se establecerá para la operación de división, el parámetro de omisión es una fila. Además, deberíamos especificar el siguiente carácter:

{{< highlight java >}}

 "~"

{{< /highlight >}}

como un carácter separador para aplicar más parámetros en las fórmulas dinámicas.

Las siguientes capturas de pantalla ilustran una fórmula dinámica y repetitiva y la hoja de cálculo de Excel resultante.

|**Archivo de plantilla**|**Archivo de salida**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
La celda "C1" contiene la fórmula **= A1*B1**, la celda "C2" contiene **= A2*B2** y la celda "C3" contiene **= A3*B3**.

Es muy fácil procesar los marcadores inteligentes. A continuación se muestra un fragmento de código en Python via Java, que muestra cómo se hace.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "SmartMarker-SimpleProcess.py" >}}


