---
title: Tables and Ranges
type: docs
weight: 50
url: /python-net/tables-and-ranges/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

Sometimes you create a table in Microsoft Excel and do not want to keep working with the table functionality that it comes with. Instead, you want something that looks like a table. To keep data in a table without losing formatting, convert the table to a regular range of data.
Aspose.Cells for Python via .NET does support this feature of Microsoft Excel for tables and list objects.

## **Using Microsoft Excel**

Use the **Convert to Range** feature to quickly convert a table to a range without losing formatting. In Microsoft Excel 2007/2010:

1. Click anywhere in the table to make sure that the active cell is in a table column.
1. On the **Design** tab, in the **Tools** group, click **Convert to Range**.

## **Using Aspose.Cells for Python via .NET**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRange-1.py" >}}

{{% alert color="primary" %}}

The table features are no longer available after the table has been converted to a range. For example, row headers no longer include the sort and filter arrows, and structured references (references that use table names) that were used in formulas turn into regular cell references.

{{% /alert %}}

## **Convert Table to Range with Options**

Aspose.Cells for Python via .NET provides additional options while converting Table to Range through the [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions) class. The [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions) class provides [**last_row**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions/last_row/) property which allows you to set the last index of the table row. The table formatting will be retained up to the specified row index and the rest of the formatting will be removed.

The sample code given below demonstrates the use of [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions) class.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRangeWithOptions-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
