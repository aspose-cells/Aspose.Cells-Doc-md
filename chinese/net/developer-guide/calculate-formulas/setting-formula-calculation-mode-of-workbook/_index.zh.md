---
title: 设置工作簿的公式计算方式
type: docs
weight: 110
url: /zh/net/setting-formula-calculation-mode-of-workbook/
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

 Aspose.Cells 还允许您设置**公式计算模式**使用[**公式设置.计算模式**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode)模式属性。您可以将其分配给[**计算模式类型**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)具有以下值之一的枚举：

- CalcModeType.自动
- CalcModeType.AutomaticExceptTable
- CalcModeType.手册

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
