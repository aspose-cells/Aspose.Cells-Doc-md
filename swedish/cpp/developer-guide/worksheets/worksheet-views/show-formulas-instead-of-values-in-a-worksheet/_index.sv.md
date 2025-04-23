---
title: Visa Formler istället för Värden i ett Kalkylblad med C++
linktitle: Visa Formler istället för Värden
type: docs
weight: 20
url: /sv/cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Denna artikel tillhandahåller exempel kod för att använda C++ API för att programmässigt visa formler istället för värden i ett Excel kalkylblad eller kalkylblad.
---

{{% alert color="primary" %}}

Det är möjligt att visa formler istället för beräknade värden i Microsoft Excel med hjälp av alternativet **Visa formler** från **Formler**-fliken. När formler visas visar Microsoft Excel formler i kalkylbladet. Du kan uppnå samma sak med hjälp av Aspose.Cells.

{{% /alert %}}

Aspose.Cells tillhandahåller en [**Worksheet.GetShowFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getshowformulas/)-egenskap. Ange detta till **true** för att ställa in Microsoft Excel att visa formler.

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
