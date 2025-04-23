---
title: Especifique cómo cruzar cadenas en HTML de salida utilizando HtmlCrossType
type: docs
weight: 140
url: /es/python-net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Escenarios de uso posibles**

Cuando la celda contiene texto o una cadena pero es más grande que el ancho de la celda, entonces la cadena se desborda si la siguiente celda en la siguiente columna está vacía o nula. Al guardar su archivo de Excel en HTML, puede controlar este desbordamiento especificando el tipo de cruce utilizando la enumeración [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype). Tiene los siguientes valores

- **HtmlCrossType.DEFAULT**: Mostrar como MS Excel, depende de la siguiente celda. Si la siguiente celda es nula, la cadena se cruzará o se truncará.

- **HtmlCrossType.MS_EXPORT**: Mostrar la cadena como MS Excel al exportar a HTML.

- **HtmlCrossType.CROSS**: Mostrar la cadena de cruce en HTML, el rendimiento para crear archivos HTML grandes será más de diez veces más rápido que al establecer el valor en Default o FitToCell.

- **HtmlCrossType.CROSS_HIDE_RIGHT**: Mostrar la cadena HTML cruzada y ocultar la cadena derecha cuando los textos se superponen.

- **HtmlCrossType.FIT_TO_CELL**: Mostrar solo la cadena dentro del ancho de la celda.

## **Especifica cómo cruzar la cadena en HTML de salida utilizando HtmlCrossType**

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](51740732.xlsx) y lo guarda en formato HTML especificando diferentes [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype). Descargue los [HTML de salida](51740734.zip) generados con este código. El archivo de Excel de ejemplo contiene la imagen bordeada con un color rojo como se muestra en esta captura de pantalla que muestra el efecto de los valores [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype) en el HTML de salida.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SpecifyHtmlCrossTypeInOutputHTML.py" >}}
