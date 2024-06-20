---
title: Especifique cómo cruzar cadenas en HTML de salida utilizando HtmlCrossType
type: docs
weight: 140
url: /es/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Escenarios de uso posibles**

Cuando la celda contiene texto o una cadena pero es más grande que el ancho de la celda, entonces la cadena se desborda si la siguiente celda en la siguiente columna está vacía o nula. Al guardar su archivo de Excel en HTML, puede controlar este desbordamiento especificando el tipo de cruce utilizando la enumeración [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType). Tiene los siguientes valores

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): Mostrar como MS Excel que depende de la siguiente celda. Si la siguiente celda está vacía, la cadena se cruzará o se truncará.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): Muestre la cadena como si fuera MS Excel exportando HTML.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS): Muestre la cadena HTML cruzada, el rendimiento para crear archivos HTML grandes será más de diez veces más rápido que configurar el valor en [**DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) o [**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): Muestre la cadena HTML cruzada y oculte la cadena derecha cuando los textos se superponen.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL): Solo mostrar la cadena dentro del ancho de la celda.

## **Especifica cómo cruzar la cadena en HTML de salida utilizando HtmlCrossType**

El siguiente código de ejemplo carga el [archivo Excel de muestra](51740747.xlsx) y lo guarda en formato HTML especificando diferentes [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType). Descargue los archivos de HTML de salida generados con este código desde [aquí](51740745.zip). El archivo Excel de muestra contiene la imagen bordeada con color rojo como se muestra en esta captura de pantalla que muestra el efecto de los valores [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType) en el HTML de salida.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
