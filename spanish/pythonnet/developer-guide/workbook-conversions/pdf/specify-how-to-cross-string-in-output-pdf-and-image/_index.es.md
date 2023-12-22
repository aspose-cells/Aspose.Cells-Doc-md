---
title: Especifique cómo cruzar la cadena en la salida PDF y la imagen
type: docs
weight: 120
url: /es/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: Aprenda a cruzar cadenas en la salida PDF y la imagen con Aspose.Cells for Python via .NET API.
keywords: Python Cross String in output PDF and image
---
##  **Posibles escenarios de uso**

Cuando una celda contiene texto o una cadena pero es más grande que el ancho de la celda, la cadena se desborda si la siguiente celda de la siguiente columna es nula o está vacía. Cuando guarda su archivo de Excel en PDF/Imagen, puede controlar este desbordamiento especificando el tipo de cruz usando el[**TextoCruzTipo**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)enumeración. Tiene los siguientes valores

- *TextCrossType.DEFAULT**: muestra texto como MS Excel que depende de la siguiente celda. Si la siguiente celda es nula, la cadena se cruzará o se truncará.

- *TextCrossType.CROSS_KEEP**: Muestra la cadena como MS Excel exportando PDF/Imagen

- *TextCrossType.CROSS_OVERRIDE**: muestra todo el texto cruzando otras celdas y anula el texto de las celdas cruzadas

- *TextCrossType.STRICT_IN_CELL**: solo muestra la cadena dentro del ancho de la celda.

##  **Especifique cómo cruzar una cadena en la salida PDF/Imagen usando TextCrossType**

El siguiente código de muestra carga el archivo Excel de muestra y lo guarda en formato PDF/Imagen especificando diferentes[**TextoCruzTipo**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)El archivo de Excel de muestra y los archivos de salida se pueden descargar desde los siguientes enlaces:

[muestraCrossType.xlsx](81920905.xlsx)

[salidaCrossType.pdf](81920903.pdf)

[salidaCrossType.png](81920904.png)

###  Código de muestra

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
