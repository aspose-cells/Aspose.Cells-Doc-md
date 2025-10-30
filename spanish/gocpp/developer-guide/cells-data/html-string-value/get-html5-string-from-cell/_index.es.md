---
title: Obtener cadena HTML5 de una celda con Golang a través de C++
linktitle: Obtener cadena HTML5 de la Celda
type: docs
weight: 90
url: /es/go-cpp/get-html5-string-from-cell/
description: Aprende cómo obtener la cadena HTML5 de una celda usando la API Aspose.Cells for C++.
keywords: Obtener cadena HTML5 de la celda, obtener cadena HTML5 de la celda, administrar cadena HTML5 de la celda
---

## **Escenarios de uso posibles**

Aspose.Cells devuelve la cadena HTML de la celda usando el método [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/) que acepta un parámetro booleano. Si pasas **false**, devolverá HTML normal, pero si pasas **true**, devolverá cadena HTML5.

## **Obtener cadena HTML5 de la Celda**

El siguiente código de ejemplo crea un objeto de libro de trabajo y agrega un texto en la celda A1 de la primera hoja de cálculo. Luego obtiene la cadena HTML normal y HTML5 de la celda A1 usando el método [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/) e imprime en la consola.

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetHtml5StringFromCell.go" >}}
## **Salida de la consola**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
