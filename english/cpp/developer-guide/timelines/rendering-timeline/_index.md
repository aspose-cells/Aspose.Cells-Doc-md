---
title: Rendering Timeline with C++
type: docs
weight: 40
url: /cpp/rendering-timeline/
description: Manage timelines of Excel files with Aspose.Cells with C++.
keywords: Rendering timeline without Office 2013, Office 2016, Office 2019 and Office 365
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Aspose.Cells supports the rendering of timeline shapes without requiring Office 2013, Office 2016, Office 2019, or Office 365. If you convert your worksheet into an image or save your workbook to PDF or HTML formats, you will see that timelines are rendered properly.

## **Rendering Timeline**
The following sample code loads the [sample Excel file](input.xlsx) that contains an existing timeline. Get the shape object according to the name of the timeline, and then render it into a picture using the `Shape::ToImage()` method. The following image is the [output image](out.png) that shows the rendered timeline. As you can see, the timeline has been rendered properly and looks the same as in the sample Excel file.

![todo:image_alt_text](out.png)
### **Sample Code**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing timeline.
    Workbook workbook(u"input.xlsx");
    
    // Access second worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(1);

    // Access the first Timeline inside the worksheet.
    Timeline timeline = sheet.GetTimelines().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    // Get timeline shape object by timeline's name
    Shape timeLineShape = sheet.GetShapes().Get(timeline.GetName());

    // Save the timeline as an image
    timeLineShape.ToImage(u"out.png", options);

    std::cout << "Timeline image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
