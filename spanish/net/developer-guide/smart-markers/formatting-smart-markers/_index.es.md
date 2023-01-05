---
title: Dar formato a marcadores inteligentes
type: docs
weight: 20
url: /es/net/formatting-smart-markers/
---
## **Copiar atributo de estilo**
A veces, cuando usa marcadores inteligentes, desea copiar el estilo de la celda que contiene las etiquetas de marcador inteligente. Puede usar el atributo CopyStyle de las etiquetas del marcador inteligente para este propósito.
### **Copia de estilos de Cells con marcadores inteligentes**
 Este ejemplo utiliza un archivo Excel de plantilla simple Microsoft con dos marcadores en las celdas A2 y B2. El marcador pegado en la celda B2 usa el atributo CopyStyle, mientras que el marcador en la celda A2 no. Aplique un formato simple (por ejemplo, establezca el color de la fuente en**rojo** y establezca el color de relleno de la celda en**amarillo**).

Al ejecutar el código, Aspose.Cells copia el formato a todos los registros de la columna B pero no conserva el formato de la columna A.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingCopyStyleAttribute-1.cs" >}}
## **Adición de etiquetas personalizadas**
### **Introducción**
Mientras trabaja con la función de datos de agrupación de Smart Markers, a veces necesita agregar sus propias etiquetas personalizadas a la fila de resumen. También desea concatenar el nombre de la columna con esa etiqueta, por ejemplo, "Subtotal de pedidos". Aspose.Cells le proporciona atributos de etiqueta y posición de etiqueta, por lo que puede colocar sus etiquetas personalizadas en los marcadores inteligentes mientras se concatena con las filas de subtotal en los datos de agrupación.
### **Adición de etiquetas personalizadas para concatenar con las filas de subtotal en marcadores inteligentes**
Este ejemplo utiliza un[archivo de datos](96927971.xlsx) y un[archivo de plantilla](96927972.xlsx) con algunos marcadores en las células. Al ejecutar el código, Aspose.Cells agrega algunas etiquetas personalizadas a las filas de resumen de los datos agrupados.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AddCustomLabels-1.cs" >}}
