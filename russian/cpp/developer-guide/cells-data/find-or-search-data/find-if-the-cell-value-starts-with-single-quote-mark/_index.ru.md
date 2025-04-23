---
title: Найти, начинается ли значение ячейки с одинарной кавычки, с помощью C++
linktitle: Узнайте, начинается ли значение ячейки с одинарной кавычки через Aspose.Cells для API Python via .NET.
type: docs
weight: 270
url: /ru/cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Узнайте, как определить начинается ли значение ячейки с одинарной кавычки через API Aspose.Cells for C++.
keywords: Найти значение ячейки, начинающееся с одинарного символа кавычки, Поиск значения ячейки, начинающегося с одинарного символа кавычки
---

{{% alert color="primary" %}}

Aspose.Cells теперь предоставляет свойство [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) для проверки, начинается ли значение ячейки с одинарного символа кавычки. До этого свойства не было способа отличить строки, такие как образец и 'образец и т. д.

{{% /alert %}}

В следующем образце кода объясняется, что строки как пример и 'пример не могут быть различены с помощью свойства [**Cell::GetStringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/). Поэтому мы должны использовать свойство [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/), чтобы различать их.

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
