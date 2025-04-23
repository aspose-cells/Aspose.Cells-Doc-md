---
title: Prüfen, ob der Zellwert mit einfachem Anführungszeichen beginnt, mit C++
linktitle: Überprüfen Sie, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt
type: docs
weight: 270
url: /de/cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Erfahren Sie, wie Sie mit der API Aspose.Cells for C++ feststellen, ob der Zellwert mit einem einzelnen Anführungszeichen beginnt.
keywords: Prüfen Sie, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt. Suchen Sie den Zellenwert, der mit einem einfachen Anführungszeichen beginnt.
---

{{% alert color="primary" %}}

Aspose.Cells bietet jetzt die [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) Eigenschaft, um zu überprüfen, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt. Vor dieser Eigenschaft gab es keine Möglichkeit, zwischen Zeichenfolgen wie Muster und 'Muster usw. zu unterscheiden.

{{% /alert %}}

Der folgende Beispielcode erklärt, dass die Zeichenfolgen wie Muster und 'Muster nicht mit der [**Cell::GetStringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/)-Eigenschaft differenziert werden können. Daher müssen wir die [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/)-Eigenschaft verwenden, um sie zu unterscheiden.

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
