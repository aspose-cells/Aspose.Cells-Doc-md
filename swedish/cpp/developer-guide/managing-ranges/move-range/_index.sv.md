---
title: Flytta cellområde i ett kalkylblad med C++
linktitle: Flytta cellintervall i en arbetsbok
type: docs
weight: 370
url: /sv/cpp/move-range-of-cells-in-a-worksheet/
description: Lär dig hur du flyttar ett cellområde i ett kalkylblad med Aspose.Cells i C++.
---

{{% alert color="primary" %}}

Den här artikeln visar hur man flyttar ett cellintervall i en arbetsbok.

{{% /alert %}}

## **Flytta cellområde i ett kalkylblad**
Exempelkoden använder en mallfil för att demonstrera uppgiften.

**Ingångsfilen**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)

Se den genererade filen med intervallet A1:B5 flyttat till C1:D5 nedan.

**Utgångsfilen**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the workbook object. Open the Excel file
    U16String inputFilePath = u"book1.xlsx";
    Workbook workbook(inputFilePath);

    // Access the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create a range from A1 to B5
    Range range = cells.CreateRange(u"A1", u"B5");

    // Move the range to the right by 2 columns
    range.MoveTo(0, 2);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
