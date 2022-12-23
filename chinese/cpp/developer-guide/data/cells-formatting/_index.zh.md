---
title: Cells 格式化
type: docs
weight: 50
url: /zh/cpp/cells-formatting/
---
## **格式 Cell 或范围 Cells**
如果要格式化单元格或单元格区域，则 Aspose.Cells 提供[风格](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_style)班级。您可以使用此类完成单元格或单元格区域的所有格式设置。以下是一些与格式化相关的事情，可以用 IStyle 类完成

- 设置单元格的填充颜色
- 设置单元格的文字换行
- 设置单元格的边框，如上、左、下、右边框等。
- 设置字体颜色、字体大小、字体名称、删除线、粗体、斜体、下划线等。
- 将文本水平或垂直对齐方式设置为右对齐、左对齐、上对齐、下对齐、居中对齐等。

如果要设置单个单元格的样式，请使用[ICell->SetIStyle() 函数](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#afa3d5b2aa5e90b286effc9e92de59dd5)方法，如果你想设置一系列单元格的样式，那么请使用[IRange->ApplyIStyle()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#aaad6703b803565b674999bbaf5eed3a0)方法。
## **示例代码**
以下示例代码以各种方式对工作表的单元格 C4 进行格式化，屏幕截图显示了[输出excel文件](21266438.xlsx)由它生成供您参考。

![待办事项：图片_替代_文本](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells.cpp" >}}
