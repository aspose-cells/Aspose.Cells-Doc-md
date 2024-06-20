---
title: Obtener cadena HTML5 de la Celda
type: docs
weight: 40
url: /es/python-java/get-html5-string-from-cell/
---

## **Obtener cadena HTML5 de la Celda**
Usando Aspose.Cells para Python via Java, puedes obtener la cadena HTML de la celda. Esto se puede lograr utilizando el método [getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)). Si pasas **false** como parámetro, te devolverá un HTML normal pero si pasas **true** como parámetro, te devolverá una cadena HTML5.

El siguiente código de ejemplo crea un objeto de libro y agrega un texto en la celda A1 de la primera hoja de trabajo. Luego obtiene la cadena de HTML normal y HTML5 de la celda A1 utilizando el método [getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) y los imprime.
## **Código de muestra**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

La siguiente es la salida generada por el fragmento de código proporcionado anteriormente.
## **Salida**
{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
