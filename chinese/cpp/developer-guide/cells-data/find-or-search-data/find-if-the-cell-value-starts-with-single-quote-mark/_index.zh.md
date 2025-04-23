---
title: 用C++查找单元格值是否以单引号开始
linktitle: 查找单元格值是否以单引号开始
type: docs
weight: 270
url: /zh/cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: 学习如何使用Aspose.Cells for C++ API查找单元格值是否以单引号开始。
keywords: 查找单元格值是否以单引号标记开始，搜索单元格值是否以单引号标记开始
---

{{% alert color="primary" %}}

Aspose.Cells 现在提供了属性 [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) 来查找单元格值是否以单引号标记开始。在此属性之前，无法区分类似 sample 和 'sample 等字符串。

{{% /alert %}}

下面的示例代码解释了像“sample”和“'sample”这样的字符串不能通过[**Cell::GetStringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/)属性进行区分。因此，我们必须使用[**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/)属性对它们进行区分。

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
