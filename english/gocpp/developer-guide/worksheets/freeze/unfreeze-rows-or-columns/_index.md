---
title: Unfreeze Rows or Columns of an Excel Worksheet with Go
linktitle: Unfreeze panes
type: docs
weight: 190
url: /gocpp/unfreeze-rows-or-columns-of-excel-worksheet
description: In this article, you will learn how to unfreeze rows, columns, or panes of Excel worksheets programmatically using the Aspose.Cells for Go API.
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, Unfreeze window.
ai_search_scope: cells_go
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

In this article, we will learn how to unfreeze rows, columns, and panes in Excel worksheets. If worksheets in Excel files are frozen, sometimes we want to unfreeze the worksheet or adjust frozen rows, columns, or panes.

## **In Excel**

1. Click the **View** tab > **Freeze Panes** > **Unfreeze Panes**.

**![unfreeze panes in Excel](Unfreeze-Panes.png)**

## **Unfreeze Rows, Columns, or Panes with Aspose.Cells for Go**
It's simple to unfreeze panes with Aspose.Cells for Go. Use the [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/gocpp/aspose.cells/worksheet/unfreezepanes/) method to unfreeze panes.

1. Construct a `Workbook` object to open the frozen file.  
2. Unfreeze panes using the `Worksheet.UnFreezePanes()` method.  
3. Save the file.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UnfreezeRowsOrColumnsOfExcelWorksheet.go" >}}

Attached [sample source Excel file](Frozen.xlsx).

{{< app/cells/assistant language="go" >}}