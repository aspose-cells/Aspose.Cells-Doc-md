---
title: Fyll på data först radvis, sedan kolumnvis med C++
linktitle: Populera Data Först per Rad och sedan per Kolumn
type: docs
weight: 1000
url: /sv/cpp/populate-data-first-by-row-then-by-column/
description: Lär dig hur du fyller på data först radvis, sedan kolumnvis via API et Aspose.Cells for C++.
keywords: Fyll i data först efter raden och sedan efter kolumnen, Infoga data först efter raden och sedan efter kolumnen, Lägg till data först efter raden och sedan efter kolumnen, Högpresterande datainfogning, Högpresterande dataaddition
---

{{% alert color="primary" %}} 

Att fylla i ett kalkylblad med data först per rad och sedan per kolumn förbättrar den övergripande prestandan.

{{% /alert %}} 

Att placera data i sekvensen A1, B1, A2, B2 går snabbare än A1, A2, B1, B2. Om det finns många celler i ett kalkylblad och du följer den andra sekvensen, det vill säga fyller i data rad för rad, kan detta tips göra programmet mycket snabbare.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook workbook;

    // Populate Data into Cells
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();
    cells.Get(u"A1").PutValue(U"data1");
    cells.Get(u"B1").PutValue(U"data2");
    cells.Get(u"A2").PutValue(U"data3");
    cells.Get(u"B2").PutValue(U"data4");

    // Save workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
