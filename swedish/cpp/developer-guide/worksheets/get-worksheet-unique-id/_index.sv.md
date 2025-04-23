---
title: Hämta unikt arbetsblads ID med C++
linktitle: Hämta unikt arbetsblads ID
type: docs
weight: 190
url: /sv/cpp/get-worksheet-unique-id/
description: Den här artikeln visar hur man hämtar Excel arkets unika ID med C++ bibliotek och API programmering.
keywords: Unikt ID för Excel ark, unikt ID för arbetsblad C++
---

## **Hämta unikt arbetsblads-ID**

Aspose.Cells ger möjlighet att hämta det unika ID:t för ett arbetsblad med hjälp av [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/)-metoden. Följande kodexempel visar användningen av [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/)-metoden för att skriva ut det unika ID:t för ett arbetsblad. Detta exempel använder denna [exempel Excel-fil](105480213.xlsx).

### Källkod

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
