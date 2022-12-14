---
title: Especifique cómo cruzar una cadena en el HTML de salida usando HtmlCrossType
type: docs
weight: 140
url: /es/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **Posibles escenarios de uso**

Cuando la celda contiene texto o una cadena pero es más grande que el ancho de la celda, la cadena se desborda si la siguiente celda en la siguiente columna es nula o está vacía. Cuando guarda su archivo de Excel en HTML, puede controlar este desbordamiento especificando el tipo de cruz usando el[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)enumeración. tiene los siguientes valores

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): Mostrar como MS Excel que depende de la siguiente celda. Si la siguiente celda es nula, la cadena se cruzará o se truncará.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): muestra la cadena como MS Excel exportando HTML.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS) : Mostrar cadena cruzada HTML, el rendimiento para crear archivos HTML grandes será más de diez veces más rápido que establecer el valor en[**DEFECTO**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) o[**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): muestra la cadena cruzada HTML y oculta la cadena correcta cuando los textos se superponen.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL): solo muestra la cadena dentro del ancho de la celda.

## **Especifique cómo cruzar una cadena en el HTML de salida usando HtmlCrossType**

El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](51740747.xlsx)lo guarda en formato HTML especificando diferentes[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)Por favor descarga el[HTML de salida](51740745.zip) archivos generados con este código. El archivo de muestra de Excel contiene la imagen bordeada de color rojo como se muestra en esta captura de pantalla que muestra el efecto de la[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)valores en HTML de salida.

![todo:imagen_alternativa_texto](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
