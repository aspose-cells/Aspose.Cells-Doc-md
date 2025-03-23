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

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a Workbook object and open an Excel file
    Workbook workbook(srcDir + u"HyperlinksSample.xlsx");

    // Get the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range A2:B3
    Range range = worksheet.GetCells().CreateRange(u"A2", u"B3");

    // Get Hyperlinks in range
    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();

    // Iterate through hyperlinks and print their details
    for (const Hyperlink& link : hyperlinks)
    {
        std::cout << link.GetArea().ToString().ToUtf8() << " : " << link.GetAddress().ToUtf8() << std::endl;

        // To delete the link, use the Hyperlink.Delete() method
        link.Delete();
    }

    // Save the workbook
    workbook.Save(outDir + u"HyperlinksSample_out.xlsx");

    std::cout << "Hyperlinks processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```