---
title: Set Worksheet Tab Color with C++
linktitle: Set Worksheet Tab Color
type: docs
weight: 120
url: /cpp/set-worksheet-tab-color/
description: This article demonstrates sample code that sets the Excel worksheet Tab Color programmatically using the C++ API or Library.
keywords: set excel tab color c++, code to set excel tab color c++
---

{{% alert color="primary" %}}

Aspose.Cells allows you to change the color of individual worksheet tabs to make them prominent from the rest. For example, you can make Expenses red, Sales green, Assets blue, etc.

{{% /alert %}}

## **Setting Worksheet Tab Color with Microsoft Excel**
1. Right-click a tab in the tab-sheet at the bottom of the current worksheet.
1. Select **Tab color**.
1. Select a color from the palette.
1. Click **OK**.

## **Setting Worksheet Tab Color with Aspose.Cells**
The sample code below shows how to set tab color with Aspose.Cells.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"worksheettabcolor.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the tab color to red
    worksheet.SetTabColor(Color::Red());

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Worksheet tab color set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}