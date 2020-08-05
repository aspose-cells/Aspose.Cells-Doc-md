---
title : "Working with Rows and Columns GridWeb" 
description : "" 
weight : 16330 
toc : false
type: docs
url: /java/developerguide/gridweb/rowsandcolumns/working+with+rows+and+columns+gridweb/
---

# Aspose.Cells for Java : Working with Rows and Columns GridWeb



{{< panel title="Contents Summary" style="primary" >}}
*   1 [Inserting Rows and Columns](#inserting-rows-and-columns)
    *   1.1 [Inserting Rows](#inserting-rows)
    *   1.2 [Inserting Columns](#inserting-columns)
*   2 [Deleting Rows and Columns](#deleting-rows-and-columns)
    *   2.1 [Deleting Rows](#deleting-rows)
    *   2.2 [Deleting Columns](#deleting-columns)
*   3 [Setting Row Height and Column Width](#setting-row-height-and-column-width)
    *   3.1 [Working with Row Heights and Column Width](#working-with-row-heights-and-column-width)
        *   3.1.1 [Setting Row Height](#setting-row-height)
        *   3.1.2 [Setting Column Width](#setting-column-width)
*   4 [Customizing Row and Column Headers](#customizing-row-and-column-headers)
    *   4.1 [Customizing Row Header](#customizing-row-header)
    *   4.2 [Customizing Column Header](#customizing-column-header)
*   5 [Freeze and Unfreeze Rows and Columns](#freeze-and-unfreeze-rows-and-columns)
    *   5.1 [Freezing Rows & Columns](#freezing-rows-&-columns)
    *   5.2 [Unfreezing Rows & Columns](#unfreezing-rows-&-columns)
*   6 [Protecting Rows and Columns](#protecting-rows-and-columns)
    *   6.1 [Restricting Context Menu Options](#restricting-context-menu-options)
{{< /panel >}}
 

 

## Inserting Rows and Columns

This topic explains how to insert new rows and columns into a worksheet using the Aspose.Cells.GridWeb API. Rows or columns can be inserted at any position in the worksheet.

### Inserting Rows

To insert a row at any position in a worksheet:

1.  Add the Aspose.Cells.GridWeb control to the Web Form or page.
2.  Access the worksheet you're adding rows to.
3.  Insert a row by specifying a row index where the row would be inserted.

### Inserting Columns

To insert a column at any position in a worksheet:

1.  Add the Aspose.Cells.GridWeb control to a Web Form or page.
2.  Access the worksheet you're adding columns to.
3.  Insert a column by specifying the column index where the column would be inserted.

You can also use `insertRows()/insertColumns()` methods to insert multiple rows/columns into the worksheets accordingly.

## Deleting Rows and Columns

This topic demonstrates how to delete rows and columns from a worksheet using the Aspose.Cells.GridWeb API. With the help of this feature, developers can take delete rows or columns at runtime.

### Deleting Rows

To delete a row from your worksheet:

1.  Add the Aspose.Cells.GridWeb control to a Web Form or page.
2.  Access the worksheet you want to delete rows from.
3.  Delete a row from the worksheet by specifying its row index.

### Deleting Columns

To delete a column from your worksheet:

1.  Add the Aspose.Cells.GridWeb control to a Web Form or page.
2.  Access the worksheet you want to delete columns from.
3.  Delete a column from the worksheet by specifying its column index.

## Setting Row Height and Column Width

Sometimes cell values are wider than the cell they are in or are on several lines. Such values are not fully visible to users unless they change the height and width of rows and columns. Aspose.Cells.GridWeb fully supports setting row heights and column width. This topic discusses these features in detail with the help of examples.

### Working with Row Heights and Column Width

#### Setting Row Height

To set the height of a row:

1.  Add the Aspose.Cells.GridWeb control to your Web Form/ page.
2.  Access the worksheet's `GridCells` collection.
3.  Set the height of all cells in any specified row.

Aspose.Cells.GridWeb accepts row height and column width measurements in points, inches, pixels, etc.

**Output: the height of the 1st row has been set to 50 points**  
![image](https://docs2.aspose.com/cells/java/attachments/5276822/5472813.png)

#### Setting Column Width

To set the width of a column:

1.  Add the Aspose.Cells.GridWeb control to your Web Form/ page.
2.  Access the worksheet's `GridCells` collection.
3.  Set the width of all cells in any specified column.

## Customizing Row and Column Headers

Like Microsoft Excel, Aspose.Cells.GridWeb also uses standard headers or captions for rows (numbers like 1, 2, 3 and so on) and columns (alphabetic like A, B, C and so on). Aspose.Cells.GridWeb also makes it possible to customize captions. This topic discusses customizing row and column headers at runtime using Aspose.Cells.GridWeb API.

### Customizing Row Header

To customize the header or caption of a row:

1.  Add the Aspose.Cells.GridWeb control to a Web Form/ page.
2.  Access the worksheet in the `GridWorksheetCollection`.
3.  Set the caption of any specified row.

**The headers of row 1 and 2 have been customized**  
![image](https://docs2.aspose.com/cells/java/attachments/5276822/5472809.png)

### Customizing Column Header

To customize the header or caption of a column:

1.  Add the Aspose.Cells.GridWeb control to a Web Form/ page.
2.  Access the worksheet in the `GridWorksheetCollection`.
3.  Set the caption of any specified column.

**The headers of column 1 and 2 have been customized**  
![image](https://docs2.aspose.com/cells/java/attachments/5276822/5472808.png)

## Freeze and Unfreeze Rows and Columns

This topic explains how to freeze and unfreeze rows and columns. Freezing columns or rows allows users to keep the column headings or row titles visible while they scroll to other parts of the worksheet. This feature is very helpful when working with worksheets that contain large volumes of data. When users scroll only data is scrolled down and the headings stay in place, making the date easier to read. The freeze panes feature is only supported in Internet Explorer 6.0 or above.

### Freezing Rows & Columns

To freeze a specific number of rows and columns:

1.  Add the Aspose.Cells.GridWeb control to a Web Form/ page.
2.  Access a worksheet.
3.  Freeze a number of rows & columns.

It is also possible to freeze a specific number of rows & columns using the interface. Right-click a cell where you want to freeze rows & columns and select **Freeze** from the list.

**Rows & columns in a frozen state**  
![image](https://docs2.aspose.com/cells/java/attachments/5276822/5472789.png)

### Unfreezing Rows & Columns

To unfreeze rows and columns:

1.  Add the Aspose.Cells.GridWeb control to a Web Form/ page.
2.  Access a worksheet.
3.  Unfreeze rows & columns.

**Worksheet after being unfrozen**  
![image](https://docs2.aspose.com/cells/java/attachments/5276822/5472788.png)

## Protecting Rows and Columns

This topic discusses a few techniques for protecting cells in rows and columns from any kind of action performed by end users. Developers can implement this protection using two techniques: by making cells in rows and columns read-only, or by restricting the GridWeb's context menu options.

### Restricting Context Menu Options

GridWeb provides a context menu that end users can use to perform operations on the control. The menu provides many options for manipulating cells, rows, and columns.

**Complete contextual options**  
![image](https://docs2.aspose.com/cells/java/attachments/5276822/5472785.png)

It is possible to restrict any kind of client-side operations on rows and columns by restricting the options available in the context menu. It can be done by setting the `EnableClientColumnOperations` and `EnableClientRowOperations` attributes of the GridWeb control to false. It is also possible to restrict users from freezing rows and columns by setting the GridWeb control's `EnableClientFreeze` attribute to false.

**Context menu after restricting row & column options**  
![image](https://docs2.aspose.com/cells/java/attachments/5276822/5472784.png)

