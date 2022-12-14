---
title: 在智能标记中分组数据时使用图像标记
type: docs
weight: 30
url: /zh/net/using-image-markers-while-grouping-data-in-smart-markers/
---
## **在智能标记中分组数据时使用图像标记**
下面的示例创建一个工作簿，然后分别在单元格 D2、E2 和 F2 中添加以下智能标记。

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

然后它用数据填充数据源并调用[WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)处理智能标记标签的方法。代码使用这些图像即[月亮.png](5115492.png)和[月亮2.png](5115491.png)但你可以使用任何图像。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
