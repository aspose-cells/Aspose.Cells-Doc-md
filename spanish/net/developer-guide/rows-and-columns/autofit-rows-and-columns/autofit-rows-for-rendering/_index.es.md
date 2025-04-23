---
title: Autoajustar filas para renderizado
type: docs
weight: 130
url: /es/net/autofit-rows-for-rendering/
---

Generalmente, cuando desea mostrar todo el texto en una celda, puede autoajustar la fila en vista Normal con un zoom al 100% en Microsoft Excel. Esto permite que el texto sea completamente visible en la vista Normal, e incluso al imprimir o guardar el archivo como PDF, el texto se mostrará correctamente.

Sin embargo, en algunos casos, el ajuste automático de la fila funciona bien en la vista normal, pero cuando cambias a la vista de impresión o guardas el archivo como un PDF, el texto se recorta. Por favor, verifica el archivo fuente [Book1.xlsx](Book1.xlsx) y las capturas de pantalla.

![el texto está recortado en la vista de impresión](text_clipped_in_printview.png)

Si quieres evitar que el texto se recorte en el archivo PDF guardado, puedes ajustar automáticamente la fila con la opción [AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/forrendering/)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Autofit-AutofitRowsForRendering.cs" >}}

Ahora, el texto no está recortado en el archivo PDF de salida.

![el texto no está recortado en el PDF guardado](text_not_clipped_in_saved_pdf.png)
{{< app/cells/assistant language="csharp" >}}
