---
title: Rendering Timeline
type: docs
weight: 40
url: /nodejs-cpp/rendering-timeline/
description: Manage timelines of Excel files with Aspose.Cells for Node.js via C++.
keywords: Rendering timeline without Office 2013, Office 2016, Office 2019, and Office 365
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Aspose.Cells for Node.js via C++ supports the rendering of timeline shapes without requiring Office 2013, Office 2016, Office 2019, or Office 365. If you convert your worksheet into an image or you save your workbook to PDF or HTML formats, you will see that timelines are rendered properly.

## **Rendering Timeline**
The following sample code loads the [sample Excel file](input.xlsx) that contains an existing timeline. Get the shape object by the timeline’s name, and then render it into a picture through the Shape.ToImage() method. The following image is the [output image](out.png) that shows the rendered timeline. As you can see, the timeline has been rendered properly and it looks the same as in the sample Excel file.

![todo:image_alt_text](out.png)
### **Sample Code**
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-RenderingTimeline.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
