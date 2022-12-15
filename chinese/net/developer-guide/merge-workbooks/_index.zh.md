---
title: 将多个工作簿合并为一个工作簿
linktitle: 工作簿合并
type: docs
weight: 66
url: /zh/net/combine-multiple-workbooks-into-a-single-workbook/
---
{{% alert color="primary" %}}

有时，您需要将包含图像、图表和数据等各种内容的工作簿合并到一个工作簿中。 Aspose.Cells 支持此功能。本文介绍如何使用 Aspose.Cells 在 Visual Studio 中创建控制台应用程序并将工作簿与几行简单的代码结合起来。

{{% /alert %}}

## **将工作簿与图像和图表相结合**

示例代码使用 Aspose.Cells 将两个工作簿组合成一个工作簿。代码加载源工作簿，使用[**工作簿.combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine)组合它们并保存输出工作簿的方法。

### **源工作簿**

- [图表.xlsx](5473097.xlsx)
- [图片.xlsx](5473096.xlsx)

### **输出工作簿**

- [组合.xlsx](5473095.xlsx)

### **截图**

以下是源工作簿和输出工作簿的屏幕截图。

{{% alert color="primary" %}}

您可以使用任何源工作簿。这些图像仅用于说明目的。

{{% /alert %}}

**图表工作簿的第一个工作表 - 堆叠** 

![待办事项：图像_替代_文本](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**图表工作簿的第二个工作表 - 线** 

![待办事项：图像_替代_文本](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**图片工作簿的第一个工作表——图片** 

![待办事项：图像_替代_文本](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**组合工作簿中的所有三个工作表 - 堆叠、线条、图片** 

![待办事项：图像_替代_文本](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CombineMultipleWorkbooksSingleWorkbook-1.cs" >}}

## **推进主题**
- [将多个工作表合并为一个工作表](/cells/zh/net/combine-multiple-worksheets-into-a-single-worksheet/)
- [合并文件](/cells/zh/net/merge-files/)
