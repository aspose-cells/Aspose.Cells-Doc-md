---
title: Delete Pivot Table from a Worksheet with Golang via C++
linktitle: Delete Pivot Table
type: docs
weight: 60
url: /go-cpp/delete-pivot-table-from-a-worksheet/
description: C++ code to remove PivotTable for Excel Worksheets using Aspose.Cells.
keywords: c++ remove pivot table from worksheet, c++ remove pivot table from excel, how to delete pivot table with c++, delete pivot table with c++, delete pivot table from excel with c++, c++ delete pivot table, c++ remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---

{{% alert color="primary" %}}

Aspose.Cells provides a feature to delete or remove Pivot Table from a Worksheet. You can delete the pivot table using pivot table object or pivot table position. Please use the [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/) method to delete the pivot table using pivot table object and [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) method to delete pivot table object using its position inside the pivot table collection.

{{% /alert %}}

The following sample code deletes two pivot tables from the worksheet. First it removes pivot table using [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/) method and then it removes pivot table using [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) method.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeletePivotTableFromAWorksheet.go" >}}