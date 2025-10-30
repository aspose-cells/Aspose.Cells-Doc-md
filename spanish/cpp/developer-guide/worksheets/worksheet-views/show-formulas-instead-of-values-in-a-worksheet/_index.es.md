---
title: Mostrar fórmulas en lugar de valores en una hoja de cálculo con C++
linktitle: Mostrar fórmulas en lugar de valores
type: docs
weight: 20
url: /es/cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Este artículo proporciona código de ejemplo para usar la API C++ para mostrar fórmulas en lugar de valores en una hoja de cálculo o hoja de Excel.
---

{{% alert color="primary" %}}

Es posible mostrar fórmulas en lugar de valores calculados en Microsoft Excel utilizando la opción **Mostrar fórmulas** de la cinta **Fórmulas**. Cuando se muestran las fórmulas, Microsoft Excel muestra las fórmulas en la hoja de trabajo. Puedes lograr lo mismo usando Aspose.Cells.

{{% /alert %}}

Aspose.Cells proporciona una propiedad [**Worksheet.GetShowFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getshowformulas/). Establece esto en **true** para que Microsoft Excel muestre fórmulas.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"source.xlsx";

    // Load the source workbook
    Workbook workbook(filePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Show formulas of the worksheet
    worksheet.SetShowFormulas(true);

    // Save the workbook
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Formulas shown successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
