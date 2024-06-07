---
title: 单元格格式
type: docs
weight: 50
url: /zh/cpp/cells-formatting/
---

## **格式化单元格或一组单元格**
如果您想要格式化单元格或一组单元格，Aspose.Cells提供了 [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style/) 类。您可以使用此类完成对单元格或一组单元格的所有格式化。与 IStyle 类相关的一些格式化方法如下

- 设置单元格的填充颜色
- 设置单元格的文本换行
- 设置单元格的边框，如顶部、左侧、底部和右侧边框等
- 设置字体颜色、字体大小、字体名称、删除线、粗体、斜体、下划线等
- 将文本水平或垂直对齐方式设置为右对齐、左对齐、顶对齐、底对齐、居中等

如果要设置单个单元格的样式，请使用 [Cell->SetStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) 方法。如果要设置一组单元格的样式，请使用 [Range->ApplyStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) 方法。
## **示例代码**
以下示例代码以各种方式格式化工作表的单元格C4，并显示了代码生成的 [输出excel文件](21266438.xlsx) 的屏幕截图供您参考。

![todo:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
