---
title: Ocultar contenido sobrepuesto con CrossHideRight al guardar en HTML con Golang a través de C++
linktitle: Ocultar contenido superpuesto con CrossHideRight al guardar en HTML
type: docs
weight: 100
url: /es/go-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: Usa CrossHideRight con Aspose.Cells en C++ para ocultar contenido superpuesto al guardar en HTML.
---

## **Escenarios de uso posibles**

Al guardar tu archivo de Excel en HTML, puedes especificar diferentes tipos de cruce para las cadenas de celdas. Por defecto, Aspose.Cells genera HTML según Microsoft Excel, pero cuando cambias el tipo de cruce a [**CrossHideRight**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype), oculta todas las cadenas en el lado derecho de la celda que están superpuestas o solapadas con la cadena de la celda.

## **Ocultar contenido superpuesto con CrossHideRight al guardar en Html**

El siguiente código de ejemplo carga el [archivo Excel de ejemplo](64716894.xlsx) y lo guarda en [HTML de salida](64716893.zip) después de configurar [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/gethtmlcrossstringtype/) como [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype). La captura de pantalla explica cómo [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) afecta el HTML de salida respecto al predeterminado.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HidingOverlaidContentWithCrosshiderightWhileSavingToHtml.go" >}}
