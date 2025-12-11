---
title: Find the Maximum Rows and Columns Supported by XLS and XLSX Formats with Go via C++
linktitle: Find Maximum Rows and Columns
type: docs
weight: 20
url: /go-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: Learn how to find the maximum rows and columns supported by XLS and XLSX formats using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

Excel formats support different numbers of rows and columns. For example, XLS supports 65,536 rows and 256 columns, while XLSX supports 1,048,576 rows and 16,384 columns. If you want to know how many rows and columns are supported by a given format, you can use [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) and [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) properties.

## **Find Maximum Rows and Columns Supported by XLS and XLSX Formats**

The following sample code creates a workbook first in XLS format and then in XLSX format. After creation, it prints the values of the [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) and [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) properties. Please see the console output provided below for your reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindMaximumRowsAndColumnsSupportedByXlsAndXlsxFormats.go" >}}
## **Console Output**

{{< highlight java >}}

Maximum rows and columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum rows and columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}