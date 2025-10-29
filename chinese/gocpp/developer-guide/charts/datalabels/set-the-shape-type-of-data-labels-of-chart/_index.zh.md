---
title: 使用Golang通过C++设置图表的数据标签形状类型
linktitle: 设置图表数据标签的形状类型
description: 学习如何使用Aspose.Cells for C++设置图表中数据标签的形状类型。我们的指南将解释不同的形状类型，并展示如何选择合适的形状以增强图表的展示效果和可用性。
keywords: Aspose.Cells for C++，制表，数据标签，形状类型，展示，易用性。
type: docs
weight: 110
url: /zh/go-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **可能的使用场景**
你可以使用`DataLabels.ShapeType`属性更改图表数据标签的形状类型。它接受`DataLabelShapeType`枚举的值，根据需要更改数据标签的形状。部分值包括：

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}

## **设置图表数据标签的形状类型**
以下示例代码将图表数据标签的形状类型更改为`DataLabelShapeType.WedgeEllipseCallout`。请参阅此代码使用的[示例Excel文件](60489778.xlsx)和由其生成的[输出Excel文件](60489779.xlsx)。截屏展示了代码在示例Excel文件上的效果。 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **示例代码**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetTheShapeTypeOfDataLabelsOfChart.go" >}}
