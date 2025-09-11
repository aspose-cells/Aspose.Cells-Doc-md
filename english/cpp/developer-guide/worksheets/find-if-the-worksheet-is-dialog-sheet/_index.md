---
title: Find if the Worksheet is Dialog Sheet with C++
linktitle: Find if the Worksheet is Dialog Sheet
type: docs
weight: 90
url: /cpp/find-if-the-worksheet-is-dialog-sheet/
description: Dialog Sheet is an old format of sheet. This article provides instructions and sample code for determining programmatically whether an Excel worksheet is a Dialog Sheet using the C++ API.
keywords: find excel worksheet dialog type c++, worksheet dialog c++
---

## **Possible Usage Scenarios**

Dialog Sheet is an old format of sheet that contains a dialog box. Such sheet could be inserted by an older version of Microsoft Excel e.g. 2003 as shown in this screenshot. It can also be inserted with VBA in newer versions e.g. Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

You can find if the sheet is a dialog sheet or some other type of sheet with the [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) property provided by Aspose.Cells. If it returns enumeration value [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) then it means, you are dealing with a dialog sheet.

## **Find if the Worksheet is Dialog Sheet**

The following sample code loads the [sample Excel file](64716820.xlsx) that contains a dialog sheet. It checks the [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) property compares it with [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) and then prints the message. Please see the console output of the sample code given below for more help.

## **Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load Excel file containing Dialog Sheet
    Workbook workbook(u"sampleFindIfWorksheetIsDialogSheet.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Find if the sheet type is dialog and print the message
    if (ws.GetType() == SheetType::Dialog)
    {
        std::cout << "Worksheet is a Dialog Sheet." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

## **Console Output**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}