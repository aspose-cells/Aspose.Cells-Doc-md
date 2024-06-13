---
title: 实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎
description: 本文描述了如何使用 Aspose.Cells 库来扩展默认计算引擎，实现自定义计算引擎。通过加载现有的 Excel 文件或创建新文件，我们可以使用 Aspose.Cells 提供的方法实现自定义计算引擎，并获得结果。最后，将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells, Excel, 自定义计算引擎, 扩展默认计算引擎
type: docs
weight: 80
url: /zh/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **实现自定义计算引擎**

Aspose.Cells具有强大的计算引擎，可以计算几乎所有的Microsoft Excel公式。尽管如此，它还允许您扩展默认的计算引擎，从而为您提供更大的动力和灵活性。

在实现此功能中使用了以下属性和类。

- [**CalculationOptions.CustomEngine**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)

以下代码实现了自定义计算引擎。它实现了 [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) 接口，该接口具有一个 [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate) 方法。该方法会针对所有公式进行调用。在这个方法中，我们捕获了 **TODAY** 函数，并向系统日期添加了一天。因此，如果当前日期是2023年7月27日，那么自定义引擎将计算TODAY()为2023年7月28日。

### **编程示例**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **结果**

请检查上述示例代码的控制台输出，具有自定义引擎的 A1 的值（日期时间）应该比没有自定义引擎的结果晚一天。

### **相关文章**

{{% alert color="primary" %}}

[在工作表中直接计算自定义函数，无需书写](/cells/zh/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
