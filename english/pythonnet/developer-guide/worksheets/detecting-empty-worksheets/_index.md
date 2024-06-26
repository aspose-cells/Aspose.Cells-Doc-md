---
title: Detecting Empty Worksheets
type: docs
weight: 410
url: /python-net/detecting-empty-worksheets/
description: This article shows you code explaining how to detect empty worksheets of Excel workbooks programmatically using Aspose.Cells for Python via .NET library.
keywords: Python Excel Library, detect empty worksheet using python, find empty excel worksheet in python.
---

## **Check for Populated Cells**

Worksheets can have one or more cells populated with values where a value can be simple (text, numeric, date/time) or a formula or a formula based value. In such a case, it is easy to detect if a given worksheet is empty or not. All we have to check is the [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) or [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) properties. If the aforementioned properties return zero or positive values that means, one or more cells have been populated, however, if any of these properties return -1 that indicates that none of the cells have been populated in the given worksheet.

{{% alert color="primary" %}}

The rows & columns collections have zero-based index therefore a cell at row 0 & column 0 means the first cell in the worksheet, which is A1.

{{% /alert %}}

## **Check for Empty Initialized Cells**

All cells which have values are automatically initialized, however, there is a possibility that a worksheet has cells with only formatting applied. In such a scenario, the [**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) or [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) properties will return -1 indicating the absence of any populated values but initialized cells due to the cell formatting cannot be detected using this approach. In order to check if a worksheet has empty initialized cells, it is advised to use the IEnumerator.MoveNext method on the enumerator acquired from [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection. If the IEnumerator.MoveNext method returns **true** that means there are one or more initialized cells in the given worksheet.

## **Check for Shapes**

It is possible that a given worksheet does not have any populated cells, however, it could contain shapes & objects such as controls, charts, images and so on. If we need to check if a worksheet contains any shape, we can do it by inspecting the [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) elements. Any positive value indicates the presence of shape(s) in the worksheet.

## **Programming Sample**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-DetectEmptyWorksheets.py" >}}
