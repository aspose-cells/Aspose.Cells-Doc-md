---
title: Especifique cómo cruzar la cadena en la salida PDF y la imagen
type: docs
weight: 20
url: /es/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Especifique cómo cruzar la cadena en la salida PDF y la imagen**
 Cuando una celda contiene texto o una cadena que es más grande que el ancho de la celda, la cadena se desborda si la siguiente celda en la siguiente columna es nula o está vacía. Cuando guarda su archivo de Excel en PDF/Imagen, puede controlar este desbordamiento especificando el tipo cruzado usando el[Tipo de cruz de texto](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType) enumeración. tiene los siguientes valores

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): Mostrar como MS Excel, depende de la siguiente celda. Si la siguiente celda es nula, la cadena se cruzará o se truncará.
- [Tipo de cruz de texto. CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP): Muestra la cadena similar a MS Excel exportando PDF/Imagen
- [TextoCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE)muestra todo el texto cruzando otras celdas y anula el texto de las celdas cruzadas
- [TextCrossType.ESTRICTO_EN_CELDA](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL): solo muestra la cadena dentro del ancho de la celda.

El siguiente código de muestra carga el archivo de muestra de Excel y lo guarda en el formato PDF/Image al especificar diferentes TextCrossType. El archivo de muestra de Excel y los archivos de salida se pueden descargar desde los siguientes enlaces:

[ejemploCrossType.xlsx](sampleCrossType.xlsx)

[salidaCrossType.pdf](outputCrossType.pdf)

[salidaCrossType.png](outputCrossType.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
