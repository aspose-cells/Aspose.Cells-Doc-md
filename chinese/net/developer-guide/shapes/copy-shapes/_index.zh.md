---
title: 在工作表之间复制形状
linktitle: 复制形状
type: docs
weight: 200
url: /zh/net/copy-shapes-between-worksheets/
---
{{% alert color="primary" %}}

有时，您需要在工作表之间复制工作表上的元素，例如图片、图表和其他绘图对象。 Aspose.Cells 支持此功能。可以最高精度复制图表、图像和其他对象。

本文让您详细了解如何在工作表之间复制形状。

{{% /alert %}}

## **将图片从一个工作表复制到另一个**

要将图片从一个工作表复制到另一个工作表，请使用[**工作表.图片.添加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)方法如下面的示例代码所示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.cs" >}}

## **将图表从一个工作表复制到另一个**

下面的代码演示了使用[**工作表.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy)将图表从一个工作表复制到另一个工作表的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.cs" >}}

## **将控件和其他绘图对象从一个工作表复制到另一个工作表**

要复制控件和其他绘图对象，请使用[**工作表.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy)方法如下例所示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.cs" >}}
