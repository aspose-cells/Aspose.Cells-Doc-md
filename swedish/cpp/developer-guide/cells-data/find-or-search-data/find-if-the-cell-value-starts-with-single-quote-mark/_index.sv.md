---
title: Hitta om cellvärdet börjar med enkel citattecken med C++
linktitle: Ta reda på om cellvärdet börjar med citattecken
type: docs
weight: 270
url: /sv/cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Lär dig hur du hittar om cellvärdet börjar med ett enkelt citattecken via API et Aspose.Cells for C++.
keywords: Hitta cellvärde som börjar med ett enkelt citattecken, Sök cellvärde som börjar med ett enkelt citattecken
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller nu egenskapen [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) för att hitta om cellvärdet börjar med ett enkelt citattecken. Innan denna egenskap fanns det inget sätt att skilja mellan strängar som exempelvis sample och 'sample osv.

{{% /alert %}}

Följande exempelkod förklarar att strängar som exempelvis sample och 'sample inte kan skiljas åt med egenskapen [**Cell::GetStringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/). Därför måste vi använda egenskapen [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) för att skilja dem åt.

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
