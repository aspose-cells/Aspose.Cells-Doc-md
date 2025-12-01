---
title: Implement Custom Paper Size of Worksheet for Rendering with C++
linktitle: Implement Custom Paper Size of Worksheet for Rendering
type: docs
weight: 70
url: /cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: This article explains how to use the C++ API to set custom paper size of your desired worksheets when rendering Excel file to PDF file format programmatically.
keywords: set custom paper size while rendering excel to pdf c++
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

There is no direct option available to create custom paper sizes in MS Excel; however, you can set a custom paper size of your desired worksheets when rendering Excel files to PDF file format. This document explains how to set a custom paper size of a worksheet using Aspose.Cells APIs.

## **Implement Custom Paper Size of Worksheet for Rendering**

Aspose.Cells allows you to implement your desired paper size of the worksheet. You may use the [**CustomPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/custompapersize/) method of the [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) class to specify a custom page size. The following sample code illustrates how to specify a custom paper size for the first worksheet in the workbook. Please also see the [output PDF](45056028.pdf) generated with the following code for reference.

## **Screenshot**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Set custom paper size in unit of inches
    ws.GetPageSetup().CustomPaperSize(6, 4);

    // Access cell B4
    Cell b4 = ws.GetCells().Get("B4");

    // Add the message in cell B4
    b4.PutValue(u"Pdf Page Dimensions: 6.00 x 4.00 in");

    // Save the workbook in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    wb.Save(outputDir + u"outputCustomPaperSize.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
