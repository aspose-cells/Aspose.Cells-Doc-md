---
title: Copy Shapes between Worksheets
linktitle: Copy Shapes
type: docs
weight: 200
url: /python-net/copy-shapes-between-worksheets/
description: This article shows how to Copy Shapes between Worksheets through the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Copy Shapes between Worksheets, Python how to Copy a Picture from one Worksheet to Another, Python how to Copy a Chart from one Worksheet to Another, Python how to Copy Controls and Other Drawing Objects from One Worksheet to Another.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to copy elements on a worksheet, for example, pictures, charts and other drawing objects, between worksheets. Aspose.Cells for Python via .NET supports this feature. Charts, images, and other objects can be copied with the highest degree of precision.

This article gives you a detailed understanding of how to copy shapes between worksheets.

{{% /alert %}}

## **Copying a Picture from one Worksheet to Another**

To copy a picture from one worksheet to another, use the [**Worksheet.pictures.add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add/#int-int-io.RawIOBase-int-int) method as shown in the sample code below.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.py" >}}

## **Copy a Chart from one Worksheet to Another**

The following code demonstrates the use of [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) method to copy a chart from one worksheet to another.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.py" >}}

## **Copy Controls and Other Drawing Objects from One Worksheet to Another**

To copy controls and other drawing objects, use the [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) method as shown in the example below.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.py" >}}
{{< app/cells/assistant language="python-net" >}}
