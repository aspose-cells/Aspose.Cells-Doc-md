---
title: 访问表单元格并使用行和列偏移量在其中添加值
type: docs
weight: 230
url: /zh/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

通常，您使用[**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法在表格或列表对象内添加值。但有时，您可能需要使用行和列偏移量在表格或列表对象内添加值。

要访问单元格中的表或列表对象，请使用 [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) 方法。要使用行和列偏移量在其中添加值，请使用 [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) 方法。

{{% /alert %}}

下面的截图显示了代码中使用的源Excel文件。它包含一个空表格，并突出显示了位于表格内的单元格D5。我们将使用 [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) 方法从单元格D5访问此表，并使用 [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) 和 [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) 方法在其中添加值。

## 示例

### 比较源文件和输出文件的屏幕截图

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

下面的截图显示了代码生成的输出Excel文件。正如您所看到的，单元格D5有一个值，表格内偏移为2,2的单元格F6也有一个值。

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### 访问单元格中的表格和使用行和列偏移量在其中添加值的C#代码

以下示例代码加载了上述截图中显示的源Excel文件，并在表内添加值，生成了如上所示的输出Excel文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
