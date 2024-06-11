---
title: 设置工作簿的公式计算模式
type: docs
weight: 130
url: /zh/java/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

Microsoft Excel允许您设置公式计算模式，即公式计算的方式。有三种可能的值：

- 自动 - 每当有变更时重新计算，并且每次打开工作簿时。
- 自动除数据表外 - 每当有变更时重新计算，但是不包括数据表。
- 手动 - 仅当用户通过按F9或CTRL+ALT+F9明确请求时，或者保存工作簿时重新计算。

{{% /alert %}}

在Microsoft Excel中设置公式计算模式：

1. 选择**公式**然后**计算选项**。
1. 选择其中一个选项。

Aspose.Cells还允许您使用[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode) 属性设置**公式计算模式**。您可以为其分配[**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType) 枚举，该枚举具有以下值之一：

- [**CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

以下示例代码首先创建一个工作簿，然后将公式计算模式设置为**手动**，并将工作簿保存为磁盘上的输出Excel文件。

**输出文件。注意公式计算模式。**

![todo:image_alt_text](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
