---
title: Especificar cómo cruzar cadenas en PDF de salida e imagen
type: docs
weight: 120
url: /es/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: Aprenda cómo cruzar cadenas en el PDF de salida e imagen con Aspose.Cells para Python via .NET API.
keywords: Python Cruza Cadena en PDF de salida e imagen
---

## **Escenarios de uso posibles**

Cuando una celda contiene texto o una cadena pero es más grande que el ancho de la celda, entonces la cadena desborda si la siguiente celda en la siguiente columna es nula o vacía. Al guardar tu archivo de Excel en PDF/Imagen, puedes controlar este desbordamiento especificando el tipo de cruce utilizando la enumeración [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/). Tiene los siguientes valores

- **TextCrossType.DEFAULT**: Muestra el texto como en MS Excel que depende de la siguiente celda. Si la siguiente celda es nula, la cadena se cruzará o se truncará.

- **TextCrossType.CROSS_KEEP**: Muestra la cadena como en MS Excel exportando PDF/Imagen

- **TextCrossType.CROSS_OVERRIDE**: Muestra todo el texto cruzando otras celdas y sobrescribiendo el texto de las celdas cruzadas

- **TextCrossType.STRICT_IN_CELL**: Solo muestra la cadena dentro del ancho de la celda.

## **Especifica cómo cruzar la cadena en el PDF/Imagen de salida utilizando TextCrossType**

El siguiente código de ejemplo carga el archivo de Excel de ejemplo y lo guarda en formato PDF/Imagen especificando diferentes [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/). El archivo de Excel de ejemplo y los archivos de salida se pueden descargar desde los siguientes enlaces

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Código de Ejemplo

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
