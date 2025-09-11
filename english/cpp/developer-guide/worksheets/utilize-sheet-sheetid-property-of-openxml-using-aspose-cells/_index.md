---
title: Utilize Sheet.SheetId property of OpenXml with C++
linktitle: Utilize Sheet.SheetId property of OpenXml
type: docs
weight: 200
url: /cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: This article shows how to utilize Sheet.SheetId property of OpenXml using Excel manipulation C++ API or Library programmatically.
keywords: sheet id property of openxml c++, sheet id excel worksheet c++
---

## **Possible Usage Scenarios**

*Sheet.SheetId* property is found inside the *DocumentFormat.OpenXml.Spreadsheet* namespace and is part of OpenXml. You can see this property and its value inside *workbook.xml* as shown in the following screenshot. Aspose.Cells provides the equivalent property as [**Worksheet.GetTabId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettabid/).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Utilize Sheet.SheetId property of OpenXml using Aspose.Cells**

The following sample code loads the [sample Excel file](51740716.xlsx), reads its Sheet or Tab Id, then assigns it new Tab Id and saves it as [output Excel file](51740717.xlsx). Please also see the console output of the code given below for a reference.

## **Sample Code**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load source Excel file
    Workbook wb(u"sampleSheetId.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Print its Sheet or Tab Id on console
    std::cout << "Sheet or Tab Id: " << ws.GetTabId() << std::endl;

    // Change Sheet or Tab Id
    ws.SetTabId(358);

    // Save the workbook
    wb.Save(u"outputSheetId.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Console Output**

{{< highlight java >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}