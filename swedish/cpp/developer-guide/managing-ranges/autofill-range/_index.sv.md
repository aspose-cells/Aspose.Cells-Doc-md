---
title: AutoFill område för Excel fil med C++
linktitle: Autofyllningsområde
type: docs
weight: 105
url: /sv/cpp/autofill-ranges/
description: Lär dig hur du utför en autofylloperation i ett specificerat område i en Excel fil med Aspose.Cells och C++.
---

## **Utför en Autofyll i det angivna området i Excel**

I Excel, välj ett område, för musen till nedre högra hörnet och dra "+" för att autofylla data.

## **Autofyll områden med Aspose.Cells**

Följande exempel visar hur man utför en AutoFill-operation på ett område. Här är en exempel fil som kan laddas ner för att testa denna funktion:

[range_autofill.xlsx](range_autofill.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"range_autofill.xlsx");

    // Get Cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create Range
    Range src = cells.CreateRange(u"C3:C4");
    Range dest = cells.CreateRange(u"C5:C10");

    // AutoFill
    src.AutoFill(dest, AutoFillType::Series);

    // Save the Workbook
    workbook.Save(u"range_autofill_result.xlsx");

    std::cout << "Range auto-filled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
