---
title: Convertir Excel a HTML con tooltip usando C++
linktitle: Convertir Excel a HTML con tooltip
type: docs
weight: 200
url: /es/go-cpp/convert-excel-to-html-with-tooltip/
description: Convertir Excel a HTML añadiendo tooltips con Aspose.Cells usando C++.
---

## **Convertir Excel a HTML con tooltip**

Podría haber casos en los que el texto se corte en el HTML generado y desees mostrar el texto completo como tooltip al pasar el cursor. Aspose.Cells soporta esto proporcionando la propiedad [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/). Establecer la propiedad [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/) en **true** añadirá el texto completo como tooltip en el HTML generado.

La siguiente imagen muestra el tooltip en el archivo HTML generado.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

El siguiente ejemplo carga el [archivo fuente de Excel](98107416.xlsx) y genera el [archivo HTML de salida](98107417.zip) con el tooltip.

Código de muestra

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToHtmlWithTooltip.go" >}}
