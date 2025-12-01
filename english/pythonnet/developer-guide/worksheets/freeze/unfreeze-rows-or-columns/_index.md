---
title: Unfreeze Rows or Columns
linktitle: Unfreeze panes
type: docs
weight: 190
url: /python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: In this article, you will learn how to unfreeze rows ,columns or panes of Excel Worksheets programmatically using Aspose.Cells for Python via .NET APIs.
keywords: Python Excel Library, Python Unfreeze panes, Python How to Unfreeze rows, Python how to Unfreeze columns, Python how to unFreeze window.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

In this article, we will learn How to UnFreeze Rows, Columns and Panes. If worksheets in the Excel files are frozen, sometimes we want to unfreeze worksheet or adjust frozen rows, columns or panes.


## **How to Unfreeze Rows or Columns In Excel**

1. Click View tab > Freeze Panes > Unfreeze Panes.

**![unfreeze panes in Excel](Unfreeze-Panes.png)**




## **How to UnFreeze Rows, Columns or Panes with Aspose.Cells for Python Excel Library**
It's simple to unfreeze panes with Aspose.Cells for Python via .NET. Please use the [**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/) method to unfeeze panes .

1. Construct Workbook to open the frozen file.
2. Unfreeze panes with Worksheet.UnFreezePanes() method.
3. Save the file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

Attached [sample source Excel file](Frozen.xlsx).
{{< app/cells/assistant language="python-net" >}}
