---
title: Convertir Excel a HTML con tooltip
type: docs
weight: 200
url: /es/python-net/convert-excel-to-html-with-tooltip/
description: Este tema le muestra cómo convertir Excel a HTML con información sobre herramientas usando Aspose.Cells para Python via NET.
keywords: Python Convertir Excel a HTML con información sobre herramientas, Convertir Excel a HTML con información sobre herramientas Python via NET, Python via NET Excel a HTML con información sobre herramientas, Python Libro a HTML con información sobre herramientas.
---

## **Convertir Excel a HTML con tooltip**

Puede haber casos en los que el texto se corte en el HTML generado y desees mostrar el texto completo como un tooltip en el evento de desplazamiento. Aspose.Cells admite esto mediante la propiedad [**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/). Establecer la propiedad [**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/) en **true** añadirá el texto completo como un tooltip en el HTML generado.

La siguiente imagen muestra el tooltip en el archivo HTML generado.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

El siguiente ejemplo de código carga el [archivo de Excel fuente](98107416.xlsx) y genera el [archivo HTML de salida](98107417.zip) con el tooltip.

Código de muestra

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ConvertExcelFileToHtmlWithTooltip-1.py" >}}
