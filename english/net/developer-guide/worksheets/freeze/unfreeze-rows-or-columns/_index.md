---
title: Unfreeze Rows or Columns
linktitle: Unfreeze panes
type: docs
weight: 190
url: /net/unfreeze-rows-or-columns-of-excel-worksheet
description: In this article, you will learn how to unfreeze rows, columns, or panes of Excel worksheets programmatically using the C# library with the .NET API.
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, Unfreeze window.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

In this article, we will learn how to unfreeze rows, columns, and panes. If worksheets in the Excel files are frozen, sometimes we want to unfreeze a worksheet or adjust frozen rows, columns, or panes.

## **In Excel**

1. Click **View** tab > **Freeze Panes** > **Unfreeze Panes**.

**![unfreeze panes in Excel](Unfreeze-Panes.png)**

## **Unfreeze Rows, Columns, or Panes with Aspose.Cells for .NET**

It’s simple to unfreeze panes with Aspose.Cells for .NET. Please use the [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes) method to unfreeze panes.

1. Construct a Workbook to open the frozen file.  
2. Unfreeze panes with the `Worksheet.UnFreezePanes()` method.  
3. Save the file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

Attached [sample source Excel file](Frozen.xlsx).
{{< app/cells/assistant language="csharp" >}}
