---
title: 设置工作簿的公式计算模式
description: 该文章介绍了如何使用Aspose.Cells库在Microsoft Excel中设置工作簿的公式计算模式。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法设置公式计算模式并获取结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, 工作簿, 公式计算模式, 设置
type: docs
weight: 110
url: /zh/net/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

Microsoft Excel允许您设置公式计算模式，即公式计算的方式。有三个可能的取值：

- 自动 - 每当有更改时重新计算，以及每次打开工作簿时。
- 自动除数据表外 - 每当有更改时重新计算，但不包括数据表。
- 手动 - 仅当用户通过按F9或CTRL+ALT+F9请求显式重新计算时，或者当保存工作簿时。

{{% /alert %}}

在Microsoft Excel中设置公式计算模式：

1. 选择**公式**，然后选择**计算选项**。
1. 选择其中一个选项。

Aspose.Cells也允许您使用[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode)模式属性设置**公式计算模式**。您可以将其分配给包含以下值之一的[**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)枚举：

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
