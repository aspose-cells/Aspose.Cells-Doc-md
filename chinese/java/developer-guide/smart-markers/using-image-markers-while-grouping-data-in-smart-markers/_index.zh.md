---
title: 在智能标记中使用Image Markers分组数据
type: docs
weight: 630
url: /zh/java/using-image-markers-while-grouping-data-in-smart-markers/
---

{{% alert color="primary" %}} 

本文提供了一个示例，用于说明在智能标记中分组数据时使用图像标记的用法。

{{% /alert %}} 
## **在智能标记中分组数据时使用图片标记**
以下示例代码创建一个工作簿，然后分别在D2、E2和F2单元格添加以下智能标记标记。

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

然后填充数据源数据，并调用[WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\))方法来处理智能标记标签。该代码使用了这些图片，即[moon.png](5472549.png)和[moon2.png](5472548.png)，但您可以使用任何图片。以下屏幕截图显示了此示例代码的输出。如您所见，列E和F中的数据相对于D列中的数据进行了分组。

![todo:image_alt_text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
