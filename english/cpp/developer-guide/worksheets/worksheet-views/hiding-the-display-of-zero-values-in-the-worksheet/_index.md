---
title: Hiding the Display of Zero Values in the Worksheet with C++
linktitle: Hiding the Display of Zero Values in the Worksheet
type: docs
weight: 50
url: /cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: This article will show you sample code explaining how to programmatically hide the zero values in an Excel spreadsheet using the C++ library or API.
keywords: hide zero values of excel worksheet in C++
---

{{% alert color="primary" %}} 

Sometimes, you need to hide zero values in a spreadsheet. It might be a personal preference or a formatting standard.

{{% /alert %}} 

To hide zero values in a worksheet in Microsoft Excel (for example Microsoft Excel 2003):

1. From the **Tools** menu, select **Options**, and then select the **View** tab.
1. Deselect the **Zero values** option.
1. Click **OK**.

Please see the following sample code that demonstrates hiding zeros using Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create a new Workbook object
    Workbook workbook(inputFilePath);

    // Get First worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Hide the zero values in the sheet
    sheet.SetDisplayZeros(false);

    // Save the workbook
    workbook.Save(srcDir + u"outputfile.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}