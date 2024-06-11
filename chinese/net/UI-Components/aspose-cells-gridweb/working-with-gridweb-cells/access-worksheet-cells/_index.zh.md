---
title: 访问工作表单元格
type: docs
weight: 10
url: /zh/net/aspose-cells-gridweb/access-worksheet-cell/
keywords: GridWeb,cell,GridCell
description: 本文介绍了如何获取 GridWeb 中的单元格(GridCell)。
---

{{% alert color="primary" %}} 

本主题讨论单元格，查看 Aspose.Cells.GridWeb 的最基本特性: 访问单元格。

{{% /alert %}} 
## **访问工作表中的单元格**
每个工作表都包含一个名为 Cells 的属性，它实际上是 Aspose.Cells.GridWeb 中的 GridCell 对象集合，其中 GridCell 对象表示一个单元格。可以使用 Aspose.Cells.GridWeb 访问任何单元格。下面讨论了两种首选方法。


### **使用单元格名称**
所有单元格都有一个唯一的名称。例如，A1、A2、B1、B2 等。Aspose.Cells.GridWeb 允许开发人员使用单元格名称访问任何所需的单元格。只需将单元格名称(作为索引)传递给 GridWorksheet 的 Cells 集合。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


**注意**

使用 cells[cellName] 访问 GridCell 可能会消耗更多内存，它将始终创建一个新的单元格(GridCell)对象，无论该单元格是否为空。


### **使用行和列索引**


单元格还可以通过其行和列索引的位置来识别。只需将单元格的行和列索引传递给 GridWorksheet 的 Cells 集合。这种方法比上述方法更快。

**最佳实践**

如果我们想要获取单元格值或单元格样式，不希望进行更新操作，可以使用 **CheckCell** 方法，如果单元格不存在，则返回 null。这将能够 **节省内存**。
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   GridCell cell = cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}



**最佳实践**
### 遍历单元格
如果我们想要逐个访问工作表中的所有单元格，可以使用 **迭代器** 来遍历已存在的单元格。这将 **节省内存**。
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
比较以下**不好**的代码，这将创建所有的单元格对象，无论是否为空，这将导致内存问题，请**不要**使用这种方式
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
