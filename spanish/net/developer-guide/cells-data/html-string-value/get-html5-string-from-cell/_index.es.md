---
title: Obtener cadena HTML5 de Cell
type: docs
weight: 90
url: /es/net/get-html5-string-from-cell/
---
## **Posibles escenarios de uso**

Aspose.Cells devuelve la cadena HTML de la celda usando el[**ObtenerCadenaHtml**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) método que acepta un parámetro booleano. si pasas**falso**como parámetro, devolverá HTML normal, pero si pasa**verdadero** como parámetro, devolverá una cadena HTML5.

## **Obtener cadena HTML5 de Cell**

El código de ejemplo siguiente crea un objeto de libro y agrega texto en la celda A1 de la primera hoja de cálculo. Luego obtiene la cadena Normal HTML y HTML5 de la celda A1 usando el[**ObtenerCadenaHtml**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)método y los imprime en la consola.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **Salida de consola**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
