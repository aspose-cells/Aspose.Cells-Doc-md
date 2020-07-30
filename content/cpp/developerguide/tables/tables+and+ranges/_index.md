---
title : "Tables and Ranges" 
description : "" 
weight : 12051 
toc : false
type: docs
url: /cpp/developerguide/tables/tables+and+ranges/
---

# Aspose.Cells for C++ : Tables and Ranges


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#introduction)
*   2 [Using Microsoft Excel](#using-microsoft-excel)
*   3 [Using Aspose.Cells](#using-aspose.cells)
{{< /panel >}}
 

## Introduction

Sometimes you create a table in Microsoft Excel and do not want to keep working with the table functionality that it comes with. Instead, you want something that looks like a table. To keep data in a table without losing formatting, convert the table to a regular range of data. Aspose.Cells does support this feature of Microsoft Excel for tables and list-objects.

## Using Microsoft Excel

Use the **Convert to Range** feature to quickly convert a table to a range without losing formatting. In Microsoft Excel 2007/2010:

1.  Click anywhere in the table to make sure that the active cell is in a table column.
2.  On the **Design** tab, in the **Tools** group, click **Convert to Range**.

The table features are no longer available after the table has been converted to a range. For example, row headers no longer include the sort and filter arrows, and structured references (references that use table names) that were used in formulas turn into regular cell references.

## Using Aspose.Cells

The following code snippet demonstrates the same functionality using Aspose.Cells.

