---
title: 在工作表之间复制形状
linktitle: 复制形状
type: docs
weight: 200
url: /zh/net/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

有时，您需要在工作表上复制元素，例如图片、图表和其他绘图对象，在工作表之间进行复制操作。Aspose.Cells支持此功能。图表、图像和其他对象可以以最高的精度进行复制。

本文详细介绍了如何在工作表之间复制形状。

{{% /alert %}}

## **从一个工作表复制图片到另一个工作表**

要将图片从一个工作表复制到另一个工作表，请使用[**Worksheet.Pictures.Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)方法，如下面示例代码所示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.cs" >}}

## **将图表从一个工作表复制到另一个工作表**

以下代码演示了使用[**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy)方法将一个工作表的图表复制到另一个工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.cs" >}}

## **从一个工作表复制控件和其他绘图对象到另一个工作表**

要复制控件和其他绘图对象，请使用如下示例所示的[**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.cs" >}}
