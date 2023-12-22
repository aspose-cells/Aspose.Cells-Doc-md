---
title: Autoajustar filas para renderizado
type: docs
weight: 130
url: /es/java/autofit-rows-for-rendering/
---
Generalmente, cuando desea mostrar todo el texto en una celda, puede ajustar automáticamente la fila en la vista Normal con un zoom del 100% en Microsoft Excel. Esto permite que el texto sea completamente visible en la vista Normal, e incluso cuando imprima o guarde el archivo como PDF, el texto se mostrará correctamente.

 Sin embargo, en algunos casos, la fila de ajuste automático funciona bien en la vista Normal, pero cuando cambia a la vista de impresión o guarda el archivo como PDF, el texto se recorta. Por favor verifique el archivo fuente[Libro1.xlsx](Book1.xlsx) y capturas de pantalla.

![el texto está recortado en printview](text_clipped_in_printview.png)

Si desea evitar que el texto se recorte en el archivo PDF guardado, puede ajustar automáticamente la fila con el[AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions/#setForRendering-boolean-) opción.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Autofit-AutofitRowsForRendering.java" >}}

Ahora, el texto no está recortado en el archivo de salida PDF.

![el texto no está recortado en el pdf guardado](text_not_clipped_in_saved_pdf.png)