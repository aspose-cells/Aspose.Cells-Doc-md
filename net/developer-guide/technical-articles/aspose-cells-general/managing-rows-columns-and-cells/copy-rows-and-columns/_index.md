---
title: Copy Rows and Columns
type: docs
weight: 100
url: /net/copy-rows-and-columns/
---

{{% alert color="primary" %}}

Aspose.Cells APIs provide the facility to copy rows and columns within or between the workbooks. While copying row or column, all the data is copied along with the styling, formulas (with updated references) and resulting values, comments, cell styles, hidden cells, images and drawing objects.

{{% /alert %}}

## **Copying Rows**

### **Copying Single Row**

The following example shows how to copy a single row in a worksheet. The example uses a Microsoft Excel spreadsheet as input and copies the first row to the next 10 rows in the same worksheet.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-CopyRowsColumns-CopyingSingleRow-CopyingSingleRow.cs" >}}

### **Copying Multiple Rows**

You can also copy multiple rows onto a new destination while using the [**Cells.CopyRows**](https://apireference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) method which takes an additional parameter of type integer to specify the number of source rows to be copied.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}

## **Copying Columns**

### **Copying Single Column**

The following example shows how to copy a column in a worksheet. This example uses an existing spreadsheet as input to the process and copies the first column to the next 10 columns using two different approaches.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-CopyRowsColumns-CopyingSingleColumn-1.cs" >}}

### **Copying Multiple Columns**

Similar to [**Cells.CopyRows**](https://apireference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) method, the Aspose.Cells APIs also provide the [**Cells.CopyColumns**](https://apireference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index) method in order to copy multiple source columns to a new location.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}

## Related Articles

- [Adjusting Row Height and Column Width](/cells/net/adjusting-row-height-and-column-width/)
- [AutoFit Rows and Columns](/cells/net/autofit-rows-and-columns/)
- [Inserting and Deleting Rows and Columns](/cells/net/inserting-and-deleting-rows-and-columns/)
- [Hiding and Showing Rows and Columns](/cells/net/hiding-and-showing-rows-and-columns/)
