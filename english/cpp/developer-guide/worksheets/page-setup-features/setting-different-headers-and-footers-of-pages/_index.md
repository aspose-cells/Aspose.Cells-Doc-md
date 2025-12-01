---
title: Setting Different Headers and Footers For Different Pages with C++
linktitle: Setting Different Headers and Footers
type: docs
weight: 35
url: /cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: This article provides sample code that shows how to programmatically set various headers and footers of Excel worksheet Page Setup settings using the C++ Library and API. You can set the headers and footers for the first page, odd pages, and even pages.
keywords: set excel header footer first page c++, set excel header footer odd pages c++, set excel header footer even pages c++
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

MS Excel supports setting different headers and footers for the first page, odd pages, and even pages since Excel 2007.
Aspose.Cells supports the same feature.

{{% /alert %}}

## **Setting Different Headers and Footers in MS Excel**

**![Setting Different Headers and Footers](difpage.png)**

1. Click **Page Layout > Print Titles > Header/Footer**.
1. Check **Different Odd and Even Pages** or **Different First Page**.
1. Enter different headers and footers.

## **Setting Different Headers and Footers with Aspose.Cells**

Aspose.Cells behaves the same as Excel.
1. Sets the flags [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdiffoddeven/) and [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdifffirst/) 
1. Enter different headers and footers.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Get the first worksheet's page setup
    PageSetup pageSetup = wb.GetWorksheets().Get(0).GetPageSetup();

    // Set different headers for odd and even pages
    pageSetup.SetIsHFDiffOddEven(true);
    pageSetup.SetHeader(1, u"I am the header of the Odd page.");
    pageSetup.SetEvenHeader(1, u"I am the header of the Even page.");

    // Set a different header for the first page
    pageSetup.SetIsHFDiffFirst(true);
    pageSetup.SetFirstPageHeader(1, u"I am the header of the First page.");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
