---
title: Find if the cell value starts with single quote mark with C++
linktitle: Find if the cell value starts with single quote mark
type: docs
weight: 270
url: /cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Learn how to find if the cell value starts with a single quote mark through the Aspose.Cells for C++ API.
keywords: Find cell value starts with a single quote mark, Search cell value starts with a single quote mark
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells now provides the [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) property to find if the cell value starts with a single quote mark. Before this property, there was no way to distinguish between strings like sample and 'sample etc.

{{% /alert %}}

The following sample code explains that the strings like sample and 'sample cannot be differentiated with [**Cell::GetStringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) property. Therefore we must use [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) property to distinguish them.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Create worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Access cell A1 and A2
    Cell a1 = sheet.GetCells().Get(u"A1");
    Cell a2 = sheet.GetCells().Get(u"A2");

    // Add sample in A1 and sample with quote prefix in A2
    a1.PutValue(u"sample");
    a2.PutValue(u"'sample");

    // Print their string values, A1 and A2 both are same
    std::cout << "String value of A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "String value of A2: " << a2.GetStringValue().ToUtf8() << std::endl;

    // Access styles of A1 and A2
    Style s1 = a1.GetStyle();
    Style s2 = a2.GetStyle();

    std::cout << std::endl;

    // Check if A1 and A2 has a quote prefix
    std::cout << "A1 has a quote prefix: " << s1.GetQuotePrefix() << std::endl;
    std::cout << "A2 has a quote prefix: " << s2.GetQuotePrefix() << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
