---
title: Convierta Excel a HTML con información sobre herramientas
type: docs
weight: 200
url: /es/net/convert-excel-to-html-with-tooltip/
---
## **Convierta Excel a HTML con información sobre herramientas**

Puede haber casos en los que el texto se corte en el HTML generado y desee mostrar el texto completo como información sobre herramientas en el evento de desplazamiento. Aspose.Cells apoya esto proporcionando**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)** propiedad. Configuración de la**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)** propiedad a**verdadero** agregará el texto completo como información sobre herramientas en el HTML generado.

La siguiente imagen muestra la información sobre herramientas en el archivo HTML generado.

![todo:imagen_alternativa_texto](convert-excel-to-html-with-tooltip_1.jpg)

 El siguiente ejemplo de código carga el[archivo fuente excel](98107416.xlsx) y genera la[archivo de salida HTML](98107417.zip) con la información sobre herramientas.

Código de muestra

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.cs" >}}
