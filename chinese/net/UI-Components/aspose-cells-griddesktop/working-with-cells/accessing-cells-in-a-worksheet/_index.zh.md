---
title: 在工作表中访问GridCell
type: docs
weight: 10
url: /zh/net/aspose-cells-griddesktop/access-cell-in-a-worksheet/
keywords: GridDesktop,GridCell,获取单元格
description: 本文介绍如何在GridDesktop工作表中获取单元格对象（GridCell）
---

{{% alert color="primary" %}} 

到目前为止，我们已经讨论了如何处理工作表，行和列，但现在是时候更深入地谈论单元格了。因此，在这个话题中，我们将以访问单元格的基本功能开始我们的讨论

{{% /alert %}} 
## **访问工作表中的单元格**
我们可以使用Aspose.Cells.GridDesktop的API访问工作表中的任何单元格。有三种可能的访问单元格的方式如下:

- **使用单元格名称**
- **使用行和列索引**
- **获取焦点单元格**

让我们逐一讨论上述三种方法。
### **使用单元格名称**
工作表中的所有单元格都有唯一的名称。例如，A1、A2、B1、B2等。Aspose.Cells.GridDesktop允许开发人员通过使用其单元格名称来访问任何所需的单元格。我们只需将单元格名称（作为索引）传递给**Worksheet**的**Cells**集合即可。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}

**注意**

使用cells[cellName]访问GridCell可能会消耗更多内存，无论该单元格是否为空，它都会始终创建一个新的单元格(GridCell)对象。

### **使用单元格的行和列索引**

**最佳实践**：

如果我们想要获取单元格的值或单元格样式，并且不想进行更新操作，我们可以使用**CheckCell**方法，如果单元格不存在，它将返回null。这将**节省内存**。
~~~C#
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// 使用其行和列索引访问单元格
GridCell cell = sheet.Cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~

工作表中的一个单元格也可以使用其行和列索引的位置来标识。我们只需要将单元格的行和列索引传递给**Worksheet**的**Cells**集合即可。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}

**注意**

使用cells[rowIndex, columnIndex]访问GridCell可能会消耗更多内存，它总是会创建一个新的单元格（GridCell）对象，无论单元格是否为空。


### **获取焦点单元格**
如果你不确定要访问哪个单元格。那么Aspose.Cells.GridDesktop还允许您访问当前用户焦点的单元格。使用这个功能，您可以让用户选择任何单元格，然后您可以在后台访问该单元格。简单地通过**Worksheet**的**GetFocusedCell**方法就可以实现。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}

**最佳实践**：
### 遍历单元格
如果我们想逐个访问工作表中的所有单元格，我们可以使用**迭代器**来遍历已存在的单元格。 这将**节省内存**。
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();

   GridCells cells = sheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
比较下面的**糟糕代码**，这将创建所有单元格对象，无论它是否为空，这将导致内存问题，请**不要**使用这种方法
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 for(int r=0;r< sheet.RowsCount;r++)
 {
     for(int c=0;c< sheet.ColumnsCount; c++)
     {
         Console.WriteLine(sheet.Cells[r,c].ToString());
     }
 }
~~~

