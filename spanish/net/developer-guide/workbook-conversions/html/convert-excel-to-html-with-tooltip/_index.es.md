---
title: Convertir Excel a HTML con tooltip
type: docs
weight: 200
url: /es/net/convert-excel-to-html-with-tooltip/
---

## **Convertir Excel a HTML con tooltip**

Puede haber casos en los que el texto se corte en el HTML generado y desees mostrar el texto completo como un tooltip en el evento de desplazamiento. Aspose.Cells admite esto mediante la propiedad [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext). Establecer la propiedad [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext) en **true** añadirá el texto completo como un tooltip en el HTML generado.

La siguiente imagen muestra el tooltip en el archivo HTML generado.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

El siguiente ejemplo de código carga el [archivo de Excel fuente](98107416.xlsx) y genera el [archivo HTML de salida](98107417.zip) con el tooltip.

Código de muestra

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.cs" >}}
