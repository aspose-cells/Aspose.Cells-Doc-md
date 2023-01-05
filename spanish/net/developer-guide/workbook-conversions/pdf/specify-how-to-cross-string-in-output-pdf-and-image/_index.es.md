---
title: Especifique cómo cruzar la cadena en la salida PDF y la imagen
type: docs
weight: 120
url: /es/net/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Posibles escenarios de uso**

Cuando una celda contiene texto o una cadena pero es más grande que el ancho de la celda, la cadena se desborda si la siguiente celda en la siguiente columna es nula o está vacía. Cuando guarda su archivo de Excel en PDF/Imagen, puede controlar este desbordamiento especificando el tipo de cruz usando el[**Tipo de cruz de texto**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)enumeración. tiene los siguientes valores

- **TextCrossType.Predeterminado**: muestra texto como MS Excel que depende de la siguiente celda. Si la siguiente celda es nula, la cadena se cruzará o se truncará.

- **TextCrossType.CrossKeep**: Muestra la cadena como MS Excel exportando PDF/Imagen

- **TextCrossType.CrossOverride**: muestra todo el texto cruzando otras celdas y anula el texto de las celdas cruzadas

- **TextCrossType.StrictInCell**: solo muestra la cadena dentro del ancho de la celda.

## **Especifique cómo cruzar una cadena en la salida PDF/Imagen usando TextCrossType**

El siguiente código de muestra carga el archivo de muestra de Excel y lo guarda en el formato PDF/Imagen especificando diferentes[**Tipo de cruz de texto**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype). El archivo de muestra de Excel y los archivos de salida se pueden descargar desde los siguientes enlaces:

[ejemploCrossType.xlsx](81920905.xlsx)

[salidaCrossType.pdf](81920903.pdf)

[salidaCrossType.png](81920904.png)

### Código de muestra

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
