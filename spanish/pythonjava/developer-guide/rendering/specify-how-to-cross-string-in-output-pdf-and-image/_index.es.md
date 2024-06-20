---
title: Especificar cómo cruzar cadenas en PDF de salida e imagen
type: docs
weight: 20
url: /es/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Especificar cómo cruzar cadenas en el PDF de salida e imagen**
Cuando una celda contiene texto o cadena que es más grande que el ancho de la celda, entonces la cadena se desborda si la siguiente celda en la siguiente columna es nula o vacía. Cuando guarde su archivo de Excel en PDF/Imagen, puede controlar este desbordamiento especificando el tipo de cruce mediante la enumeración [TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType). Tiene los siguientes valores

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): Mostrar como en MS Excel, depende de la siguiente celda. Si la siguiente celda es nula, la cadena se cruzará o se truncará.
- [TextCrossType. CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP) : Mostrar la cadena de manera similar a la exportación de PDF/Imagen de MS Excel
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE) : Mostrar todo el texto cruzando otras celdas y sobrescribir el texto de las celdas cruzadas
- [TextCrossType.STRICT_IN_CELL](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL) : Solo mostrar la cadena dentro del ancho de la celda.

El siguiente código de muestra carga el archivo de Excel de muestra y lo guarda en formato PDF/Imagen especificando diferentes tipos de TextCrossType. El archivo de Excel de muestra y los archivos de salida se pueden descargar desde los siguientes enlaces:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
