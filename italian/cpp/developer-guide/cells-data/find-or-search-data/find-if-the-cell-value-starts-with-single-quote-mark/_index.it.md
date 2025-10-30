---
title: Trova se il valore della cella inizia con il simbolo di singolo apice con C++
linktitle: Verifica se il valore della cella inizia con un apice singolo
type: docs
weight: 270
url: /it/cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Scopri come trovare se il valore della cella inizia con un simbolo di apice singolo tramite l API Aspose.Cells for C++.
keywords: Trova il valore della cella che inizia con un singolo segno di citazione, Cerca il valore della cella che inizia con un singolo segno di citazione
---

{{% alert color="primary" %}}

Aspose.Cells ora fornisce la proprietà [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) per trovare se il valore della cella inizia con un singolo segno di citazione. Prima di questa proprietà, non c'era modo di distinguere tra stringhe come campione e 'campione ecc.

{{% /alert %}}

Il seguente codice di esempio spiega che le stringhe come campione e 'campione non possono essere differenziate con la proprietà [**Cell::GetStringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/). Pertanto, dobbiamo utilizzare la proprietà [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) per distinguerle.

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
