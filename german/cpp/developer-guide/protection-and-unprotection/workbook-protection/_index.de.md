---
title: Arbeitsmappe Struktur mit C++ schützen und entsperren
linktitle: Arbeitsmappenstruktur schützen und entschützen
type: docs
weight: 40
url: /de/cpp/protect-and-unprotect-workbook-structure/
description: Schützen und entsperren Sie die Arbeitsmappe Struktur von Excel Dateien mit C++ und Aspose.Cells.
---

{{% alert color="primary" %}}
Um zu verhindern, dass andere Benutzer versteckte Arbeitsblätter einsehen, Arbeitsblätter hinzufügen, verschieben, löschen oder ausblenden und Arbeitsblätter umbenennen, können Sie die Struktur Ihres Excel-Arbeitsblatts mit einem Kennwort schützen.
{{% /alert %}}

## **Arbeitsmappe-Struktur in MS Excel schützen und entsperren**

**![Arbeitsmappenstruktur schützen und entschützen](schuetzen-und-entschuetzen-arbeitsmappenstruktur.png)**

1. Klicken Sie auf **Überprüfen > Arbeitsmappe schützen**.
1. Geben Sie ein Passwort in das **Passwortfeld** ein.
1. Wählen Sie **OK**, geben Sie das Passwort erneut ein, um es zu bestätigen, und wählen Sie dann erneut **OK**.

## **Arbeitsmappe-Struktur mit {Aspose.Cells for C++} schützen**
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

    // Protect workbook structure with a password
    workbook.Protect(ProtectionType::Structure, u"password");

    // Save the workbook to a file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Arbeitsmappe-Struktur mit {Aspose.Cells for C++} entsperren**
Die Entschützung der Arbeitsmappenstruktur ist mit der Aspose.Cells API einfach.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open an Excel file which workbook structure is protected.
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Unprotect workbook structure.
    workbook.Unprotect(u"password");

    // Save Excel file.
    workbook.Save(inputFilePath);

    std::cout << "Workbook structure unprotected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}
Hinweis: Ein korrektes Passwort ist erforderlich.
{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
