---
title: 设置图表数据标签的形状类型
description: 了解如何使用 Aspose.Cells for .NET 设置图表中数据标签的形状类型。我们的指南将解释可用的不同形状类型，并向您展示如何为数据标签选择适当的形状，以增强图表的呈现和可用性。
keywords: Aspose.Cells for .NET, charting, data labels, shape types, presentation, usability.
type: docs
weight: 110
url: /zh/net/set-the-shape-type-of-data-labels-of-chart/
---
##  **可能的使用场景**
您可以使用 DataLabels.ShapeType 属性更改图表数据标签的形状类型。它采用 DataLabelShapeType 枚举的值并相应地更改数据标签的形状类型。它的一些值是

{{< highlight "java" >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
##  **设置图表数据标签的形状类型**
以下示例代码将图表数据标签的形状类型更改为 DataLabelShapeType.WedgeEllipseCallout。请参阅[Excel 文件示例](60489778.xlsx)在此代码中使用的[输出Excel文件](60489779.xlsx)由它产生的。屏幕截图显示了代码对示例 Excel 文件的效果。

![待办事项：图像_替代_文本](set-the-shape-type-of-data-labels-of-chart_1.png)
##  **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
