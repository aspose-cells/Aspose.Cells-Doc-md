---
title: 操作数据透视表
type: docs
weight: 20
url: /zh/cpp/manipulate-pivot-table/
---
##  **可能的使用场景**
除了创建新的数据透视表之外，您还可以操作新的和现有的数据透视表。您可以更改数据透视表源范围内的数据，然后刷新并计算并获得数据透视表单元格的新值。请用[数据透视表.RefreshData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/)和[数据透视表.CalculateData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/)更改数据透视表源范围中的值后刷新数据透视表的方法。
##  **操作数据透视表**
以下示例代码加载[示例 Excel 文件](23167013.xlsx)并访问其第一个工作表内的现有数据透视表。它更改数据透视表源范围内的单元格 B3 的值，然后刷新数据透视表。在刷新数据透视表之前，它访问数据透视表单元格 H8 的值，即 15，刷新数据透视表后，其值更改为 6。请参阅[输出Excel文件](23167014.xlsx)使用此代码生成的屏幕截图显示了示例代码对示例 excel 文件的影响。另请参阅下面的控制台输出，其中显示刷新数据透视表之前和之后数据透视表单元格 H8 的值。

![待办事项：图像_替代_文本](manipulate-pivot-table_1.png)
##  **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable-new.cpp" >}}
##  **控制台输出**
下面是使用提供的命令执行上述示例代码时的控制台输出[示例 Excel 文件](23167013.xlsx).

{{< highlight "java" >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
