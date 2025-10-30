---
title: Verifiera Lösenord för att Skydda Arket med C++
linktitle: Verifiera lösenord som används för att skydda arbetsbladet
type: docs
weight: 370
url: /sv/cpp/verify-password-used-to-protect-the-worksheet/
description: Lär dig hur du verifierar lösenordet som används för att skydda ett ark med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells API:er har förbättrat [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) klassen genom att införa några användbara egenskaper och metoder. En sådan metod är [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) som tillåter att ange ett lösenord som en instans av *string* och verifierar om samma lösenord har använts för att skydda [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

{{% /alert %}}

[**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) metoden returnerar **true** om det angivna lösenordet matchar det som används för att skydda det angivna arket och **false** annars. Koden nedan använder [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) metod i samband med [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) egenskap för att upptäcka lösenordsskydd och verifierar lösenordet.

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
{{< app/cells/assistant language="cpp" >}}
