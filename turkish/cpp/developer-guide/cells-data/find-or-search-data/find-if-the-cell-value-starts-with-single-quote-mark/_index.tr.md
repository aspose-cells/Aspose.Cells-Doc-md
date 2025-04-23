---
title: Hücre değeri tek tırnak işaretiyle başlıyorsa, C++ ile bulma
linktitle: Hücre değerinin tek tek tırnak işaretiyle başlayıp başlamadığını bul
type: docs
weight: 270
url: /tr/cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Aspose.Cells for C++ API’sini kullanarak hücre değeri tek tırnakla başlıyor mu, diye nasıl bakacağınızı öğrenin.
keywords: Hücre değerinin tek tek tırnak işaretiyle başlayıp başlamadığını bulmak için şimdi Aspose.Cells {0} özelliğini sağlar. Bu özelliğin öncesinde, örnek ve örnek gibi örneğin gibi stringler arasında ayrım yapmanın bir yolu yoktu.
---

{{% alert color="primary" %}}

Aşağıdaki örnek kod, 'örnek' ve 'örnek gibi örneğin' gibi stringler arasında ayrım yapmanın {0} özelliği ile mümkün olamayacağını açıklar. Bu nedenle, onları ayırt etmek için {1} özelliğini kullanmalıyız.

{{% /alert %}}

Aşağıdaki örnek kod, örnek ve 'örnek gibi dizilerin [**Cell::GetStringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) özelliği ile ayırt edilemeyeceğini açıklar. Bu nedenle onları ayırt etmek için [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) özelliğini kullanmamız gerekir.

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
