---
title: 在工作表中应用条件格式
type: docs
weight: 40
url: /zh/cpp/apply-conditional-formatting-in-worksheet/
---
##  **可能的使用场景**
Aspose.Cells 允许您添加各种条件格式，例如公式、高于平均值、色标、数据栏、图标集、Top10 等。它提供了[格式条件](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/)类，它具有应用您选择的条件格式所需的所有方法。以下是一些 Get 方法的列表。

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
##  **在工作表中应用条件格式**
以下示例代码演示如何在单元格 A1 和 B2 上添加 Cell 值条件格式。请参阅[输出Excel文件](23167004.xlsx)由代码生成，下面的屏幕截图解释了代码对[输出Excel文件](23167004.xlsx)。如果您在单元格 A2 和 B2 中输入大于 100 的值，单元格 A1 和 B2 中的红色填充颜色将会消失。

![待办事项：图像_替代_文本](apply-conditional-formatting-in-worksheet_1.png)
##  **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
