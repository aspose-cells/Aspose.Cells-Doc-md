---
title: Eindeutige ID des Arbeitsblatts mit C++ abrufen
linktitle: Arbeitsblatt Eindeutige ID abrufen
type: docs
weight: 190
url: /de/cpp/get-worksheet-unique-id/
description: Dieser Artikel zeigt, wie man die eindeutige ID eines Excel Arbeitsblatts mithilfe der C++ Bibliothek und API programmgesteuert erhält.
keywords: eindeutige ID Excel Arbeitsblatt C++, eindeutige ID Arbeitsblatt C++, C++
---

## **Arbeitsblatt Eindeutige ID abrufen**

Aspose.Cells bietet die Möglichkeit, die eindeutige ID eines Arbeitsblatts mit der Methode [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/) abzurufen. Das folgende Codebeispiel demonstriert die Verwendung der [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/)-Methode, um die eindeutige ID eines Arbeitsblatts zu drucken. Das folgende Codebeispiel verwendet diese [Beispiel-Excel-Datei](105480213.xlsx).

### Quellcode

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print Unique Id
    std::cout << "Unique Id: " << worksheet.GetUniqueId().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
