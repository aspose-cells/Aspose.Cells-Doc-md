---
title: Duplikate Zeilen in einem Arbeitsblatt mit C++ entfernen
linktitle: Doppelte Zeilen in einem Arbeitsblatt entfernen
type: docs
weight: 370
url: /de/cpp/remove-duplicate-rows-in-a-worksheet/
description: Lernen Sie, wie Sie doppelte Zeilen in einem Arbeitsblatt mit Aspose.Cells for C++ entfernen.
---

{{% alert color="primary" %}}

Das Entfernen doppelter Zeilen ist eine von Microsoft Excel viele nützlichen Funktionen. Es ermöglicht Benutzern, doppelte Zeilen in einem Arbeitsblatt zu entfernen, und Sie können auswählen, welche Spalten auf doppelte Informationen überprüft werden sollen.

Aspose.Cells bietet die Methode `Cells::RemoveDuplicates()` für diesen Zweck. Sie können auch `startRow`, `startColumn`, `endRow` und `endColumn` festlegen, um Spalten auszuwählen.

Hier sind die Beispiel Dateien, die heruntergeladen werden können, um diese Funktion zu testen:

[removeduplicates.xlsx](removeduplicates.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook book(u"removeduplicates.xlsx");

    // Remove duplicates from the first worksheet
    book.GetWorksheets().Get(0).GetCells().RemoveDuplicates(0, 0, 5, 3);

    // Save the result
    book.Save(u"removeduplicates-result.xlsx");

    std::cout << "Duplicates removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% /alert %}}
