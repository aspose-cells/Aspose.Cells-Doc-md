---
title: 在工作表之间复制形状
linktitle: 复制形状
type: docs
weight: 200
url: /zh/python-net/copy-shapes-between-worksheets/
description: 本文展示了如何通过Aspose.Cells for Python via .NET API在工作表之间复制形状。
keywords: Python Excel库，Python将形状复制到另一个工作表，Python如何将图片从一个工作表复制到另一个工作表，Python如何将图表从一个工作表复制到另一个工作表，Python如何将控件和其他绘图对象从一个工作表复制到另一个工作表。
---

{{% alert color="primary" %}}

有时，您需要在工作表之间复制元素，例如图片、图表和其他绘图对象。Aspose.Cells for Python via .NET支持此功能。可以精确复制图表、图片和其他对象。

本文详细介绍了如何在工作表之间复制形状。

{{% /alert %}}

## **从一个工作表复制图片到另一个工作表**

要将图片从一个工作表复制到另一个，请使用以下示例代码中显示的 [**Worksheet.pictures.add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add/#int-int-io.RawIOBase-int-int) 方法。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.py" >}}

## **将图表从一个工作表复制到另一个**

以下代码演示了使用 [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) 方法将图表从一个工作表复制到另一个。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.py" >}}

## **从一个工作表复制控件和其他绘图对象到另一个**

要复制控件和其他绘图对象，请使用以下示例中显示的 [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) 方法。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.py" >}}
