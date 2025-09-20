---
title: Merge Files with Golang via C++
linktitle: Merge Files
type: docs
weight: 20
url: /go-cpp/merge-files/
description: Learn how to merge Excel files efficiently using Aspose.Cells for C++.
---

## **Introduction**

Aspose.Cells provides different ways for merging files. For simple files with data, formatting, and formulas, the [**Workbook.Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) method can be used to combine several workbooks, and the [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) method can be used to copy worksheets into a new workbook. These methods are easy to use and effective, but if you have a lot of files to merge, you might find that they take a lot of system resources. To avoid this, use the [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) static method, a more efficient way to merge several files.

## **Merge Files Using Aspose.Cells**

The following sample code illustrates how to merge large files using the [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/) method. It takes two simple but large files, Book1.xls and Book2.xls. The files contain formatted data and formulas only.

{{% alert color="primary" %}}

The [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/) method only supports merging data, styles, formatting, and formulas. Objects like charts, pictures, comments, or other objects might not be merged using this method. Moreover, a cached file is used to store temporary data for the process.

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeFiles.go" >}}