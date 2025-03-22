---
title: Rendering Timeline with C++
type: docs
weight: 40
url: /cpp/rendering-timeline/
description: Manage timelines of Excel files with Aspose.Cells with C++.
keywords: Rendering timeline without office 2013, office 2016, office 2019 and office 365
---

## **Possible Usage Scenarios**
Aspose.Cells supports the rendering of timeline shape without using office 2013, office 2016, office 2019 and office 365. If you convert your worksheet into an image or you save your workbook to PDF or HTML formats, you will see, timelines are rendered properly.

## **Rendering Timeline**
The following sample code loads the [sample Excel file](input.xlsx) that contains an existing timeline. Get the shape object according to the name of timeline, and then render it into a picture through the Shape.ToImage() method. The flowing image is the [output image](out.png) that shows the rendered timeline. As you can see, timeline has been rendered properly and it looks the same as in the sample Excel file.

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
