---
title: 自定义函数直接计算，无需写在工作表中
type: docs
weight: 90
url: /zh/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
## **自定义函数直接计算，无需写在工作表中**

本主题说明如何直接计算自定义函数而无需先将它们写入工作表。请使用[**Worksheet.CalculateFormula（字符串公式，CalculationOptions opts）**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)为此目的的方法。

请参阅下面的示例代码，该代码说明了此方法的用法。我们使用了一个名为 MyCompany.CustomFunction() 的自定义函数，并将其值计算为“Aspose.Cells”。由我们自己计算，然后该值自动与计算引擎“欢迎使用”的单元格 A1 的值连接，最终计算值返回为“欢迎使用 Aspose.Cells。”。正如您在我们的代码中看到的没有在工作表中的任何地方编写我们的自定义函数，它是由我们自己的自定义逻辑直接计算的。

### **编程范例**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **控制台输出**

下面是上述示例代码的控制台输出。

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **相关文章**

{{% alert color="primary" %}}

[实施自定义计算引擎以扩展 Aspose.Cells 的默认计算引擎](/cells/zh/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
