---
title: 在工作表中应用条件格式
type: docs
weight: 40
url: /zh/cpp/apply-conditional-formatting-in-worksheet/
---

## **可能的使用场景**
Aspose.Cells允许您添加各种条件格式，例如公式、高于平均值、颜色比例、数据条、图标集、前10名等。它提供了[FormatCondition](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/)类，该类具有应用您选择的条件格式所需的所有方法。这是一些Get方法的列表。

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
## **在工作表中应用条件格式**
以下示例代码演示了如何在单元格A1和B2上添加单元格值的条件格式。请查看代码生成的[输出Excel文件](23167004.xlsx)，以及以下截图解释了代码在[输出Excel文件](23167004.xlsx)上的效果。如果在单元格A2和B2中放入大于100的值，则从单元格A1和B2的红色填充颜色将消失。

![todo:image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
