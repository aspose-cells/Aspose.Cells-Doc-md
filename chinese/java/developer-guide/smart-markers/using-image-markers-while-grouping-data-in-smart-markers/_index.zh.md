---
title: 在智能标记中分组数据时使用图像标记
type: docs
weight: 630
url: /zh/java/using-image-markers-while-grouping-data-in-smart-markers/
---
{{% alert color="primary" %}} 

本文提供了一个示例，说明在智能标记中对数据进行分组时图像标记的用法。

{{% /alert %}} 
## **在智能标记中分组数据时使用图像标记**
下面的示例代码创建一个工作簿，然后分别在单元格 D2、E2 和 F2 中添加以下智能标记标签。

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

然后它用数据填充数据源并调用[WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\) ) 方法来处理智能标记标签。代码使用这些图像即[月亮.png](5472549.png)和[月亮2.png](5472548.png)但你可以使用任何图像。以下屏幕截图显示了此示例代码的输出。如您所见，E 列和 F 列中的数据根据 D 列中的数据分组。

![待办事项：图像_替代_文本](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
