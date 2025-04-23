---
title: Ajuste automático de filas para renderizado con C++
linktitle: Autoajustar filas para renderizado
type: docs
weight: 130
url: /es/cpp/autofit-rows-for-rendering/
description: Aprenda cómo ajustar automáticamente las filas para renderizado en archivos de Excel usando Aspose.Cells con C++.
---

Generalmente, cuando desea mostrar todo el texto en una celda, puede autoajustar la fila en vista Normal con un zoom al 100% en Microsoft Excel. Esto permite que el texto sea completamente visible en la vista Normal, e incluso al imprimir o guardar el archivo como PDF, el texto se mostrará correctamente.

Sin embargo, en algunos casos, el ajuste automático de la fila funciona bien en la vista normal, pero cuando cambias a la vista de impresión o guardas el archivo como un PDF, el texto se recorta. Por favor, verifica el archivo fuente [Book1.xlsx](Book1.xlsx) y las capturas de pantalla.

![el texto está recortado en la vista de impresión](text_clipped_in_printview.png)

Si desea evitar que el texto se recorte en el archivo PDF guardado, puede ajustar automáticamente la fila con la opción [AutoFitterOptions.GetForRendering()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getforrendering/).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize workbook instance
    Workbook workbook(u"Book1.xlsx");

    // Set autofit options for rendering
    AutoFitterOptions autoFitterOptions;
    autoFitterOptions.SetForRendering(true);

    // Autofit rows with options
    workbook.GetWorksheets().Get(0).AutoFitRows(autoFitterOptions);

    // Save to PDF
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    Aspose::Cells::Cleanup();
}
```

Ahora, el texto no está recortado en el archivo PDF de salida.

![el texto no está recortado en el PDF guardado](text_not_clipped_in_saved_pdf.png)
