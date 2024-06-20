---
title: Obtener cadena HTML5 de la Celda
type: docs
weight: 90
url: /es/java/get-html5-string-from-cell/
---

## **Escenarios de uso posibles**

Aspose.Cells devuelve la cadena HTML de la celda usando el método [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString). Si pasas **false** como parámetro, te devolverá HTML Normal pero si pasas **true** como parámetro, te devolverá la cadena HTML5.

## **Obtener cadena HTML5 de la Celda**

El siguiente código de muestra crea un objeto workbook y agrega texto en la celda A1 de la primera hoja de trabajo. Luego obtiene la cadena HTML Normal y HTML5 de la celda A1 usando el método [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString) e imprime en la consola.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **Salida de la consola**

{{< highlight java >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
