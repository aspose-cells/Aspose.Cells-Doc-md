---
title: 设置图表的数据标签的形状类型
description: 了解如何使用Aspose.Cells for .NET在图表中设置数据标签的形状类型。 我们的指南将解释可用的不同形状类型，并向您展示如何选择适合数据标签的适当形状，以增强图表的呈现和可用性。
keywords: Aspose.Cells for .NET，图表，数据标签，形状类型，演示，易用性。
type: docs
weight: 110
url: /zh/net/set-the-shape-type-of-data-labels-of-chart/
---

## **可能的使用场景**
您可以使用 DataLabels.ShapeType 属性更改图表的数据标签的形状类型。这需要 DataLabelShapeType 枚举的值，并相应地更改数据标签的形状类型。其一些值为

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **设置图表数据标签的形状类型**
以下示例代码将图表的数据标签的形状类型更改为 DataLabelShapeType.WedgeEllipseCallout。请参阅此代码中使用的 [示例 Excel 文件](60489778.xlsx) 和生成的 [输出 Excel 文件](60489779.xlsx)。屏幕截图显示了代码对示例 Excel 文件的影响。 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
