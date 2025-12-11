---
title: Check if VBA Project is Protected and Locked for Viewing with C++
linktitle: Check if VBA Project is Protected and Locked for Viewing
type: docs
weight: 30
url: /cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Learn how to check if VBA Project is protected and locked for viewing in Excel files using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Check if VBA Project is Protected and Locked for Viewing in C++

Aspose.Cells allows you to check if the VBA (Visual Basic for Applications) Project of an Excel file is protected and locked for viewing. For this, the API provides the [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/) property. If it is locked for viewing, then the [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/) property returns **true**.

## **Sample Code**

The following sample code loads the [sample Excel file](43352065.xlsm) and checks if the VBA (Visual Basic for Applications) Project of the Excel file is protected and locked for viewing. Please also see its console output as a reference.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCheckifVBAProjectisProtected.xlsm";

    // Load your source Excel file
    Workbook wb(inputFilePath);

    // Access the VBA project of the workbook
    VbaProject vbaProject = wb.GetVbaProject();

    // Check whether the "Lock project for viewing" setting is true
    std::cout << "Is VBA Project Locked for Viewing: " << vbaProject.GetIslockedForViewing() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Console Output**

This is the console output of the above sample code when executed with the provided [sample Excel file](43352065.xlsm).

{{< highlight cpp >}}
Is VBA Project Locked for Viewing: True
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
