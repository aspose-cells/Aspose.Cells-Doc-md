---
title: Passwort, das zum Schutz des Arbeitsblatts verwendet wurde, mit C++ überprüfen
linktitle: Das Verifizieren des zum Schutz des Arbeitsblatts verwendeten Passworts
type: docs
weight: 370
url: /de/cpp/verify-password-used-to-protect-the-worksheet/
description: Erfahren Sie, wie man das zum Schutz eines Arbeitsblatts verwendete Passwort mit Aspose.Cells for C++ überprüft.
---

{{% alert color="primary" %}}

Die Aspose.Cells-APIs haben die Klasse [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) durch die Einführung einiger nützlicher Eigenschaften und Methoden verbessert. Eine solche Methode ist die [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/), die die Angabe eines Passworts als Instanz von *string* ermöglicht und überprüft, ob dasselbe Passwort zum Schutz des [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) verwendet wurde.

{{% /alert %}}

Die Methode [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) gibt **true** zurück, wenn das angegebene Passwort mit dem zum Schutz des Arbeitsblatts verwendeten Passwort übereinstimmt, und **false**, wenn es nicht übereinstimmt. Der folgende Code verwendet die Methoden [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) und die Eigenschaft [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/), um den Passwortschutz zu erkennen und das Passwort zu überprüfen.

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
