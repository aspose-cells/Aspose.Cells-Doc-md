---
title: Calcular el Factor de Escalado de Configuración de Página con C++
linktitle: Calcular Factor de Escala de Configuración de Página
type: docs
weight: 300
url: /es/cpp/calculate-page-setup-scaling-factor/
description: Este artículo proporciona código de ejemplo que explica cómo usar la API o biblioteca en C++ para calcular el factor de escalado de la configuración de página usando la opción Ajustar a n páginas de ancho por m de alto de la hoja de cálculo de Excel programáticamente.
keywords: Ajustar a n páginas de ancho por m de alto en Excel C++, calcular el factor de escalado de la configuración de página en C++
---

{{% alert color="primary" %}}

Cuando se establece la Escala de Configuración de Página usando la opción **Ajustar a n página(s) de ancho por m de alto**, Microsoft Excel calcula el Factor de Escala de Configuración de Página. Puedes calcular lo mismo utilizando la propiedad [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/). Esta propiedad devuelve un valor double que se puede convertir a un valor porcentual. Por ejemplo, si devuelve 0.5, significa que el factor de escala es del 50%.

{{% /alert %}}

El siguiente código de ejemplo ilustra cómo calcular el factor de escala de configuración de página utilizando la propiedad [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some data in these cells
    worksheet.GetCells().Get(u"A4").PutValue(u"Test");
    worksheet.GetCells().Get(u"S4").PutValue(u"Test");

    // Set paper size
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Set fit to pages wide as 1
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Calculate page scale via sheet render
    ImageOrPrintOptions options;
    SheetRender sr(worksheet, options);

    // Convert page scale double value to percentage
    double pageScale = sr.GetPageScale();
    std::wstring strPageScale = std::to_wstring(pageScale * 100) + L"%";

    // Write the page scale value
    std::wcout << strPageScale << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
