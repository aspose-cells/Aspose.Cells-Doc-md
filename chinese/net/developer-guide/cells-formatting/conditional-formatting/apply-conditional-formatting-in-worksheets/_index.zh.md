---
title: 在工作表中应用条件格式
description: 如何使用 C# 中的 Aspose.Cells 库在工作表中应用条件格式。通过调整这些标准，您可以更好地控制单元格的外观和显示方式。
keywords: Aspose.Cells, Conditional Formatting, C#, Worksheet, Formatting
type: docs
weight: 130
url: /zh/net/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

本文旨在详细了解如何向工作表中的一系列单元格添加条件格式。

条件格式是 Microsoft Excel 中的一项高级功能，它允许您将格式应用于一系列单元格，并根据单元格的值或公式的值更改格式。例如，单元格的背景可以是红色以突出显示负值，或者文本颜色可以是绿色以显示正值。当单元格的值满足格式条件时，将应用该格式。如果单元格的值不满足格式条件，则使用单元格的默认格式。

可以使用 Microsoft Office Automation 应用条件格式，但这有其缺点。涉及几个原因和问题：例如安全性、稳定性、可扩展性和速度。寻找其他解决方案的主要原因是Microsoft本身强烈建议不要使用Office Automation软件解决方案。

本文展示了如何创建控制台应用程序，使用 Aspose.Cells API 通过几行最简单的代码在单元格上添加条件格式。

{{% /alert %}}

##  **使用 Aspose.Cells 根据 Cell 值应用条件格式**

1. *下载并安装Aspose.Cells**。
 1.下载Aspose.Cells for .NET。
1. 将其安装在您的开发计算机上。
所有 Aspose 组件安装后均在评估模式下工作。该评估模式没有时间限制，仅在生成的文档中注入水印。
1. *创建一个项目**。
启动 Visual Studio.NET 并创建一个新的控制台应用程序。此示例创建一个 C# 控制台应用程序，但您也可以使用 VB.NET。
1. *添加参考文献**。
将对 Aspose.Cells 的引用添加到您的项目中，例如添加对 ….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll 的引用
1. *根据单元格值应用条件格式。
下面是用于完成任务的代码。我对单元格应用条件格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

执行上述代码时，条件格式将应用于输出文件 (output.xls) 的第一个工作表中的单元格“A1”。应用于 A1 的条件格式取决于单元格值。如果 A1 的单元格值介于 50 和 100 之间，则由于应用了条件格式，背景颜色为红色。

##  **使用Aspose.Cells应用基于公式的条件格式**

1. 根据公式应用条件格式（代码片段）
下面是完成任务的代码。它在 B3 上应用条件格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

执行上述代码时，条件格式将应用于输出文件 (output.xls) 第一个工作表中的单元格“B3”。应用的条件格式取决于将“B3”值计算为 B1 和 B2 之和的公式。
