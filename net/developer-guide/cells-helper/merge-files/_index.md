---
title: Merge Files
type: docs
weight: 20
url: /net/merge-files/
---

## **Introduction**
Aspose.Cells provides different ways for merging files. For simple files with data, formatting, and formulas, the [Workbook.Combine()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/combine) method can be used to combine several workbooks, and the [Worksheet.Copy()](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/methods/copy/index) method can be used to copy worksheets into a new workbook. These methods are easy to use and effective, but if you have a lot of files to merge, you might find that they take a lot of system resources. To avoid this, use the [CellsHelper.MergeFiles](https://apireference.aspose.com/net/cells/aspose.cells/cellshelper/methods/mergefiles) static method, a more efficient way to merge several files.
## **Merge Files Using Aspose.Cells**
The following sample code illustrates how to merge large files using the [CellsHelper.MergeFiles](https://apireference.aspose.com/net/cells/aspose.cells/cellshelper/methods/mergefiles) method. It takes two simple but large files, Book1.xls and Book2.xls. The files contain formatted data and formulas only.

{{% alert color="primary" %}} 

The [CellsHelper.MergeFiles](https://apireference.aspose.com/net/cells/aspose.cells/cellshelper/methods/mergefiles) method only supports merging data, styles, formatting, and formulas. Objects like charts, pictures, comments or other objects might not be merged using this method. Moreover, a cached file is used to store temporary data for the process.

{{% /alert %}} 

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}