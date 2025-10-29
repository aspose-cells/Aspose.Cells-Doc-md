---
title: 从单元格访问表格并使用行和列偏移添加值
type: docs
weight: 230
url: /zh/python-net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

通常，您可以使用 [**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool) 方法向表格或列表对象中添加值。但有时，您可能需要使用行和列偏移向表格或列表对象中添加值。

要从单元格中访问表格或列表对象，请使用 [**Cell.get_table()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_table/#) 方法。要使用行和列偏移向其中添加值，请使用 [**ListObject.put_cell_value**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/put_cell_value/#int-int-any) 方法。

{{% /alert %}}

以下截图显示了代码中使用的源Excel文件。它包含了空表格并突出显示了位于表格内的单元格D5。我们将使用[**Cell.get_table()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_table/#) 方法从单元格D5访问这个表格，然后使用[**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool) 和[**ListObject.put_cell_value**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/put_cell_value/#int-int-any) 方法向其中添加值。

## 示例

### 比较源文件和输出文件的截图

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

以下截图显示了代码生成的输出Excel文件。您可以看到单元格D5具有一个值，而位于表格偏移2,2的单元格F6也具有一个值。

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### 访问单元格中的表格并使用行列偏移添加值的Python代码

以下示例代码加载了上面截图中显示的源Excel文件，并向表格内添加值，并生成了上面所示的输出Excel文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-AccessTableFromCellAndAddValue.py" >}}
{{< app/cells/assistant language="python-net" >}}
