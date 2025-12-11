---
title: Expanding text from right to left while exporting Excel files to HTML with C++
linktitle: Expanding text from right to left while exporting Excel files to HTML
type: docs
weight: 60
url: /cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
description: Learn how to expand text from right to left while exporting Excel files to HTML using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells for C++ now supports expanding text from right to left while exporting Excel files to HTML. This feature has been implemented since v8.9.0.0. If your source Excel file contains any text that expands from right to left, Aspose.Cells will export it to HTML correctly.

{{% /alert %}} 

## **Expanding text from right to left while exporting Excel files to HTML**

The following sample code converts the [sample Excel file](5115502.xlsx) into HTML. This screenshot shows how the sample Excel file looks in Microsoft Excel 2013.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

This screenshot shows the [output HTML generated with the older version](5115509).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

This screenshot shows the [output HTML generated with the newer version](5115508).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

As you can see in the screenshots, the newer version expands the right‑aligned text to the left correctly, just like Microsoft Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file into the workbook object
    Workbook wb(srcDir + u"sample.xlsx");

    // Save workbook in HTML format
    U16String outputPath = srcDir + u"ExpandTextFromRightToLeft_out_" + CellsHelper::GetVersion() + u".html";
    wb.Save(outputPath, SaveFormat::Html);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
