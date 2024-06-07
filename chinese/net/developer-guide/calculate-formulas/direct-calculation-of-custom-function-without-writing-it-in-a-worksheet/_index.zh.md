---
title: 在工作表中直接计算自定义函数而不将其写入
description: 本文介绍如何使用Aspose.Cells库在Microsoft Excel中直接计算自定义函数，而无需在工作表中编写函数。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法计算自定义函数并获得结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells、Excel、自定义函数、直接计算、无需编写、工作表
type: docs
weight: 90
url: /zh/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **在工作表中直接计算自定义函数而不将其写入**

此主题解释了如何直接计算自定义函数，而无需先在工作表中编写函数。请使用[**Worksheet.CalculateFormula(string formula, CalculationOptions opts)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)方法实现此目的。

请参阅以下示例代码，演示了此方法的使用。我们使用了一个名为MyCompany.CustomFunction()的自定义函数，通过自己的逻辑计算其值为"Aspose.Cells."，然后此值由计算引擎自动与单元格A1的值"Welcome to "连接，最终计算值返回为"Welcome to Aspose.Cells."。如您在上述代码中所见，我们未在工作表中编写自定义函数，而是通过我们自己的定制逻辑直接计算。

### **编程示例**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **控制台输出**

以下是上述示例代码的控制台输出。

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **相关文章**

{{% alert color="primary" %}}

[实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎](/cells/zh/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
