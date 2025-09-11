---
title: Generate Thumbnail of the Worksheet with C++
linktitle: Generate Thumbnail of the Worksheet
type: docs
weight: 110
url: /cpp/generate-thumbnail-of-the-worksheet/
description: Generate worksheet thumbnails as images using Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

It can be useful to generate thumbnails from worksheets. A thumbnail is a small image that can be pasted into a Word document or a PowerPoint presentation to give a preview of what's on the worksheet. It can be added to a webpage with a link to download the original document and has a host of other uses.

{{% /alert %}} 

Aspose.Cells for C++ allows you to output worksheets to image files, making thumbnail generation straightforward. The following sample code demonstrates how to output worksheets to image files using C++.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source workbook
    Workbook book(srcDir + u"sampleGenerateThumbnailOfWorksheet.xlsx");

    // Configure image rendering options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Bmp);
    imgOptions.SetVerticalResolution(200);
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetDesiredSize(600, 600, true); // Set thumbnail dimensions

    // Access first worksheet
    WorksheetCollection worksheets = book.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Render worksheet to image
    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputGenerateThumbnailOfWorksheet.bmp");

    std::cout << "Worksheet thumbnail generated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}