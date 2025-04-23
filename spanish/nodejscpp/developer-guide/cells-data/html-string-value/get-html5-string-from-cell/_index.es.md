---
title: Obtener cadena HTML5 de la Celda
type: docs
weight: 90
url: /es/nodejs-cpp/get-html5-string-from-cell/
description: Aprender cómo obtener cadenas HTML5 de una celda a través de la API Aspose.Cells for Node.js via C++.
keywords: Obtener cadena HTML5 de una celda Node.js a través de C++, Obtener cadena HTML5 de una celda Node.js a través de C++, Gestionar cadena HTML5 de una celda Node.js a través de C++
---

## **Escenarios de uso posibles**

Aspose.Cells devuelve la cadena HTML de la celda usando el método [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) que acepta un parámetro booleano. Si pasas **false** como parámetro, devolverá HTML normal; si pasas **true**, devolverá cadena HTML5.

## **Obtener cadena HTML5 de la Celda**

El siguiente código de ejemplo crea un objeto libro de trabajo y agrega algo de texto en la celda A1 de la primera hoja. Luego obtiene las cadenas HTML normal y HTML5 de la celda A1 usando el método [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) y las imprime en la consola.

## **Código de muestra**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-HtmlStringValue-GetHtml5String.js" >}}


## **Salida de la consola**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
