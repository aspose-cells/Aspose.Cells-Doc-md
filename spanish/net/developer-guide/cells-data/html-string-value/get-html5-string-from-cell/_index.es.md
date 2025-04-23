---
title: Obtener cadena HTML5 de la Celda
type: docs
weight: 90
url: /es/net/get-html5-string-from-cell/
description: Aprenda cómo obtener la cadena HTML5 de la celda a través de la API Aspose.Cells for .NET.
keywords: Obtener cadena HTML5 de la celda, obtener cadena HTML5 de la celda, administrar cadena HTML5 de la celda
---

## **Escenarios de uso posibles**

Aspose.Cells devuelve la cadena HTML de la celda utilizando el método [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) que acepta un parámetro booleano. Si pasa **false** como parámetro, devolverá HTML normal, pero si pasa **true** como parámetro, devolverá la cadena HTML5.

## **Obtener cadena HTML5 de la Celda**

El siguiente código de ejemplo crea un objeto de libro de trabajo y agrega un texto en la celda A1 de la primera hoja de cálculo. Luego obtiene la cadena HTML normal y HTML5 de la celda A1 usando el método [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) e imprime en la consola.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **Salida de la consola**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
