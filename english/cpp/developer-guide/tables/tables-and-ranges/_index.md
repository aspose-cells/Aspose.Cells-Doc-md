---
title: Tables and Ranges
type: docs
weight: 30
url: /cpp/tables-and-ranges/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**
Sometimes you create a table in Microsoft Excel and do not want to keep working with the table functionality that it comes with. Instead, you want something that looks like a table. To keep data in a table without losing formatting, convert the table to a regular range of data. Aspose.Cells supports this feature of Microsoft Excel for tables and list objects.

## **Using Microsoft Excel**
Use the **Convert to Range** feature to quickly convert a table to a range without losing formatting. In Microsoft Excel 2007/2010:

1. Click anywhere in the table to make sure that the active cell is in a table column.
2. On the **Design** tab, in the **Tools** group, click **Convert to Range**.

{{% alert color="primary" %}} 

The table features are no longer available after the table has been converted to a range. For example, row headers no longer include the sort and filter arrows, and structured references (references that use table names) that were used in formulas turn into regular cell references.

{{% /alert %}} 

## **Using Aspose.Cells**
The following code snippet demonstrates the same functionality using Aspose.Cells.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
