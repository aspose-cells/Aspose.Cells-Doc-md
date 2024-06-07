---
title: 访问工作表单元格
type: docs
weight: 10
url: /zh/net/aspose-cells-gridweb/access-worksheet-cell/
keywords: GridWeb,cell,GridCell
description: 本文介绍如何在GridWeb中获取单元格(GridCell)。
---

{{% alert color="primary" %}} 

该主题讨论单元格，查看Aspose.Cells.GridWeb的最基本功能：访问单元格。

{{% /alert %}} 
## **在工作表中访问单元格**
每个工作表都包含一个名为Cells的属性，实际上是GridCell对象的集合，其中GridCell对象表示Aspose.Cells.GridWeb中的一个单元格。可以使用Aspose.Cells.GridWeb来访问任何单元格。下面讨论了两种优选的方法。


### **使用单元格名称**
所有单元格都有唯一的名称。例如，A1，A2，B1，B2等。Aspose.Cells.GridWeb允许开发人员通过使用单元格名称来访问任何所需的单元格。只需将单元格名称(作为索引)传递到GridWorksheet的Cells集合中。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


**注意**

使用cells[cellName]访问GridCell可能会消耗更多内存，无论该单元格是否为空，它都会始终创建一个新的单元格(GridCell)对象。


### **使用行和列索引**


一个单元格也可以通过其行和列索引的位置来识别。只需将单元格的行和列索引传递给GridWorksheet的Cells集合。这种方法比上面的方法更快。

**最佳实践**：

如果我们想要获取单元格的值或单元格样式，并且不想进行更新操作，我们可以使用**CheckCell**方法，如果单元格不存在，它将返回null。这将**节省内存**。
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   GridCell cell = cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}



**最佳实践**：
### 遍历单元格
如果我们想逐个访问工作表中的所有单元格，我们可以使用**迭代器**来遍历已存在的单元格。 这将**节省内存**。
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
比较下面的**糟糕代码**，这将创建所有单元格对象，无论它是否为空，这将导致内存问题，请**不要**使用这种方法
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
