---
title: Passwort zum Ändern in Aspose.Cells mit C++ prüfen
linktitle: Passwort zum Ändern prüfen
type: docs
weight: 2400
url: /de/cpp/check-password-to-modify-using-aspose-cells/
description: Prüfen, ob das angegebene Passwort mit dem Passwort zum Ändern übereinstimmt, mit Aspose.Cells für C++.
---

{{% alert color="primary" %}}

Manchmal müssen Sie programmatisch prüfen, ob das angegebene Passwort mit dem **Passwort zum Ändern** übereinstimmt. Aspose.Cells bietet die Methode WorkbookSettings.WriteProtection.ValidatePassword(), die Sie verwenden können, um zu prüfen, ob das Passwort zum Ändern korrekt ist oder nicht.

{{% /alert %}}

## **Passwort zum Ändern in Microsoft Excel überprüfen**

Sie können beim Erstellen Ihrer Arbeitsbücher in Microsoft Excel **Passwort zum Öffnen** und **Passwort zum Ändern** zuweisen. Bitte sehen Sie sich diesen Screenshot an, der die Benutzeroberfläche zeigt, die Microsoft Excel zum Angeben dieser Passwörter bereitstellt.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Überprüfen Sie das Kennwort zur Änderung mit Aspose.Cells**

Die folgenden Beispielscodes laden die [Quell-Excel](5112232.xlsx)-Datei. Sie hat ein Passwort zum Öffnen als 1234 und ein Passwort zum Ändern als 5678. Der Code überprüft zunächst, ob 567 das richtige Passwort zum Ändern ist, und gibt false zurück, und dann überprüft er, ob 5678 das Passwort zum Ändern ist, und gibt true zurück.

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

### **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielscodes nach dem Laden der [Quell-Excel](5112232.xlsx)-Datei.

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
