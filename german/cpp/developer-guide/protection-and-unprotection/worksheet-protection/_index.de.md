---
title: Arbeitsblatt mit C++ schützen und entsperren
linktitle: Arbeitsblatt schützen und entschützen
type: docs
weight: 40
url: /de/cpp/protect-and-unprotect-worksheets/
description: Arbeitsblatt von Excel Dateien mit {Aspose.Cells for C++} schützen und entsperren.
---

{{% alert color="primary" %}}
Um zu verhindern, dass andere Benutzer versehentlich oder absichtlich Daten in einem Arbeitsblatt ändern, verschieben oder löschen, können Sie die Zellen in Ihrem Excel-Arbeitsblatt sperren und das Blatt dann mit einem Kennwort schützen. 
{{% /alert %}}

## **Arbeitsblatt in MS Excel schützen und entsperren**

**![Arbeitsblatt schützen und aufheben](schuetzen-und-aufheben.png)**

1. Klicken Sie auf **Überprüfen > Arbeitsblatt schützen**.
1. Geben Sie ein Passwort in das **Passwortfeld** ein.
1. Wählen Sie die **Zulassen**-Optionen aus.
1. Wählen Sie **OK**, geben Sie das Passwort erneut ein, um es zu bestätigen, und wählen Sie dann erneut **OK**.

## **Arbeitsblatt mit {Aspose.Cells for C++} schützen**
Es sind nur die folgenden einfachen Codezeilen erforderlich, um die Arbeitsmappenstruktur von Excel-Dateien zu schützen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Protect contents of the worksheet
    sheet.Protect(ProtectionType::Contents);

    // Protect worksheet with password
    sheet.GetProtection().SetPassword(u"test");

    // Save as Excel file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Arbeitsblatt mit {Aspose.Cells for C++} entsperren**
Das Aufheben des Arbeitsblatts ist mit der Aspose.Cells-API einfach. Wenn das Arbeitsblatt passwortgeschützt ist, ist ein korrektes Kennwort erforderlich.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Unprotect the worksheet with password
    sheet.Unprotect(u"password");

    // Save the workbook
    workbook.Save(u"Book1.xlsx");

    std::cout << "Worksheet unprotected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Erweiterte Schutzeinstellungen seit Excel XP](/cells/de/cpp/advanced-protection-settings-since-excel-xp/)
- [Überprüfen Sie, ob das Arbeitsblatt mit einem Kennwort geschützt ist](/cells/de/cpp/detect-if-worksheet-is-password-protected/)
- [Arbeitsblätter schützen](/cells/de/cpp/protecting-worksheets/)
- [Arbeitsblatt entsperren](/cells/de/cpp/unprotect-a-worksheet/)
- [Überprüfen Sie das verwendete Kennwort zum Schutz des Arbeitsblatts](/cells/de/cpp/verify-password-used-to-protect-the-worksheet/)
{{< app/cells/assistant language="cpp" >}}
