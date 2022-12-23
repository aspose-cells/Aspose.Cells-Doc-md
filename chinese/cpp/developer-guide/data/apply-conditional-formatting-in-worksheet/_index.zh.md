---
title: 在工作表中应用条件格式
type: docs
weight: 40
url: /zh/cpp/apply-conditional-formatting-in-worksheet/
---
## **可能的使用场景**
Aspose.Cells 允许您添加各种条件格式，例如公式、高于平均值、色标、数据栏、图标集、Top10 等。它提供了[I格式条件](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition)类，它具有应用您选择的条件格式的所有必要方法。下面是一些 Get 方法的列表。

- [GetIAboveAverage()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#aff550fd834cd78967ec440492ff012d5)
- [GetIColorScale()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a3348a7c447dc564ceabc22c9c89bd6f5)
- [GetIDataBar()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a4415a87833c41386ed1595e742485e07)
- [获取IIconSet()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a011b2c7dbaaf671819d09f5d1df865e3)
- [GetITop10()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a64388aaf1b43811f5ee1ee3090c9bd4a)
## **在工作表中应用条件格式**
以下示例代码显示如何在单元格 A1 和 B2 上添加 Cell 值条件格式。请参阅[输出excel文件](23167004.xlsx)由代码生成，下面的截图解释了代码对[输出excel文件](23167004.xlsx).如果您在单元格 A2 和 B2 中输入大于 100 的值，则单元格 A1 和 B2 中的红色填充颜色将消失。

![待办事项：图片_替代_文本](apply-conditional-formatting-in-worksheet_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet.cpp" >}}
