---
title: 在工作表中应用条件格式
description: 如何在C#中使用Aspose.Cells库在工作表中应用条件格式。通过调整这些条件，您可以更好地控制单元格的外观。
keywords: Aspose.Cells, 条件格式, C#, 工作表, 格式
type: docs
weight: 130
url: /zh/net/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

本文旨在提供如何在工作表的一系列单元格中添加条件格式的详细理解。

条件格式是Microsoft Excel中的高级功能，允许您为一系列单元格应用格式，并根据单元格的值或公式的值更改格式。例如，单元格的背景可能是红色以突出显示负值，或正值可能为绿色的文本颜色。当单元格的值符合格式条件时，将应用该格式。如果单元格的值不符合格式条件，则使用单元格的默认格式。

通过Microsoft Office Automation 可以应用条件格式，但这样做存在其缺点。涉及了几个原因和问题：例如，安全性，稳定性，可伸缩性和速度。寻找另一种解决方案的主要原因是Microsoft自己强烈建议不要在软件解决方案中使用Office Automation。

本文展示如何创建一个控制台应用程序，并在几行最简单的代码中使用Aspose.Cells API在单元格上添加条件格式。

{{% /alert %}}

## **使用Aspose.Cells根据单元格值应用条件格式**

1. **下载并安装Aspose.Cells**。
   1. 下载Aspose.Cells for .NET。
1. 在开发计算机上安装它。
   所有Aspose组件在安装时都以评估模式运行。评估模式没有时间限制，只会在生成的文档中插入水印。
1. **创建一个项目**。
   启动Visual Studio.NET并创建一个新的控制台应用程序。本示例创建了一个C#控制台应用程序，但您也可以使用VB.NET。
1. **添加引用**。
   向您的项目添加对Aspose.Cells的引用，例如添加对….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll的引用
1. *根据单元格值应用条件格式。
   以下是用于完成任务的代码。我在一个单元格上应用了条件格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

执行上述代码后，将在output.xls的第一个工作表中的单元格“A1”上应用条件格式。应用于A1的条件格式取决于单元格值。如果A1的单元格值介于50和100之间，则由于应用了条件格式，背景颜色为红色。

## **使用Aspose.Cells根据公式应用条件格式**

1. 根据公式应用条件格式（代码片段）
   以下是用于完成任务的代码。它在B3上应用了条件格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

执行上述代码后，将在output.xls的第一个工作表中的单元格“B3”上应用条件格式。应用的条件格式取决于计算“B3”值的公式，即B1和B2的总和。
