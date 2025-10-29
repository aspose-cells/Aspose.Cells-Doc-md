---
title: 在工作表中应用条件格式
linktitle: 在工作表中应用条件格式
description: 如何在 Node.js 中通过 C++ 使用 Aspose.Cells 库对工作表应用条件格式，以更好地控制单元格外观。
keywords: Aspose.Cells，条件格式，Node.js via C++，工作表，格式化
type: docs
weight: 130
url: /zh/nodejs-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

本文旨在详细介绍如何向工作表的一系列单元格添加条件格式。

条件格式是Microsoft Excel中的一个高级功能，允许您对一系列单元格应用格式，并且根据单元格的值或公式的值进行格式更改。例如，单元格的背景可能显示为红色以突出显示负值，或者正值的文字颜色可能为绿色。当单元格的值满足格式条件时，将应用格式。如果单元格的值不满足格式条件，则使用单元格的默认格式。

使用Microsoft Office Automation可以应用条件格式，但这有其缺点。涉及几个原因和问题：例如，安全性，稳定性，可扩展性和速度。寻找另一个解决方案的主要原因是，Microsoft本身强烈建议不要在软件解决方案中使用Office Automation。

本文展示了如何使用Aspose.Cells API在单元格上添加条件格式的几行简单的代码来创建一个控制台应用程序。

{{% /alert %}}

## **使用Aspose.Cells根据单元格值应用条件格式**

1. **下载并安装Aspose.Cells**。
   1. 下载 Aspose.Cells for Node.js via C++。
1. 在您的开发计算机上安装它。
   所有Aspose组件在安装后都处于评估模式。评估模式没有时间限制，只会在生成的文档中插入水印。
1. **创建一个项目**。
   开始你的 Node.js 项目，初始化它。本示例创建了一个 Node.js 控制台应用程序。
1. **添加引用**。
   向你的项目添加对 Aspose.Cells 的引用，例如通过如下方式引入包：
   ```javascript
   const AsposeCells = require("aspose.cells.node");
   ```
1. **根据单元格值应用条件格式**。
    以下是完成任务所使用的代码。它在单元格上应用了条件格式。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyToCellValue.js" >}}


 执行上述代码时，将在输出文件（output.xls）第一个工作表的“A1”单元格应用条件格式。所应用的条件格式取决于单元格值。如果A1单元格的值在50到100之间，则背景色由于条件格式而变成红色。

## **使用Aspose.Cells根据公式应用条件格式**

1.根据公式应用条件格式（代码片段）
   以下是完成任务的代码。它在B3上应用条件格式。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyToFormula.js" >}}

 执行上述代码时，将在输出文件（output.xls）第一张工作表的“B3”单元格应用条件格式。应用的条件格式取决于计算“B3”值的公式，即B1与B2之和。
{{< app/cells/assistant language="nodejs-cpp" >}}
