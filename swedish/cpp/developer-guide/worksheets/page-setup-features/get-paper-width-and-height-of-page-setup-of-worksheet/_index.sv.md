---
title: Hämta papper bredd och höjd för sidsetup på arbetsbladet med C++
linktitle: Hämta papper bredd och höjd för sidsetup
type: docs
weight: 50
url: /sv/cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Lär dig hur du with C++ kan hämta Excel Arbetsbladets sidsetup papper bredd och papper höjd programmässigt med Aspose.Cells for C++ API.
keywords: excel sidsetup pappersbredd c++, excel sidsetup pappershöjd c++
---

## **Möjliga användningsscenario**

Ibland behöver du veta bredden och höjden på pappersstorleken som har ställts in i sidsetupen för arbetsbladet. Använd [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) och [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/)-metoderna för detta ändamål.

## **Hämta pappersbredd och höjd i sidinställningen för kalkylblad**

Följande exempel kod förklarar användningen av [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) och [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/)-metoderna. Den ändrar först pappersstorleken till *A2* och hittar sedan bredden och höjden på papperet, därefter ändrar den till *A3*, *A4*, *Letter* och finner bredden och höjden på papperet respektive.

### **Exempelkod**

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

### **Konsoloutput**

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
