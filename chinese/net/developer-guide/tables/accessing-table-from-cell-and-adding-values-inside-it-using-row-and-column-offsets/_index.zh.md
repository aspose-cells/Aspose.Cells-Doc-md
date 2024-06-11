---
title: 从单元格访问表格并使用行和列偏移添加值
type: docs
weight: 230
url: /zh/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

通常，您可以使用 [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) 方法向表格或列表对象中添加值。但有时，您可能需要使用行和列偏移向表格或列表对象中添加值。

要从单元格中访问表格或列表对象，请使用 [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) 方法。要使用行和列偏移向其中添加值，请使用 [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) 方法。

{{% /alert %}}

以下截图显示了代码中使用的源Excel文件。它包含了空表格并突出显示了位于表格内的单元格D5。我们将使用[**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) 方法从单元格D5访问这个表格，然后使用[**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) 和[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) 方法向其中添加值。

## 示例

### 比较源文件和输出文件的截图

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

以下截图显示了代码生成的输出Excel文件。您可以看到单元格D5具有一个值，而位于表格偏移2,2的单元格F6也具有一个值。

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### 访问单元格内表格并使用行列偏移来添加值的C#代码

以下示例代码加载了上面截图中显示的源Excel文件，并向表格内添加值，并生成了上面所示的输出Excel文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
