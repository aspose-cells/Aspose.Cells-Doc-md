---
title: Access Worksheet Cell
type: docs
weight: 10
url: /net/aspose-cells-gridweb/access-worksheet-cell/
keywords: GridWeb,cell,GridCell
description: This article introduces how to get cell (GridCell) in GridWeb.
---

{{% alert color="primary" %}} 

This topic discusses cells, looking at Aspose.Cells.GridWeb's most basic feature: accessing cells.

{{% /alert %}} 
## **Accessing Cells in a Worksheet**
Each worksheet contains a property by the name of Cells that is actually a collection of GridCell objects where a GridCell object represents a cell in Aspose.Cells.GridWeb. It is possible to access any cell using Aspose.Cells.GridWeb. There are two preferred methods, each of which is discussed below.


### **Using Cell Name**
All cells have a unique name. For example, A1, A2, B1, B2 etc. Aspose.Cells.GridWeb allows developers to access any desired cell by using the cell name. Simply pass the cell name (as an index) to the Cells collection of the GridWorksheet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


**Notice**

Access GridCell using cells[cellName] may consume more memory.it will always create a new cell (GridCell) object no matter whether the the cell is null.


### **Using Row & Column Indices**
~~

A cell can also be recognized by its location in terms of row and column indices. Just pass a cell's row and column indices to the Cells collection of the GridWorksheet. This approach is more faster than the above one.

**Best Practices**:

if we want to get the cell value or cell style and do not want to do the update operation,we can use **CheckCell** method which will return null if the cell does not exist.this will **save memory**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   GridCell cell = cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}



**Best Practices**:
### Iterate over the cells
if we want to access all the cells in the worksheet one by one, we can use **iterators** to  traverse the existed cells. this will **save memory**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
compare the below code which is **bad**  ,this will create all the cells object no matter whether it is null,thus will cause memory issues,so please **do not** use this way
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r< cells.MaxRow;r++)
 {
     for(int c=0;c< cells.MaxColumn; c++)
     {
         Console.WriteLine(cells[r,c].ToString());
     }
 }
~~~
