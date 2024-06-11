---
title: 在工作表之间复制形状
linktitle: 复制形状
type: docs
weight: 200
url: /zh/net/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

有时，您需要在工作表之间复制元素，例如图片、图表和其他绘图对象。Aspose.Cells支持此功能。可以以最高精度复制图表、图片和其他对象。

本文详细介绍了如何在工作表之间复制形状。

{{% /alert %}}

## **从一个工作表复制图片到另一个工作表**

要将图片从一个工作表复制到另一个，请使用以下示例代码中显示的 [**Worksheet.Pictures.Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) 方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.cs" >}}

## **将图表从一个工作表复制到另一个**

以下代码演示了使用 [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) 方法将图表从一个工作表复制到另一个。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.cs" >}}

## **从一个工作表复制控件和其他绘图对象到另一个**

要复制控件和其他绘图对象，请使用以下示例中显示的 [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) 方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.cs" >}}
