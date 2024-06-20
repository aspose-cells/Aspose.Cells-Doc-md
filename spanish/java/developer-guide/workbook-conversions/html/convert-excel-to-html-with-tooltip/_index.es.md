---
title: Convertir Excel a HTML con tooltip
type: docs
weight: 150
url: /es/java/convert-excel-to-html-with-tooltip/
---

## **Convertir Excel a HTML con tooltip**

Puede haber casos en los que el texto se corte en el HTML generado y desees mostrar el texto completo como información sobre herramientas en el evento de desplazamiento. Aspose.Cells admite esto proporcionando la propiedad [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText). Establecer la propiedad [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText) en **true** agregará el texto completo como información sobre herramientas en el HTML generado.

La siguiente imagen muestra el tooltip en el archivo HTML generado.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

La siguiente muestra de código carga el [archivo de Excel fuente](AddTooltipToHtmlSample.xlsx) y genera el [archivo HTML de salida](AddTooltipToHtmlSample_out.zip) con la información sobre herramientas.

## Código de Muestra

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.java" >}}
