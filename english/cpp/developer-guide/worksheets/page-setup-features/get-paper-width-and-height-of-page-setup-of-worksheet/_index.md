---
title: Get Paper Width and Height of Page Setup of Worksheet with C++
linktitle: Get Paper Width and Height of Page Setup
type: docs
weight: 50
url: /cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Learn how to get the Excel Worksheet Page Setup paper width and paper height using C++ code programmatically with Aspose.Cells for C++ API.
keywords: excel page setup paper width c++, excel page setup paper height c++
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Sometimes, you need to know the width and height of a paper size as set in the page setup of the worksheet. Please use the [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) and [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/) methods for this purpose.

## **Get Paper Width and Height of Page Setup of Worksheet**

The following sample code demonstrates the usage of [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) and [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/) methods. It first changes the paper size to *A2* and prints the width and height of the paper, then changes it to *A3*, *A4*, and *Letter*, printing the corresponding dimensions each time.

### **Sample Code**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook class
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Set paper size to A2 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA2);
    cout << "PaperA2: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A3 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3);
    cout << "PaperA3: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A4 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);
    cout << "PaperA4: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to Letter and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperLetter);
    cout << "PaperLetter: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Console Output**

Here is the console output of the above sample code.

{{< highlight cpp >}}
PaperA2: 16.54x23.39
PaperA3: 11.69x16.54
PaperA4: 8.27x11.69
PaperLetter: 8.5x11
{{< /highlight >}}
