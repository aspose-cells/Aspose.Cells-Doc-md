---
title: Convierta Excel a HTML con información sobre herramientas
type: docs
weight: 200
url: /es/python-net/convert-excel-to-html-with-tooltip/
description: Este tema le muestra cómo convertir Excel a HTML con información sobre herramientas usando Aspose.Cells for Python a través de NET.
keywords: Python Convert Excel to HTML with tooltip, Convert Excel to HTML with tooltip Python via NET, Python via NET Excel to HTML with tooltip, Python Workbook to HTML with tooltip.
---
##  **Convierta Excel a HTML con información sobre herramientas**

Puede haber casos en los que el texto esté cortado en el HTML generado y desee mostrar el texto completo como información sobre herramientas en el evento de desplazamiento. Aspose.Cells apoya esto proporcionando**[HtmlSaveOptions.add_tooltip_text](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/)** propiedad. Configurando el**[HtmlSaveOptions.add_tooltip_text](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/)** propiedad a**verdadero** agregará el texto completo como información sobre herramientas en el HTML generado.

La siguiente imagen muestra la información sobre herramientas en el archivo HTML generado.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

 El siguiente ejemplo de código carga el[archivo excel fuente](98107416.xlsx) y genera el[salida del archivo HTML](98107417.zip) con la información sobre herramientas.

Código de muestra

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ConvertExcelFileToHtmlWithTooltip-1.py" >}}
