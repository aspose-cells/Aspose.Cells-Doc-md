---
title: 设置工作簿公式计算模式
description: 本文介绍如何在Microsoft Excel中使用Aspose.Cells库设置工作簿的公式计算模式。通过加载现有的Excel文件或者新建一个Excel文件，我们可以使用Aspose.Cells提供的方法来设置公式计算模式并得到结果。最后，我们将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells, Excel, workbook, formula calculation mode, settings
type: docs
weight: 110
url: /zh/net/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel允许设置公式计算模式，即公式的计算方式。有三个可能的值：

- 自动 - 每当发生更改以及每次打开工作簿时都会重新计算。
- 除数据表外自动 - 每当发生更改时重新计算，但忽略数据表。
- 手动 - 仅当用户通过按 F9 或 CTRL+ALT+F9 明确请求时或保存工作簿时才重新计算。

{{% /alert %}}

在Microsoft Excel中设置公式计算模式：

1. 选择**公式**然后*计算选项**。
1. 选择选项之一。

 Aspose.Cells 还允许您设置**公式计算模式**使用[**公式设置.计算模式**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode)模式属性。您可以将其分配给[**计算模式类型**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)具有以下值之一的枚举：

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
