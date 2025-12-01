---
title: Insert or Delete Rows in an Excel Worksheet
type: docs
weight: 20
url: /net/insert-or-delete-rows-in-an-excel-worksheet/
description: This article provides the C# code to insert and delete rows in Excel worksheet
keywords: c# insert or delete rows in excel worksheet, c# insert or delete rows in excel, c# insert rows in excel, c# delete rows in excel, insert or delete rows in excel worksheet with c#, insert or delete rows in excel with c#, insert rows in excel with c#, delete rows in excel with c#
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

When creating a new worksheet, or working with an existing worksheet, you might need to add extra rows or columns to accommodate data. At other times, you might need to delete rows or columns from specified positions in the worksheet.

{{% /alert %}}

Aspose.Cells offers two methods for inserting and deleting rows: [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) and [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). These methods are optimized for performance and do the job very quickly.

To insert or remove a number of rows, we recommend that you always use the [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) and [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) methods instead of using the [**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) or [**DeleteRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow) methods in a loop.

Aspose.Cells works in the same way as Microsoft Excel does. When rows or columns are added, the worksheet content is shifted down and to the right. When rows or columns are removed, the worksheet content is shifted up or to the left. Any references in other worksheets and cells are updated when rows are added or removed.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
