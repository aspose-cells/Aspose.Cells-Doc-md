---
title: 如何在智能标记中使用图片标记
type: docs
weight: 30
url: /zh/net/how-to-use-image-markers-in-smart-markers/
alias: [/net/using-image-markers-while-grouping-data-in-smart-markers/]
---

## **可能的使用场景**
图片标记是模板系统（如FoxPro、Handlebars或现代UI框架）中的特殊占位符，用于动态插入图片或视觉资产到模板中。有时，您需要使用智能标记插入图片。Aspose.Cells 使其成为可能，将图片添加到智能标记中。

## **智能标记中的图片参数**
管理图像的智能标记参数。

- **Picture:FitToCell** - 自动将图像适合到单元格的行高和列宽。
- **Picture:ScaleN** - 将高度和宽度按N百分比缩放。
- **Picture:Width:Nin和Height:Nin** - 将图像渲染为 N 英寸高和 N 英寸宽。您还可以指定左偏移量和顶部偏移量（以点为单位）。

## **如何在智能标记中使用图片标记**
请参阅以下示例代码，演示如何使用智能标记插入图片。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}

## **在分组数据时使用图片标记的方法**
以下示例创建一个工作簿，然后在单元格D2、E2和F2中分别添加以下智能标记标签。

{{< highlight java >}}

&=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

然后填充数据源数据，并调用[WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) 方法处理智能标记标签。代码使用了这些图片即[moon.png](5115492.png)和[moon2.png](5115491.png)，但您可以使用任何图片。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}

{{< app/cells/assistant language="csharp" >}}
