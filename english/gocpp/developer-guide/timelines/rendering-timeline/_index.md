---
title: Rendering Timeline with Golang via C++
type: docs
weight: 40
url: /go-cpp/rendering-timeline/
description: Manage timelines of Excel files with Aspose.Cells with Golang via C++.
keywords: Rendering timeline without Office 2013, Office 2016, Office 2019 and Office 365
---

## **Possible Usage Scenarios**
Aspose.Cells supports the rendering of timeline shapes without requiring Office 2013, Office 2016, Office 2019, or Office 365. If you convert your worksheet into an image or save your workbook to PDF or HTML formats, you will see that timelines are rendered properly.

## **Rendering Timeline**
The following sample code loads the [sample Excel file](input.xlsx) that contains an existing timeline. Get the shape object according to the name of the timeline, and then render it into a picture using the `Shape::ToImage()` method. The following image is the [output image](out.png) that shows the rendered timeline. As you can see, the timeline has been rendered properly and looks the same as in the sample Excel file.

![todo:image_alt_text](out.png)
### **Sample Code**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderingTimeline.go" >}}
{{< app/cells/assistant language="go" >}}
