---
title: 在工作表中应用条件格式
description: 如何在C#中使用Aspose.Cells库在工作表中应用条件格式。通过调整这些条件，您可以更好地控制单元格的外观。
keywords: Aspose.Cells，条件格式化，C#，工作表，格式化
type: docs
weight: 130
url: /zh/net/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

本文旨在详细介绍如何向工作表的一系列单元格添加条件格式。

条件格式是Microsoft Excel中的一个高级功能，允许您对一系列单元格应用格式，并且根据单元格的值或公式的值进行格式更改。例如，单元格的背景可能显示为红色以突出显示负值，或者正值的文字颜色可能为绿色。当单元格的值满足格式条件时，将应用格式。如果单元格的值不满足格式条件，则使用单元格的默认格式。

使用Microsoft Office Automation可以应用条件格式，但这有其缺点。涉及几个原因和问题：例如，安全性，稳定性，可扩展性和速度。寻找另一个解决方案的主要原因是，Microsoft本身强烈建议不要在软件解决方案中使用Office Automation。

本文展示了如何使用Aspose.Cells API在单元格上添加条件格式的几行简单的代码来创建一个控制台应用程序。

{{% /alert %}}

## **使用Aspose.Cells根据单元格值应用条件格式**

1. **下载并安装Aspose.Cells**。
   1. 下载 Aspose.Cells for .NET。
1. 在您的开发计算机上安装它。
   所有Aspose组件在安装后都处于评估模式。评估模式没有时间限制，只会在生成的文档中插入水印。
1. **创建一个项目**。
   启动Visual Studio.NET并创建一个新的控制台应用程序。该示例创建了一个C#控制台应用程序，但您也可以使用VB.NET。
1. **添加引用**。
   向项目添加对Aspose.Cells的引用，例如添加对….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll的引用。
1. *根据单元格值应用条件格式。
   下面是用于完成任务的代码。它应用了一个单元格的条件格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

执行上述代码后，在输出文件（output.xls）的第一个工作表中的单元格“A1”上应用了条件格式。应用于A1的条件格式取决于单元格的值。如果A1的单元格值在50到100之间，则由于应用了条件格式，背景颜色为红色。

## **使用Aspose.Cells根据公式应用条件格式**

1.根据公式应用条件格式（代码片段）
   以下是完成任务的代码。它在B3上应用条件格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

执行以上代码后，在输出文件的第一个工作表（output.xls）中的单元格“B3”应用条件格式。应用的条件格式取决于计算“B3”值的公式，该公式将B1和B2相加。
{{< app/cells/assistant language="csharp" >}}
