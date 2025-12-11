---
title: Rendering Slicer with C++
type: docs
weight: 40
url: /cpp/rendering-slicer/
description: Render slicers in Excel files using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Aspose.Cells supports the rendering of slicer shapes. If you convert your worksheet into an image or you save your workbook to PDF or HTML formats, you will see that slicers are rendered properly.

## **Rendering Slicer**
The following sample code loads the [sample Excel file](67338479.xlsx) that contains an existing slicer. It converts the worksheet into an image by setting the print area that covers only the slicer. The following image is the [output image](67338480.png) that shows the rendered slicer. As you can see, the slicer has been rendered properly and it looks the same as in the sample Excel file.

![todo:image_alt_text](rendering-slicer_1)

## **Sample Code**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    
    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleRenderingSlicer.xlsx");

    // Access first worksheet.
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Set the print area because we want to render slicer only.
    ws.GetPageSetup().SetPrintArea(u"B15:E25");

    // Specify image or print options, set one page per sheet and only area to true.
    ImageOrPrintOptions imgOpts;
    imgOpts.SetHorizontalResolution(200);
    imgOpts.SetVerticalResolution(200);
    imgOpts.SetImageType(ImageType::Png);
    imgOpts.SetOnePagePerSheet(true);
    imgOpts.SetOnlyArea(true);

    // Create sheet render object and render worksheet to image.
    SheetRender sr(ws, imgOpts);
    sr.ToImage(0, u"outputRenderingSlicer.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
