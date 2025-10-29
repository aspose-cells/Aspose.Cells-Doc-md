---
title: 单元格格式
type: docs
weight: 50
url: /zh/cpp/cells-formatting/
---

## **格式化单元格或一系列单元格**
如果要格式化单元格或一系列单元格，那么Aspose.Cells提供[Style](https://reference.aspose.com/cells/cpp/aspose.cells/style/)类。您可以使用此类完成单元格或一系列单元格的所有格式设置。使用IStyle类可以完成一些与格式设置相关的事项，如下所示

- 设置单元格的填充颜色
- 设置单元格的文本换行
- 设置单元格的边框，如顶部、左侧、底部和右侧边框等
- 设置字体颜色、字体大小、字体名称、删除线、粗体、斜体、下划线等
- 设置文本的水平或竖直对齐方式，右对齐、左对齐、顶部对齐、底部对齐、居中等

如果要设置单个单元格的样式，请使用[Cell->SetStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)方法，如果要设置一系列单元格的样式，请使用[Range->ApplyStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)方法。
## **示例代码**
以下示例代码以各种方式格式化工作表的单元格C4，屏幕截图显示了通过代码生成的[输出Excel文件](21266438.xlsx)的参考文档。

![todo:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
