---
title: Cells 格式化
type: docs
weight: 50
url: /zh/cpp/cells-formatting/
---
##  **格式 Cell 或 Cells 的范围**
如果您想设置单元格或单元格范围的格式，则 Aspose.Cells 提供[风格](https://reference.aspose.com/cells/cpp/aspose.cells/style/)班级。您可以使用此类完成单元格或单元格区域的所有格式设置。可以使用 IStyle 类完成的一些与格式化相关的事情如下

- 设置单元格的填充颜色
- 设置单元格的文本换行
- 设置单元格的边框，如上、左、下、右边框等。
- 设置字体颜色、字体大小、字体名称、删除线、粗体、斜体、下划线等。
- 将文本水平或垂直对齐方式设置为右、左、上、下、居中等。

如果您想设置单个单元格的样式，请使用[Cell->设置样式()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)方法，如果你想设置一系列单元格的样式，那么请使用[范围->ApplyStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)方法。
##  **示例代码**
以下示例代码以各种方式格式化工作表的单元格 C4，屏幕截图显示了[输出Excel文件](21266438.xlsx)由其生成供您参考。

![待办事项：图像_替代_文本](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
