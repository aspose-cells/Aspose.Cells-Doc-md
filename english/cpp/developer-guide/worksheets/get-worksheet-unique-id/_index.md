---
title: Get Worksheet Unique ID with C++
linktitle: Get Worksheet Unique ID
type: docs
weight: 190
url: /cpp/get-worksheet-unique-id/
description: This article shows how to get Excel worksheet unique ID using C++ library and API programmatically.
keywords: unique ID Excel worksheet C++, unique ID worksheet C++
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Get Worksheet Unique ID**

Aspose.Cells provides the ability to get the unique ID of a worksheet by using the [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/) method. The following code snippet demonstrates the use of the [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/) method to print the unique ID of a worksheet. The following code snippet uses this [sample excel file](105480213.xlsx).

### Source Code

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
