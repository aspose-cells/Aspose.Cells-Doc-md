---
title: Resize Rows and Columns
type: docs
weight: 30
url: /net/resize-rows-and-columns/
---

{{% alert color="primary" %}} 

Sometimes cell values are wider that the cell they are in, or are on several lines. Such values are not fully visible to users unless they change the height and width of rows and columns. Aspose.Cells.GridWeb fully supports setting row heights and column width. This topic discusses these features in detail with the help of examples.

{{% /alert %}} 
## **Working with Row Heights and Column Width**
### **Setting Row Height**
To set the height of a row:

1. Add the Aspose.Cells.GridWeb control to your Web Form.
1. Access the worksheet's Cells collection.
1. Set the height of all cells in any specified row.

{{% alert color="primary" %}} 

SetRowHeight and SetColumnWidth method of the Cells collection also has variants available to set row height and column width measurements in inches and pixels.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetRowHeight.cs" >}}
### **Setting Column Width**
To set the width of a column:

1. Add the Aspose.Cells.GridWeb control to your Web Form.
1. Access the worksheet's Cells collection.
1. Set the width of all cells in any specified column.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetColumnWidth.cs" >}}
