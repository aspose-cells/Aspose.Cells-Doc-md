---
title: Get Hyperlinks in Range with C++
linktitle: Get Hyperlinks in Range
type: docs
weight: 100
url: /cpp/get-hyperlinks-in-range/
description: Learn how to get hyperlinks in range through the Aspose.Cells for C++ API.
keywords: Get Hyperlinks in Range, Get all the hyperlinks in the selected range, Delete hyperlink in Range, Delete the hyperlinks in the selected range
---

## **Get Hyperlinks in Range**

The [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) class provides a [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/gethyperlinks/) property which returns all the hyperlinks in the selected range. You may also delete the Hyperlink by calling the [**Hyperlink.Delete**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/delete/) method.

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