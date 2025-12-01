---
title: Copy Page Setup Settings from Source Worksheet into Destination Worksheet with C++
linktitle: Copy Page Setup Settings
type: docs
weight: 80
url: /cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: This article explains how to use the C++ API or Library sample code to copy Page Setup settings from source Worksheet into destination Worksheet programmatically.
keywords: copy page setup settings c++, copy page setup settings to target worksheet c++
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When you add a new sheet to a workbook, it contains the default *Page Setup settings*. There may be times when you need to transfer the settings ([**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)) from one worksheet to another worksheet. This document explains how to copy Page Setup settings from one worksheet to another using Aspose.Cells APIs.

## **Copy Page Setup Settings from Source Worksheet into Destination Worksheet**

The following sample code illustrates how to copy *Page Setup settings* from one worksheet to another using [**PageSetup.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/copy/) method. Please see the following sample code and its console output for a reference.

## **Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    wb.GetWorksheets().Add(u"TestSheet1");
    wb.GetWorksheets().Add(u"TestSheet2");

    Worksheet TestSheet1 = wb.GetWorksheets().Get(u"TestSheet1");
    Worksheet TestSheet2 = wb.GetWorksheets().Get(u"TestSheet2");

    TestSheet1.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3ExtraTransverse);

    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    CopyOptions copyOptions;
    TestSheet2.GetPageSetup().Copy(TestSheet1.GetPageSetup(), copyOptions);

    std::cout << "After Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "After Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Console Output**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
