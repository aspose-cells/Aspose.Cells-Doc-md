---
title: Check Password to modify using Aspose.Cells with C++
linktitle: Check Password to modify
type: docs
weight: 2400
url: /cpp/check-password-to-modify-using-aspose-cells/
description: Check if the given password matches the Password to modify using Aspose.Cells with C++.
---

{{% alert color="primary" %}}

Sometimes, you need to check if the given password matches the **Password to modify** programmatically. Aspose.Cells provides WorkbookSettings.WriteProtection.ValidatePassword() method which you can use to check if the given Password to modify is correct or not.

{{% /alert %}}

## **Check Password to modify in Microsoft Excel**

You can assign **Password to open** and **Password to modify** while creating your workbooks in Microsoft Excel. Please see this screenshot which shows the interface Microsoft Excel provides to specify these passwords.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Check Password to modify using Aspose.Cells**

The following sample codes load the [source Excel](5112232.xlsx) file. It has a Password to open as 1234 and Password to modify as 5678. The code first checks if 567 is correct Password to modify and it returns false and then it checks if 5678 is Password to modify and it returns true.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleBook.xlsx";

    // Specify password to open inside the load options
    LoadOptions opts;
    opts.SetPassword(u"1234");

    // Open the source Excel file with load options
    Workbook workbook(inputFilePath, opts);

    // Check if "567" is the password to modify
    bool ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"567");
    std::wcout << L"Is 567 correct Password to modify: " << ret << std::endl;

    // Check if "5678" is the password to modify
    ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"5678");
    std::wcout << L"Is 5678 correct Password to modify: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Console Output**

Here is the Console Output of the above sample code after loading the [source Excel](5112232.xlsx) file.

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}