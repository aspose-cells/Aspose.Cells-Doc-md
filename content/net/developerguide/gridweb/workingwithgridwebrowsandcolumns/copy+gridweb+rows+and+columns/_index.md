---
title : "Copy GridWeb Rows and Columns" 
description : "" 
weight : 16706 
toc : false
type: docs
url: /net/developerguide/gridweb/workingwithgridwebrowsandcolumns/copy+gridweb+rows+and+columns/
---

# Aspose.Cells for .NET : Copy GridWeb Rows and Columns


Aspose.Cells.GridWeb component offers the means to copy row & column while using the `GridCells` class. This article demonstrates the usage of APIs exposed by the Aspose.Cells.GridWeb to copy rows & columns on GridWeb interface.

The `GridCells.CopyRow`, `GridCells.CopyColumn`, `GridCells.CopyRows` & `GridCells.CopyColumns` methods will copy the contents, styling & formulas from the source row & column to destination.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Copying Rows & Columns](#copying-rows-&-columns)
    *   1.1 [Copying Single Row](#copying-single-row)
    *   1.2 [Copying Single Column](#copying-single-column)
    *   1.3 [Copying Multiple Rows](#copying-multiple-rows)
    *   1.4 [Copying Multiple Columns](#copying-multiple-columns)
{{< /panel >}}
 

## Copying Rows & Columns

If you are not already acquainted with Aspose.Cells.GridWeb component, we strongly suggest you to check the [Introduction to Aspose.Cells.GridWeb](http://www.aspose.com/docs/display/cellsnet/Introduction+of+GridWeb) and detailed article on [How to add Aspose.Cells.GridWeb component in a WebForms application](http://www.aspose.com/docs/display/cellsnet/Creating+Control+on+a+Web+Form).

### Copying Single Row

In order to keep the example simple, the article uses an existing spreadsheet with one row and a simple formula that sums all the values in the row. Here is how the spreadsheet is displayed in the Aspose.Cells.GridWeb interface before copying the row.

![image](5115392.png)

The code snippet is simple as demonstrated below. It accesses `GridCells` object of active worksheet order to make a copy of the first row to the subsequent row.

  
Here is how the Aspose.Cells.GridWeb looks after copy row operation.

![image](5115391.png)

### Copying Single Column

The following example uses an existing spreadsheet with one column and a simple formula that sums all the values in the column. Here is how the spreadsheet is displayed in the Aspose.Cells.GridWeb interface before copying the column.

![image](5115394.png)

Similar to the above example, the following code snippet accesses the `GridCells` object of active worksheet order to make a copy of the first column to the subsequent column.

Here is how the Aspose.Cells.GridWeb looks after copy column operation.

![image](5115393.png)

You may use the `GridCells.CopyRow` & `GridCells.CopyColumn` methods in loop to copy the source row & column to multiple rows & columns respectively.

### Copying Multiple Rows

It is also possible to copy multiple rows to a new destination while using the `GridCells.CopyRows` method, which takes an additional parameter of type integer to specify the number of source rows to be copied.

Here is how Aspose.Cells.GridWeb look before & after copy rows operation.

![image](5115396.png)

![image](5115395.png)

### Copying Multiple Columns

The `GridCells` class also provide the `CopyColumns` method, which takes an additional parameter of type integer to specify the number of source columns to be copied.

Here is how Aspose.Cells.GridWeb look before & after copy rows operation.

![image](5115398.png)

![image](5115397.png)

