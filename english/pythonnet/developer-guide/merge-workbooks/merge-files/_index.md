---
title: Merge Files
type: docs
weight: 20
url: /python-net/merge-files/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

Aspose.Cells for Python via .NET provides different ways for merging files. For simple files with data, formatting, and formulas, the [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) method can be used to combine several workbooks, and the [**Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy) method can be used to copy worksheets into a new workbook. These methods are easy to use and effective, but if you have a lot of files to merge, you might find that they **consume** a lot of system resources. To avoid this, use the [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files) static method, a more efficient way to merge several files.

## **Merge Files Using Aspose.Cells for Python via .NET**

The following sample code illustrates how to merge large files using the [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files) method. It takes two simple but large files, Book1.xls and Book2.xls. The files contain formatted data and formulas only.

{{% alert color="primary" %}}

The [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files) method only supports merging data, styles, formatting, and formulas. Objects like charts, pictures, comments**,** or other objects might not be merged using this method. Moreover, a cached file is used to store temporary data for the process.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CellsHelperClass-MergeFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
