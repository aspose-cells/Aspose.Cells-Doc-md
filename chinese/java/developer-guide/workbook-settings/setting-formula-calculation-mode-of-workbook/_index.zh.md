---
title: 设置工作簿的公式计算方式
type: docs
weight: 130
url: /zh/java/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel允许设置公式计算方式，即公式的计算方式。存在三个可能的值：

- 自动 - 每当发生更改时重新计算，以及每次打开工作簿时重新计算。
- 自动，数据表除外 - 每当发生更改时重新计算，但不包括数据表。
- 手动 - 仅当用户通过按 F9 或 CTRL+ALT+F9 明确请求时或保存工作簿时才重新计算。

{{% /alert %}}

在Microsoft Excel中设置公式计算模式：

1. 选择**公式**接着**计算选项**.
1. 选择其中一个选项。

 Aspose.Cells 还允许您设置**公式计算模式**使用[**公式设置.计算模式**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode)财产。您可以将其分配给[**计算模式类型**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType)具有以下值之一的枚举：

- [**CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.手册**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

下面的示例代码首先创建一个工作簿，然后将公式计算模式设置为**手动的**并将工作簿作为输出 Excel 文件保存在磁盘上。

**输出文件。注意公式计算方式。**

![待办事项：图像_替代_文本](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
