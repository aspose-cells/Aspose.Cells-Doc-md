---
title: Ta bort dubblettrader i ett kalkblad med C++
linktitle: Ta bort dubblettrader i ett arbetsblad
type: docs
weight: 370
url: /sv/cpp/remove-duplicate-rows-in-a-worksheet/
description: Lära dig hur man tar bort dubblettrader i ett kalkblad med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Att ta bort dubblettrader är en av Microsoft Excels många användbara funktioner. Det tillåter användare att ta bort dubblettrader i ett kalkblad, och du kan välja vilka kolumner som ska kontrolleras för dubblettinformation.

Aspose.Cells tillhandahåller metoden `Cells::RemoveDuplicates()` för detta ändamål. Du kan även ställa in `startRow`, `startColumn`, `endRow` och `endColumn` för att välja kolumner.

Följande är provfiler som kan laddas ned för att testa denna funktion:

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
{{< app/cells/assistant language="cpp" >}}
