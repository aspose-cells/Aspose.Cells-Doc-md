---
title: Åtkomst till Text Box via Namn med C++
linktitle: Tillgång till textfältet genom namnet
type: docs
weight: 230
url: /sv/cpp/access-the-text-box-by-the-name/
description: Lär dig hur man får åtkomst till en text box via dess namn med Aspose.Cells for C++.
---

## Åtkomst till textlådan med namnet

Tidigare kunde textlådor nås via index från [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/)-samlingen, men nu kan du också få åtkomst till textlådan via dess namn i denna samling. Det är ett bekvämt och snabbt sätt att få åtkomst till din textlåda om du redan känner till dess namn.

Följande exempel kod skapar först en text låda och tilldelar den text och ett namn. Sedan, i nästa steg, får vi åtkomst till samma textlåda via dess namn och skriver ut dess text.

### C++-kod för att få åtkomst till textlådan via namn

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    int idx = sheet.GetTextBoxes().Add(10, 10, 10, 10);

    // Access newly created TextBox using its index & name it
    TextBox tb1 = sheet.GetTextBoxes().Get(idx);
    tb1.SetName(u"MyTextBox");

    // Set text for the TextBox
    tb1.SetText(u"This is MyTextBox");

    // Access the same TextBox via its name
    TextBox tb2 = sheet.GetTextBoxes().Get(u"MyTextBox");

    // Display the text of the TextBox accessed via name
    std::cout << tb2.GetText().ToUtf8() << std::endl;

    std::cout << "Press any key to continue..." << std::endl;
    std::cin.get();

    Aspose::Cells::Cleanup();
}
```

### Konsoloutput som genereras av provkoden

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
