---
title: Determine if Paper Size of Worksheet is Automatic with C++
linktitle: Determine if Paper Size of Worksheet is Automatic
type: docs
weight: 90
url: /cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: This article explains how to use the C++ API or library sample code to determine if Paper Size of Worksheet is Automatic programmatically.
keywords: determine if paper size of worksheet automatic c++
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Most of the time, the paper size of the worksheet is automatic. When it is automatic, it is often set as *Letter*. Sometimes the user sets the paper size of the worksheet as per their requirements. In this case, the paper size is not automatic. You can find if the worksheet paper size is automatic or not using the [**PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/isautomaticpapersize/) property of the **Worksheet** class.

## **Determine if Paper Size of Worksheet is Automatic**

The sample code given below loads the following two Excel files

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

and finds if the paper size of their first worksheet is automatic or not. In Microsoft Excel, you can check if the paper size is automatic or not via the Page Setup window as shown in this screenshot.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the first workbook having automatic paper size false
    Workbook wb1(sourceDir + u"samplePageSetupIsAutomaticPaperSize-False.xlsx");

    // Load the second workbook having automatic paper size true
    Workbook wb2(sourceDir + u"samplePageSetupIsAutomaticPaperSize-True.xlsx");

    // Access the first worksheet of both workbooks
    Worksheet ws11 = wb1.GetWorksheets().Get(0);
    Worksheet ws12 = wb2.GetWorksheets().Get(0);

    // Print the PageSetup.IsAutomaticPaperSize property of both worksheets
    std::wcout << u"First Worksheet of First Workbook - IsAutomaticPaperSize: " << ws11.GetPageSetup().IsAutomaticPaperSize() << std::endl;
    std::wcout << u"First Worksheet of Second Workbook - IsAutomaticPaperSize: " << ws12.GetPageSetup().IsAutomaticPaperSize() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Console Output**

Here is the console output of the above sample code when executed with the given sample Excel files.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
