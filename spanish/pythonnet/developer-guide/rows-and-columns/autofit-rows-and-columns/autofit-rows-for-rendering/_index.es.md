---
title: Autoajustar filas para renderizado
type: docs
weight: 130
url: /es/python-net/autofit-rows-for-rendering/
description: Aprende cómo ajustar filas para renderización a través de la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Ajustar Filas para Renderización de Python, Ajustar automáticamente la altura de la fila al abrir un archivo de Excel. 
---

Generalmente, cuando desea mostrar todo el texto en una celda, puede autoajustar la fila en vista Normal con un zoom al 100% en Microsoft Excel. Esto permite que el texto sea completamente visible en la vista Normal, e incluso al imprimir o guardar el archivo como PDF, el texto se mostrará correctamente.

Sin embargo, en algunos casos, el ajuste automático de la fila funciona bien en la vista normal, pero cuando cambias a la vista de impresión o guardas el archivo como un PDF, el texto se recorta. Por favor, verifica el archivo fuente [Book1.xlsx](Book1.xlsx) y las capturas de pantalla.

![el texto está recortado en la vista de impresión](text_clipped_in_printview.png)

Si deseas evitar que el texto se recorte en el archivo PDF guardado, puedes ajustar automáticamente la fila con la opción [AutoFitterOptions.for_rendering](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/for_rendering/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsForRendering.py" >}}

Ahora, el texto no está recortado en el archivo PDF de salida.

![el texto no está recortado en el PDF guardado](text_not_clipped_in_saved_pdf.png)
{{< app/cells/assistant language="python-net" >}}
