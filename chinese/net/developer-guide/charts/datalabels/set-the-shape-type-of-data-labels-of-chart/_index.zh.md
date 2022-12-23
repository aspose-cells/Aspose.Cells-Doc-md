---
title: 设置图表数据标签的形状类型
type: docs
weight: 110
url: /zh/net/set-the-shape-type-of-data-labels-of-chart/
---
## **可能的使用场景**
您可以使用 DataLabels.ShapeType 属性更改图表数据标签的形状类型。它采用 DataLabelShapeType 枚举的值并相应地更改数据标签的形状类型。它的一些值是

{{< highlight "java" >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **设置图表数据标签的形状类型**
以下示例代码将图表数据标签的形状类型更改为 DataLabelShapeType.WedgeEllipseCallout。请参阅[示例 Excel 文件](60489778.xlsx)用于此代码和[输出Excel文件](60489779.xlsx)由它产生。屏幕截图显示了代码对示例 Excel 文件的影响。

![待办事项：图片_替代_文本](set-the-shape-type-of-data-labels-of-chart_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
