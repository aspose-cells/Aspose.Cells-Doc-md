---
title: Erkennen, ob ein Arbeitsblatt passwortgeschützt ist mit C++
linktitle: Erkennen, ob Arbeitsblatt passwortgeschützt ist
type: docs
weight: 360
url: /de/cpp/detect-if-worksheet-is-password-protected/
description: Erfahren Sie, wie man erkennt, ob ein Arbeitsblatt mit Aspose.Cells for C++ passwortgeschützt ist.
---

{{% alert color="primary" %}}

Es ist möglich, Arbeitsmappen und Arbeitsblätter separat zu schützen. Zum Beispiel kann eine Tabelle ein oder mehrere passwortgeschützte Arbeitsblätter enthalten, die Tabelle selbst jedoch möglicherweise nicht geschützt sein. Die APIs von Aspose.Cells bieten die Mittel, um festzustellen, ob ein bestimmtes Arbeitsblatt passwortgeschützt ist oder nicht. Dieser Artikel zeigt die Nutzung der API Aspose.Cells for C++, um dasselbe zu erreichen.

{{% /alert %}}

Aspose.Cells for C++ hat die Eigenschaft [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) freigegeben, um zu erkennen, ob ein Arbeitsblatt passwortgeschützt ist oder nicht. Die boolesche Eigenschaft [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) gibt **true** zurück, wenn [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) passwortgeschützt ist, und **false**, wenn nicht.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        std::cout << "Worksheet is password protected" << std::endl;
    }
    else
    {
        std::cout << "Worksheet is not password protected" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
