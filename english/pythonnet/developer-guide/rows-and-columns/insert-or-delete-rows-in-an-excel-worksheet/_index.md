---
title: Insert or Delete Rows in an Excel Worksheet
type: docs
weight: 20
url: /python-net/insert-or-delete-rows-in-an-excel-worksheet/
description: This article provides the python code to insert and delete rows in Excel worksheet with Aspose.Cells for Python via .NET library.
keywords: Python Excel Library, Python insert or delete rows in excel worksheet, Python insert or delete rows in excel, Python insert rows in excel, Python delete rows in excel, insert or delete rows in excel worksheet with Python, insert or delete rows in excel with Python, insert rows in excel with Python, delete rows in excel with Python
---

{{% alert color="primary" %}}

When creating a new worksheet, or working with an existing worksheet, you might need to add extra rows or columns to accommodate data. At other times, you might need to delete rows or columns from specified positions in the worksheet.

{{% /alert %}}

Aspose.Cells for Python via .NET offers two methods for inserting and deleting rows: [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) and [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/). These methods are optimized for performance and do the job very quickly.

To insert or remove a number of rows, we recommend that you always use the [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) and [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/) methods instead of using the [**Cells.insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row) or [**delete_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_row) methods in a loop.

Aspose.Cells for Python via .NET works in the same way as Microsoft Excel does. When rows or columns are added, the worksheet content is shifted down and to the right. When rows or columns are removed, the worksheet content is shifted up or to the left. Any references in other worksheets and cells are updated when rows are added or removed.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertDeleteRows-1.py" >}}
{{< app/cells/assistant language="python-net" >}}