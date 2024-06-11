---
title: 在工作表中访问GridCell
type: docs
weight: 10
url: /zh/net/aspose-cells-griddesktop/access-cell-in-a-worksheet/
keywords: GridDesktop,GridCell,get cell
description: 本文介绍如何在GridDesktop的工作表中获取单元格对象(GridCell)。
---

{{% alert color="primary" %}} 

到目前为止，我们已经讨论了如何处理工作表、行和列，但现在是时候更深入地谈论单元格了。因此，在本话题中，我们将从访问单元格的基本特性开始讨论单元格。

{{% /alert %}} 
## **在工作表中访问单元格**
我们可以使用Aspose.Cells.GridDesktop的API访问工作表的任何单元格。以下是访问单元格的三种可能方式：

- **使用单元格名称**
- **使用行和列索引**
- **获取焦点单元格**

让我们依次讨论上述三种方法。
### **使用单元格名称**
工作表中的所有单元格都有唯一的名称。例如，A1、A2、B1、B2等。Aspose.Cells.GridDesktop允许开发人员使用单元格名称访问任何需要的单元格。我们所需要做的就是将单元格名称(作为索引)传递给**Worksheet**的**Cells**集合。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}

**注意**

使用 cells[cellName] 访问 GridCell 可能会消耗更多内存，它将始终创建一个新的单元格(GridCell)对象，无论该单元格是否为空。

### **使用单元格的行和列索引**

**最佳实践**

如果我们想要获取单元格值或单元格样式，不希望进行更新操作，可以使用 **CheckCell** 方法，如果单元格不存在，则返回 null。这将能够 **节省内存**。
~~~C#
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// 使用行和列索引访问单元格
GridCell cell = sheet.Cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~

工作表中的单元格还可以通过其行和列索引的方式来识别。我们只需将单元格的行和列索引传递给工作表的Cells集合即可。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}

**注意**

使用cells[rowIndex, columnIndex]访问GridCell可能会消耗更多内存，它将始终创建一个新的单元格（GridCell）对象，无论单元格是否为空。


### **获取焦点单元格**
如果您不准确地知道要访问哪个单元格。那么，Aspose.Cells.GridDesktop也允许您访问当前用户焦点的单元格。使用此功能，您可以允许用户选择任何单元格，然后您可以在后台访问该单元格。只需使用工作表的GetFocusedCell方法即可轻松实现。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}

**最佳实践**
### 遍历单元格
如果我们想要逐个访问工作表中的所有单元格，可以使用 **迭代器** 来遍历已存在的单元格。这将 **节省内存**。
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();

   GridCells cells = sheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
比较以下**不好**的代码，这将创建所有的单元格对象，无论是否为空，这将导致内存问题，请**不要**使用这种方式
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

