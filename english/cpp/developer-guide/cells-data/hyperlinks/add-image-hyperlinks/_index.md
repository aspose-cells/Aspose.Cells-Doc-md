---
title: Add Image Hyperlinks with C++
linktitle: Add Image Hyperlinks
type: docs
weight: 140
url: /cpp/add-image-hyperlinks/
description: Learn how to Add Image Hyperlinks through the Aspose.Cells for C++ API.
keywords: Add Image Hyperlinks, Insert Image Hyperlinks
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Hyperlinks are useful for accessing information on other worksheets, or on websites. Microsoft Excel lets users add hyperlinks on text in cells, and on images. Image hyperlinks can make navigating a worksheet easier, for example, as next and previous buttons, or logos that link to particular sites. This document explains how to insert image hyperlinks in a worksheet using Aspose.Cells.

{{% /alert %}} 

Aspose.Cells allows you to add hyperlinks to images in spreadsheets at runtime. It is possible to set and modify the link's screen tip and address. The following sample code illustrates how to add an image hyperlink into a worksheet.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a string value to a cell
    worksheet.GetCells().Get(u"C2").PutValue(u"Image Hyperlink");

    // Set the 4th row height
    worksheet.GetCells().SetRowHeight(3, 100);

    // Set the C column width
    worksheet.GetCells().SetColumnWidth(2, 21);

    // Add a picture to the C4 cell
    int index = worksheet.GetPictures().Add(3, 2, 4, 3, srcDir + u"aspose-logo.jpg");

    // Get the picture object
    Picture pic = worksheet.GetPictures().Get(index);

    // Set the placement type
    pic.SetPlacement(PlacementType::FreeFloating);

    // Add an image hyperlink
    Hyperlink hlink = pic.AddHyperlink(u"http://www.aspose.com/");

    // Specify the screen tip
    hlink.SetScreenTip(u"Click to go to Aspose site");

    // Save the Excel file
    workbook.Save(outDir + u"ImageHyperlink_out.xls");

    std::cout << "Image hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
