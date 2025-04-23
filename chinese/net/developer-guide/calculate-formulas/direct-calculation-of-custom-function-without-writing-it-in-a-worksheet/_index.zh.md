---
title: 直接计算自定义函数，无需先将其编写在工作表中
description: 本文介绍如何使用Aspose.Cells库在Microsoft Excel中直接计算自定义函数，而无需在工作表中编写函数。 通过加载现有的Excel文件或创建一个新的Excel文件，我们可以使用Aspose.Cells提供的方法来计算自定义函数并获得结果。 最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, 自定义函数, 直接计算, 无需书写, 工作表
type: docs
weight: 90
url: /zh/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **在不将其写入工作表的情况下直接计算自定义函数**

本主题解释了如何在不首先在工作表中编写自定义函数的情况下直接计算您的自定义函数。请使用 [**Worksheet.CalculateFormula(string formula, CalculationOptions opts)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) 方法来实现这一目的。

请参阅以下示例代码，演示了如何使用此方法。我们使用了一个名为 MyCompany.CustomFunction() 的自定义函数，并且通过自己的自定义逻辑计算其值为 "Aspose.Cells."，然后该值由计算引擎自动地与单元格 A1 的值 "Welcome to " 进行连接，最终计算的值返回为 "Welcome to Aspose.Cells."。从代码中可以看到，我们并未在工作表中编写自定义函数，而是直接通过我们自己的自定义逻辑进行计算。

### **编程示例**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **控制台输出**

以下是上面示例代码的控制台输出。

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **相关文章**

{{% alert color="primary" %}}

[实现自定义计算引擎以扩展 Aspose.Cells 的默认计算引擎](/cells/zh/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
