---
title: Find Maximum Rows and Columns supported by XLS and XLSX formats with Golang via C++
linktitle: Find Maximum Rows and Columns
type: docs
weight: 20
url: /go-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: Learn how to find the maximum rows and columns supported by XLS and XLSX formats using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

There are different numbers of rows and columns supported by Excel formats. For example, XLS supports 65536 rows and 256 columns while XLSX supports 1048576 rows and 16384 columns. If you want to know how many rows and columns are supported by a given format, you can use [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) and [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) properties.

## **Find Maximum Rows and Columns supported by XLS and XLSX formats**

The following sample code creates a workbook first in XLS and then in XLSX format. After creation, it prints the values of [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) and [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) properties. Please see the console output of the code given below for your reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindMaximumRowsAndColumnsSupportedByXlsAndXlsxFormats.go" >}}
## **Console Output**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}