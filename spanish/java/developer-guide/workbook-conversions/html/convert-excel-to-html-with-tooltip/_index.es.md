---
title: Convierta Excel a HTML con información sobre herramientas
type: docs
weight: 150
url: /es/java/convert-excel-to-html-with-tooltip/
---
## **Convierta Excel a HTML con información sobre herramientas**

Puede haber casos en los que el texto se corte en el HTML generado y desee mostrar el texto completo como información sobre herramientas en el evento de desplazamiento. Aspose.Cells apoya esto proporcionando**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)**propiedad. Configuración de la**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)**propiedad a**verdadero**agregará el texto completo como información sobre herramientas en el HTML generado.

La siguiente imagen muestra la información sobre herramientas en el archivo HTML generado.

![todo:imagen_alternativa_texto](convert-excel-to-html-with-tooltip_1.jpg)

El siguiente ejemplo de código carga el[archivo fuente excel](AddTooltipToHtmlSample.xlsx)y genera la[archivo HTML de salida](AddTooltipToHtmlSample_out.zip)con la información sobre herramientas.

## Código de muestra

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.java" >}}
