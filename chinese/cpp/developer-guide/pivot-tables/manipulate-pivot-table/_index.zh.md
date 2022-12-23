---
title: 操纵数据透视表
type: docs
weight: 20
url: /zh/cpp/manipulate-pivot-table/
---
## **可能的使用场景**
除了创建新的数据透视表之外，您还可以操作新的和现有的数据透视表。您可以更改数据透视表的源范围内的数据，然后刷新并计算它并获得数据透视表单元格的新值。请用[IPivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/class/aspose.cells.pivot.i_pivot_table#ab6d71ded346508a1d4a93c59680ddaf6)和[IPivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/class/aspose.cells.pivot.i_pivot_table#a3d6ffec8ce2a7a4ccb58e0452a1733dd)更改数据透视表源范围内的值以刷新数据透视表后的方法。
## **操纵数据透视表**
下面的示例代码加载[示例 excel 文件](23167013.xlsx)并访问其第一个工作表内的现有数据透视表。它更改数据透视表源范围内的单元格 B3 的值，然后刷新数据透视表。在刷新数据透视表之前，它访问数据透视表单元格 H8 的值为 15，刷新数据透视表后，其值变为 6。请参阅[输出excel文件](23167014.xlsx)使用此代码生成，屏幕截图显示示例代码对示例 excel 文件的影响。另请参阅下面的控制台输出，其中显示刷新数据透视表前后数据透视表单元格 H8 的值。

![待办事项：图片_替代_文本](manipulate-pivot-table_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable.cpp" >}}
## **控制台输出**
以下是使用提供的执行时上述示例代码的控制台输出[示例 excel 文件](23167013.xlsx).

{{< highlight "java" >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
