---
title: Formateo de marcadores inteligentes
type: docs
weight: 20
url: /es/java/formatting-smart-markers/
---

## **Atributo de estilo de copia**
A veces, al usar marcadores inteligentes, desea copiar el estilo de la celda que contiene las etiquetas de marcador inteligente. Puede utilizar el atributo CopyStyle de las etiquetas de marcador inteligente para este propósito.
### **Copia de estilos de celdas con marcadores inteligentes**
Este ejemplo utiliza un archivo de plantilla de Microsoft Excel simple con dos marcadores en las celdas A2 y B2. El marcador pegado en la celda B2 utiliza el atributo CopyStyle, mientras que el marcador en la celda A2 no lo hace. Aplique un formato simple (por ejemplo, configure el color de la fuente a **rojo** y configure el color de relleno de la celda a **amarillo**).

Este ejemplo utiliza un [archivo de plantilla](template1.xlsx) con algunos marcadores en las celdas. Al ejecutar el código, Aspose.Cells copia el formato a todos los registros en la columna B pero no conserva el formato en la columna A.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-UsingCopyStyleAttribute-1.java" >}}


## **Agregar etiquetas personalizadas**
### **Introducción**
Mientras se trabaja con la función de agrupación de datos de Smart Markers, a veces es necesario agregar sus propias etiquetas personalizadas a la fila de resumen. También se quiere concatenar el nombre de la columna con esa etiqueta, por ejemplo "Subtotal de Pedidos". Aspose.Cells le proporciona los atributos Label y LabelPosition, para que pueda colocar sus etiquetas personalizadas en los Smart Markers mientras se concatenan con las filas de subtotal en la agrupación de datos.
### **Agregar etiquetas personalizadas para concatenar con las filas de subtotal en Smart Markers**
Este ejemplo utiliza un [archivo de plantilla](template.xlsx) con algunos marcadores en las celdas. Al ejecutar el código, Aspose.Cells agrega algunas etiquetas personalizadas a las filas de resumen para los datos agrupados.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-AddCustomLabels-1.java" >}}
{{< app/cells/assistant language="java" >}}
