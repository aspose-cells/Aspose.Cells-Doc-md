---
title: Encontrar si el valor de la celda empieza con comilla simple con C++
linktitle: Encontrar si el valor de la celda comienza con un signo de comilla simple
type: docs
weight: 270
url: /es/cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Aprende cómo encontrar si el valor de la celda comienza con una comilla simple mediante la API Aspose.Cells for C++.
keywords: Encontrar valor de celda que comienza con un signo de comilla simple, Buscar valor de celda que comienza con un signo de comilla simple
---

{{% alert color="primary" %}}

Ahora Aspose.Cells proporciona la propiedad [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) para encontrar si el valor de la celda comienza con un signo de comilla simple. Antes de esta propiedad, no había forma de distinguir entre cadenas como ejemplo y 'ejemplo, etc.

{{% /alert %}}

El siguiente código de muestra explica que las cadenas como ejemplo y 'ejemplo no se pueden diferenciar con la propiedad [**Cell::GetStringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/). Por lo tanto, debemos usar la propiedad [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) para distinguirlas.

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
