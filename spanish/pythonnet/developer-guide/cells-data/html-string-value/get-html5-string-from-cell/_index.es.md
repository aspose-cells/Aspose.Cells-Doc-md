---
title: Obtener cadena HTML5 de la Celda
type: docs
weight: 90
url: /es/python-net/get-html5-string-from-cell/
description: Aprende cómo obtener la cadena HTML5 de la celda a través de la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Obtener cadena HTML5 de la celda en Python, Obtener cadena HTML5 de la celda usando Python, Manejar la cadena HTML5 de la celda en Python.
---

## **Escenarios de uso posibles**

Aspose.Cells para Python via .NET devuelve la cadena HTML de la celda usando el método [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool) que acepta un parámetro booleano. Si pasa **false** como parámetro, devolverá HTML normal pero si pasa **true** como parámetro, devolverá la cadena HTML5.

## **Obtener cadena HTML5 de la Celda**

El siguiente código de ejemplo crea un objeto de libro de trabajo y agrega un texto en la celda A1 de la primera hoja de cálculo. Luego obtiene la cadena HTML normal y HTML5 de la celda A1 usando el método [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool) e imprime en la consola.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetHTML5StringFromCell.py" >}}

## **Salida de la consola**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
