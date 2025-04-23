---
title: Especificar cómo cruzar cadenas en PDF de salida e imagen
type: docs
weight: 110
url: /es/java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Escenarios de uso posibles**

Cuando una celda contiene texto o cadena pero es más grande que el ancho de la celda, entonces la cadena se desborda si la siguiente celda en la siguiente columna está vacía. Al guardar su archivo de Excel en PDF/Imagen, puede controlar este desbordamiento especificando el tipo de cruce utilizando la enumeración [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). Tiene los siguientes valores

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): Mostrar como en MS Excel, depende de la siguiente celda. Si la siguiente celda está vacía, la cadena se cruzará o se truncará.

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-KEEP): Mostrar la cadena como en MS Excel al exportar a PDF/Imagen

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-OVERRIDE): Mostrar todo el texto cruzando otras celdas y reemplazar el texto de las celdas cruzadas

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT-IN-CELL): Solo mostrar la cadena dentro del ancho de la celda.

## **Especifica cómo cruzar la cadena en el PDF/Imagen de salida utilizando TextCrossType**

El siguiente código de ejemplo carga el archivo de Excel de ejemplo y lo guarda en formato PDF/Imagen especificando diferentes [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). El archivo de Excel de ejemplo y los archivos de salida se pueden descargar desde los siguientes enlaces

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
{{< app/cells/assistant language="java" >}}
