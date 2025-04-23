---
title: 设置图表数据标签的形状类型
description: 使用 Aspose.Cells for .NET 学习如何设置图表中数据标签的形状类型。我们的指南将解释可用的不同形状类型，并演示如何选择适当的形状以增强图表的表现和可用性。
keywords: Aspose.Cells for .NET, 制图, 数据标签, 形状类型, 表现, 可用性。
type: docs
weight: 110
url: /zh/net/set-the-shape-type-of-data-labels-of-chart/
---

## **可能的使用场景**
您可以使用DataLabels.ShapeType属性更改图表的数据标签的形状类型。它采用DataLabelShapeType枚举的值，并相应地更改数据标签的形状类型。其中一些取值为

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **设置图表数据标签的形状类型**
以下示例代码将图表的数据标签形状类型更改为DataLabelShapeType.WedgeEllipseCallout。请参阅此代码中使用的[示例Excel文件](60489778.xlsx)和由其生成的[输出Excel文件](60489779.xlsx)。截图显示了代码对示例Excel文件的效果。 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
