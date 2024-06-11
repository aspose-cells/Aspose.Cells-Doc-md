---
title: 访问工作表中的GridRow
type: docs
weight: 10
url: /zh/net/aspose-cells-gridweb/access-row-in-a-worksheet/
keywords: GridWeb, GridRow, 获取行
description: 本文介绍了如何在GridWeb工作表中获取行对象(GridRow)。
---
### 遍历行
**最佳实践**：
如果我们要逐一访问工作表中的所有行，我们可以使用**迭代器**来遍历现有的行。这样可以**节约内存**。
~~~C#

// 使用迭代器访问行
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
比较下面的代码，这将创建所有的行对象，无论是否为null，因此会导致内存问题，请**不要**使用这种方式
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
但是您可以使用CheckRow方法，以检查行是否为空
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.CheckRow(r);
     if(row==null){
       Console.WriteLine("行为空:"+r);
     }else{
       Console.WriteLine(row.Index+" "+row.Height);
     }
 }
~~~
