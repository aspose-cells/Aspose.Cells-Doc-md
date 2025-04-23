---
title: 在智能标记中分组数据时使用Image Markers
type: docs
weight: 630
url: /zh/java/using-image-markers-while-grouping-data-in-smart-markers/
---

{{% alert color="primary" %}} 

本篇文章展示了在智能标记中分组数据时使用Image Markers的示例。

{{% /alert %}} 
## **在智能标记中分组数据时使用Image Markers**
以下是一个示例代码，它创建了一个工作簿，然后在分别的单元格D2、E2和F2中添加了以下智能标记标签。

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

然后，它用数据源填充数据，并调用 [WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process--) 方法处理智能标记标签。代码中使用了这些图片，例如 [moon.png](5472549.png) 和 [moon2.png](5472548.png)，你也可以使用任何图片。下面的截图显示了此示例代码的输出，可以看到，E 列和 F 列的数据是按照 D 列的数据分组的。

![todo:image_alt_text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
{{< app/cells/assistant language="java" >}}
