---
title: 自定义函数直接计算，无需将其写入工作表
description: 本文介绍如何使用Aspose.Cells库直接计算Microsoft Excel中的自定义函数，而无需将函数写入工作表中。通过加载现有的Excel文件或者创建一个新的Excel文件，我们可以使用Aspose.Cells提供的方法来计算自定义函数并得到结果。最后，我们将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells, Excel, custom functions, direct calculations, no need to write, worksheets
type: docs
weight: 90
url: /zh/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
##  **自定义函数直接计算，无需将其写入工作表**

本主题介绍如何直接计算自定义函数，而无需先将其写入工作表中。请使用[**Worksheet.CalculateFormula（字符串公式，CalculationOptions选项）**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)用于此目的的方法。

请参阅以下示例代码来说明此方法的用法。我们使用了名为 MyCompany.CustomFunction() 的自定义函数，并将其值计算为“Aspose.Cells”。然后这个值会被计算引擎自动与单元格 A1 的值“Welcome to”连接起来，最终计算出的值返回为“Welcome to Aspose.Cells。”。正如您在代码中看到的那样，我们有没有在工作表中的任何地方编写我们的自定义函数，它是由我们自己的自定义逻辑直接计算的。

###  **编程示例**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

###  **控制台输出**

以下是上述示例代码的控制台输出。

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

###  **相关文章**

{{% alert color="primary" %}}

[实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎](/cells/zh/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
