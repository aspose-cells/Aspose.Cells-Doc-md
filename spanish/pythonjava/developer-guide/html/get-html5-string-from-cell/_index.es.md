---
title: Obtener cadena HTML5 de Cell
type: docs
weight: 40
url: /es/python-java/get-html5-string-from-cell/
---
## **Obtener cadena HTML5 de Cell**
Usando Aspose.Cells for Python via Java, puede obtener la cadena HTML de la celda. Esto se puede lograr usando el[getHtmlString(booleano html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) método proporcionado por el API. Si pasa**falso**como parámetro te devolverá Normal HTML pero si pasas**verdadero**como parámetro, devolverá una cadena HTML5.

El código de ejemplo siguiente crea un objeto de libro y agrega texto en la celda A1 de la primera hoja de cálculo. Luego obtiene la cadena Normal HTML y HTML5 de la celda A1 usando el[getHtmlString(booleano html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) y los imprime.
## **Código de muestra**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

El siguiente es el resultado generado por el fragmento de código proporcionado anteriormente.
## **Producción**
{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
