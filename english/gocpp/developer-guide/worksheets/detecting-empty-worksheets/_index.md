---
title: Detecting Empty Worksheets with Golang via C++
linktitle: Detecting Empty Worksheets
type: docs
weight: 410
url: /go-cpp/detecting-empty-worksheets/
description: This article shows you code explaining how to detect empty worksheets of Excel workbooks programmatically using Go API with Aspose.Cells library.
keywords: detect empty worksheet c++, find empty excel worksheet c++
---

## **Check for Populated Cells**

Worksheets can have one or more cells populated with values where a value can be simple (text, numeric, date/time) or a formula or a formula‑based value. In such a case, it is easy to detect if a given worksheet is empty or not. All we have to check is the [**Cells.MaxDataRow**](https://reference.aspose.com/cells/go-cpp/cells/getmaxdatarow/) or [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/go-cpp/cells/getmaxdatacolumn/) properties. If the aforementioned properties return zero or positive values, that means one or more cells have been populated. However, if any of these properties return -1, that indicates that none of the cells have been populated in the given worksheet.

{{% alert color="primary" %}}

The rows and columns collections have a zero‑based index; therefore, a cell at row 0 and column 0 is the first cell in the worksheet, which is A1.

{{% /alert %}}

## **Check for Empty Initialized Cells**

All cells which have values are automatically initialized. However, there is a possibility that a worksheet has cells with only formatting applied. In such a scenario, the [**Cells.MaxDataRow**](https://reference.aspose.com/cells/go-cpp/cells/getmaxdatarow/) or [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/go-cpp/cells/getmaxdatacolumn/) properties will return -1, indicating the absence of any populated values. But initialized cells that exist only because of cell formatting cannot be detected using this approach. In order to check if a worksheet has initialized cells, it is advised to use the `MoveNext` method on the enumerator acquired from the [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/) collection. If the `MoveNext` method returns **true**, that means there are one or more initialized cells in the given worksheet.

## **Check for Shapes**

It is possible that a given worksheet does not have any populated cells; however, it could contain shapes and objects such as controls, charts, images, and so on. If we need to check if a worksheet contains any shape, we can do it by inspecting the [**ShapeCollection.Count**](https://reference.aspose.com/cells/go-cpp/shapecollection/getcount/) property. Any positive value indicates the presence of shape(s) in the worksheet.

## **Programming Sample**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectingEmptyWorksheets.go" >}}
{{< app/cells/assistant language="go" >}}
