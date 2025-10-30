---
title: Hämta hyperlänkar i område med C++
linktitle: Få hyperlänkar inom intervall
type: docs
weight: 100
url: /sv/cpp/get-hyperlinks-in-range/
description: Lär dig hur du hämtar hyperlänkar i område via API n Aspose.Cells for C++.
keywords: Få hyperlänkar i område, Få alla hyperlänkar i det valda området, Ta bort hyperlänk i område, Ta bort hyperlänkarna i det valda området
---

## **Hämta hyperlänkar i omfånget**

[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)-klassen tillhandahåller en [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/gethyperlinks/)-egenskap som returnerar alla hyperlänkar inom det valda intervallet. Du kan även ta bort hyperlänken genom att anropa [**Hyperlink.Delete**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/delete/)-metoden.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"HyperlinksSample.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Range range = worksheet.GetCells().CreateRange(u"A2", u"B3");
    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();

    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink& link = hyperlinks[i];
        std::cout << link.GetArea().ToString().ToUtf8() << " : " << link.GetAddress().ToUtf8() << std::endl;
        link.Delete();
    }

    workbook.Save(outDir + u"HyperlinksSample_out.xlsx");
    std::cout << "Hyperlinks processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
