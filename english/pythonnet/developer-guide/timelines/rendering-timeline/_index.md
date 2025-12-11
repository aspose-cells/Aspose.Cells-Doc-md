---
title: Rendering Timeline
type: docs
weight: 40
url: /python-net/rendering-timeline/
description: Manage timelines of Excel files with Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python library, Python rendering timeline without Excel, render timeline to image using Aspose.Cells for Python library.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Aspose.Cells for Python via .NET supports rendering timeline shapes without using Office 2013, Office 2016, Office 2019, or Office 365. If you convert your worksheet into an image or save your workbook to PDF or HTML formats, you will see that timelines are rendered properly.

## **How to Render Timeline Using Aspose.Cells for Python Excel Library**
The following sample code loads the [sample Excel file](input.xlsx) that contains an existing timeline. It gets the shape object according to the name of the timeline and then renders it into a picture through the `Shape.to_image()` method. The following image is the [output image](out.png) that shows the rendered timeline. As you can see, the timeline has been rendered properly and it looks the same as in the sample Excel file.

![todo:image_alt_text](out.png)

### **Sample Code**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-RenderingTimeline.py" >}}

{{< app/cells/assistant language="python-net" >}}
