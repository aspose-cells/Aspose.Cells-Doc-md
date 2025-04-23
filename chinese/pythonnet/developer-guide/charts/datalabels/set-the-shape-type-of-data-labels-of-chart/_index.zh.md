---
title: 设置图表数据标签的形状类型
description: 学习如何使用Aspose.Cells for Python via .NET设置图表中数据标签的形状类型。我们的指南将介绍不同的形状类型，并指导您选择合适的形状以增强图表的表现和实用性。
keywords: Aspose.Cells for Python via .NET，制图，数据标签，形状类型，演示，实用性。
type: docs
weight: 110
url: /zh/python-net/set-the-shape-type-of-data-labels-of-chart/
---

## **可能的使用场景**
您可以使用DataLabels.ShapeType属性更改图表的数据标签的形状类型。它采用DataLabelShapeType枚举的值，并相应地更改数据标签的形状类型。其中一些取值为

{{< highlight java >}}

DataLabelShapeType.BENT_LINE_CALLOUT

DataLabelShapeType.DOWN_ARROW_CALLOUT

DataLabelShapeType.ELLIPSE

DataLabelShapeType.LINE_CALLOUT

DataLabelShapeType.RECT

etc.

{{< /highlight >}}

## **设置图表数据标签的形状类型**
以下示例代码将图表的数据标签形状类型更改为DataLabelShapeType.WedgeEllipseCallout。请参阅此代码中使用的[示例Excel文件](60489778.xlsx)和由其生成的[输出Excel文件](60489779.xlsx)。截图显示了代码对示例Excel文件的效果。 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **示例代码**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SetShapeTypeOfDataLabelsOfChart.py" >}}
