---
title: Rendering Timeline
type: docs
weight: 40
url: /net/rendering-timeline/
description: Manage timelines of Excel files with Aspose.Cells.
keywords: Rendering timeline without office 2013, office 2016, office 2019 and office 365
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Aspose.Cells supports the rendering of timeline shapes without requiring Office 2013, Office 2016, Office 2019, or Office 365. If you convert your worksheet into an image or you save your workbook to PDF or HTML formats, you will see that timelines are rendered properly.

## **Rendering Timeline**
The following sample code loads the [sample Excel file](input.xlsx) that contains an existing timeline. Get the shape object by the name of the timeline, and then render it into a picture through the `Shape.ToImage()` method. The following image is the [output image](out.png) that shows the rendered timeline. As you can see, the timeline has been rendered properly and it looks the same as in the sample Excel file.

![todo:image_alt_text](out.png)
### **Sample Code**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Timelines-RenderingTimeline.cs" >}}

{{< app/cells/assistant language="csharp" >}}
