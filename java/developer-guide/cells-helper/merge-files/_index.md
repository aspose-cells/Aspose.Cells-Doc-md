---
title: Merge Files
type: docs
weight: 10
url: /java/merge-files/
---

## **Introduction**

Aspose.Cells provides different ways for merging files. For simple files with data, formatting, and formulas, the [**Workbook.combine()**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook)) method can be used to combine several workbooks, and the [**Worksheet.copy(**)](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)) method can be used to copy worksheets into a new workbook. These methods are easy to use and effective, but if you have a lot of files to merge, you might find that they take a lot of system resources. To avoid this, use the CellsHelper.mergeFiles static method, a more efficient way to merge several files.

## **Merge Files Using Aspose.Cells**

The following sample code illustrates how to merge large files using the CellsHelper.mergeFiles method. It takes two simple but large files, MyBook1.xls and MyBook2.xls. The files contain formatted data and formulas only.

{{% alert color="primary" %}}

The CellsHelper.mergeFiles method only supports merging data, styles, formatting, and formulas. Objects like charts, pictures, comments or other objects might not be merged using this method. Moreover, a cached file is used to store temporary data for the process.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
