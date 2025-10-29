---
title: 操作数据透视表
type: docs
weight: 20
url: /zh/cpp/manipulate-pivot-table/
---

## **可能的使用场景**
除了创建新的数据透视表外，您还可以操作新的和现有的数据透视表。您可以更改数据透视表的源范围中的数据，然后刷新和计算它，并获取数据透视表单元格的新值。更改数据透视表源范围中的值后，请使用[PivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) 和[PivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) 方法来刷新数据透视表。
## **操作数据透视表**
以下示例代码加载了[示例excel文件](23167013.xlsx)，并访问了它的第一个工作表中的现有数据透视表。它更改了位于数据透视表源范围内的单元格B3的值，然后刷新了数据透视表。在刷新数据透视表之前，它访问了数据透视表单元格H8的值，为15，刷新数据透视表后，其值变为6。请参阅使用此代码生成的[输出excel文件](23167014.xlsx)和显示示例代码对示例excel文件的影响的屏幕截图。还请参阅下面的控制台输出，显示刷新数据透视表前后数据透视表单元格H8的值。

![todo:image_alt_text](manipulate-pivot-table_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable-new.cpp" >}}
## **控制台输出**
以下是上述示例代码在提供的[示例excel文件](23167013.xlsx)上执行时的控制台输出。

{{< highlight java >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
