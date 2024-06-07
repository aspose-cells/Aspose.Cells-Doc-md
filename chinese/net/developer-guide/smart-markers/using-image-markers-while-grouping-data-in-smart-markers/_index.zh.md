---
title: 在智能标记中使用Image Markers分组数据
type: docs
weight: 30
url: /zh/net/using-image-markers-while-grouping-data-in-smart-markers/
---

## **在智能标记中分组数据时使用图片标记**
以下示例创建一个工作簿，然后分别在单元格D2、E2和F2中添加以下智能标记标签。

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

然后填充数据源数据并调用[WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)方法处理智能标记标签。该代码使用这些图片，即[moon.png](5115492.png)和[moon2.png](5115491.png)，但您可以使用任何图片。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
