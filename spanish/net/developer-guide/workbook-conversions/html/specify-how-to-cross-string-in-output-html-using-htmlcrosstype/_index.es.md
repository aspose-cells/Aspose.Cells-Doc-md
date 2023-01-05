---
title: Especifique cómo cruzar la cadena en la salida HTML usando HtmlCrossType
type: docs
weight: 140
url: /es/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **Posibles escenarios de uso**

Cuando la celda contiene texto o una cadena pero es más grande que el ancho de la celda, la cadena se desborda si la siguiente celda en la siguiente columna es nula o está vacía. Cuando guarda su archivo de Excel en HTML, puede controlar este desbordamiento especificando el tipo de cruz usando el[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) enumeración. tiene los siguientes valores

- **HtmlCrossType.Predeterminado**: Mostrar como MS Excel, depende de la siguiente celda. Si la siguiente celda es nula, la cadena se cruzará o se truncará.

- **HtmlCrossType.MSExport**: Muestra la cadena como MS Excel exportando HTML.

- **HtmlCrossType.Cross**: Mostrar HTML cadena cruzada, el rendimiento para crear archivos HTML grandes será más de diez veces más rápido que establecer el valor en Predeterminado o FitToCell.

- **HtmlCrossType.FitToCell**: solo muestra la cadena dentro del ancho de la celda.

## **Especifique cómo cruzar la cadena en la salida HTML usando HtmlCrossType**

 El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](51740732.xlsx) y lo guarda en formato HTML especificando diferentes[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) . Por favor descarga el[HTML de salida](51740734.zip) generado con este código. El archivo de muestra de Excel contiene la imagen bordeada de color rojo como se muestra en esta captura de pantalla que muestra el efecto de la[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) valores en la salida HTML.

![todo:imagen_alternativa_texto](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
