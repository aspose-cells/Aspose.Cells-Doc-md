---
title: 设置工作簿的公式计算模式
description: 本文介绍了如何使用Aspose.Cells库在Microsoft Excel中设置工作簿的公式计算模式。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法设置公式计算模式并获取结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, 工作簿, 公式计算模式, 设置
type: docs
weight: 110
url: /zh/net/setting-formula-calculation-mode-of-workbook/
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

Aspose.Cells还允许使用[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) 模式属性设置**公式计算模式**。您可以将其分配给[**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype) 枚举，该枚举具有以下值之一：

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
