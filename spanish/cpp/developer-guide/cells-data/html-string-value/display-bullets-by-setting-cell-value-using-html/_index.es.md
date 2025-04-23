---
title: Mostrar viñetas configurando el Valor de la Celda usando HTML con C++
linktitle: Mostrar Viñetas al Establecer el Valor de la Celda usando HTML
type: docs
weight: 130
url: /es/cpp/display-bullets-by-setting-cell-value-using/
description: Agregar viñetas a celdas de Excel usando HTML y la API Aspose.Cells for C++, fácil de usar.
keywords: agregar viñetas en Excel, agregar viñetas en Excel c++, mostrar viñetas en Excel, mostrar viñetas en Excel c++, agregar viñetas en Excel con HTML, agregar viñetas en Excel con HTML c++, mostrar viñetas en Excel con HTML, mostrar viñetas en Excel con HTML c++, mostrar viñetas en Excel usando HTML, agregar viñetas en Excel usando HTML
---

{{% alert color="primary" %}}

Aspose.Cells es compatible con la visualización de viñetas con código HTML. Este artículo explicará cómo mostrar viñetas configurando el valor de la celda usando HTML. Usaremos la propiedad [**Cell.GetHtmlString()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) para establecer el valor de la celda con nuestro HTML.

{{% /alert %}}

## Código C++ para mostrar viñetas configurando el valor de la celda usando HTML

El siguiente código utiliza código HTML para establecer el valor de la celda. Una vez que ejecutes este código, obtendrás la salida como se muestra en la imagen a continuación.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get("A1");

    // Set the HTML string
    cell.SetHtmlString(u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'>Text 1 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 2 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 3 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 4 </font>");

    // Auto fit the Columns
    worksheet.AutoFitColumns();

    // Save the workbook
    U16String outputFilePath = u"BulletsInCells_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Resultado generado por el código de ejemplo

La siguiente captura de pantalla muestra la salida del código de muestra anterior.

![todo:image_alt_text](display-bullets-by-setting-cell-value-using-html_1.png)
