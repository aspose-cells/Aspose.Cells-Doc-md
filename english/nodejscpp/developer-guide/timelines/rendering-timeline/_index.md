---
title: Rendering Timeline
type: docs
weight: 40
url: /nodejs-cpp/rendering-timeline/
description: Manage timelines of Excel files with Aspose.Cells for Node.js via C++.
keywords: Rendering timeline without office 2013, office 2016, office 2019 and office 365
---

## **Possible Usage Scenarios**
Aspose.Cells for Node.js via C++ supports the rendering of timeline shape without using office 2013, office 2016, office 2019 and office 365. If you convert your worksheet into an image or you save your workbook to PDF or HTML formats, you will see, timelines are rendered properly.

## **Rendering Timeline**
The following sample code loads the [sample Excel file](input.xlsx) that contains an existing timeline. Get the shape object according to the name of timeline, and then render it into a picture through the Shape.ToImage() method. The flowing image is the [output image](out.png) that shows the rendered timeline. As you can see, timeline has been rendered properly and it looks the same as in the sample Excel file.

![todo:image_alt_text](out.png)
### **Sample Code**
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-RenderingTimeline.js" >}}
