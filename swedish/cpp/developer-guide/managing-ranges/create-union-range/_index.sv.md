---
title: Skapa unionsområde med C++
linktitle: Skapa Union Range
type: docs
weight: 360
url: /sv/cpp/create-union-range/
description: Skapa unionsområde i Excel filer med Aspose.Cells och C++.
---

## **Skapa unionsspann**
Aspose.Cells ger möjligheten att skapa unionsområde med hjälp av [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/) metoden. [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/) tar två parametrar, adressen för att skapa unionsområdet och index för kalkylbladet. Metoden returnerar ett [UnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/unionrange/)-objekt.

Följande kodsnutt demonstrerar skapandet av ett unionsområde med [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/). Den genererade utdatafilen är bifogad för referens.

- [Utdatafil](106364952.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Create union range
    UnionRange unionRange = workbook.GetWorksheets().CreateUnionRange(u"sheet1!A1:A10,sheet1!C1:C10", 0);

    // Put value "ABCD" in the range
    unionRange.SetValue(u"ABCD");

    // Save the output workbook
    workbook.Save(u"CreateUnionRange_out.xlsx");

    std::cout << "Union range created and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
