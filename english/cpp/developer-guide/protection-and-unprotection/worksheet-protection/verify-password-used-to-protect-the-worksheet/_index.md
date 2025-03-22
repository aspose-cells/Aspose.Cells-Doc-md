---
title: Verify Password Used to Protect the Worksheet with C++
linktitle: Verify Password Used to Protect the Worksheet
type: docs
weight: 370
url: /cpp/verify-password-used-to-protect-the-worksheet/
description: Learn how to verify the password used to protect a worksheet using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells APIs have enhanced the [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) class by introducing some useful properties & methods. One such method is the [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) which allows specifying a password as an instance of *string* and verifies if the same password has been used to protect the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

{{% /alert %}}

The [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) method returns **true** if the specified password matches the password used to protect the given worksheet and **false** if the specified password does not match. The following piece of code uses the [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) method in conjunction with [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) property to detect the password protection, and verifies the password.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"Sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        // Verify the password used to protect the Worksheet
        if (sheet.GetProtection().VerifyPassword(u"1234"))
        {
            std::cout << "Specified password has matched" << std::endl;
        }
        else
        {
            std::cout << "Specified password has not matched" << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```