---
title: Obtener cadena HTML5 de Cell
type: docs
weight: 90
url: /es/java/get-html5-string-from-cell/
---
## **Posibles escenarios de uso**

Aspose.Cells devuelve la cadena HTML de la celda usando el[**getHtmlString(booleano html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)método. si pasas**falso**como parámetro, le devolverá HTML normal, pero si pasa**verdadero**como parámetro, devolverá una cadena HTML5.

## **Obtener cadena HTML5 de Cell**

El código de ejemplo siguiente crea un objeto de libro y agrega texto en la celda A1 de la primera hoja de cálculo. Luego obtiene la cadena Normal HTML y HTML5 de la celda A1 usando el[**getHtmlString(booleano html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)método y los imprime en la consola.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **Salida de consola**

{{< highlight "java" >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
