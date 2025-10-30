---
title: Infoga tidslinje med C++
linktitle: Tidslinjer
type: docs
weight: 170
url: /sv/cpp/create-timeline/
description: Lär dig hur man skapar en tidslinje med Aspose.Cells med C++.
---

## **Möjliga användningsscenario**

Istället för att justera filter för att visa datum kan du använda en pivottabell-tidslinje — ett dynamiskt filteralternativ som låter dig enkelt filtrera efter datum/tid och zooma in på den period du vill ha med en skjutreglagen. Microsoft Excel låter dig skapa en tidslinje genom att välja en pivottabell och sedan klicka på *Infoga > Tidslinje*. Aspose.Cells låter dig också skapa en tidslinje med hjälp av [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.timelines/timelinecollection/add/) metoden.

## **Skapa tidslinje till en Pivot-tabell**

Se följande exempelkod. Den laddar den [provs Excel-fil](input.xlsx) som innehåller pivot-tabellen. Den skapar sedan tidslinjen baserad på det första baspivot-fältet. Slutligen sparar den arbetsboken i [output XLSX](output.xlsx) format. Följande skärmbild visar tidslinjen skapad av Aspose.Cells i den slutliga Excel-filen.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing pivot table
    U16String inputFilePath = u"input.xlsx";
    Workbook wb(inputFilePath);

    // Access second worksheet (index 1)
    Worksheet sheet = wb.GetWorksheets().Get(1);

    // Access first pivot table inside the worksheet
    PivotTable pivot = sheet.GetPivotTables().Get(0);

    // Add timeline relating to pivot table
    int index = sheet.GetTimelines().Add(pivot, 15, 1, u"Ship Date");

    // Access the newly added timeline from timeline collection
    Timeline timeline = sheet.GetTimelines().Get(index);

    // Save the modified workbook
    U16String outputFilePath = u"output.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Timeline added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
