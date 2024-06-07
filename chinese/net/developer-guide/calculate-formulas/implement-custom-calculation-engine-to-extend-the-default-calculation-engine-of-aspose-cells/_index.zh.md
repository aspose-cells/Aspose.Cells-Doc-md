---
title: 实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎
description: 本文描述了如何使用Aspose.Cells库通过实现自定义计算引擎扩展默认的计算引擎。通过加载现有的Excel文件或创建新文件，我们可以使用Aspose.Cells提供的方法实现自定义计算引擎并获取结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells、Excel、自定义计算引擎、扩展默认的计算引擎
type: docs
weight: 80
url: /zh/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **实现自定义计算引擎**

Aspose.Cells具有强大的计算引擎，几乎可以计算所有的Microsoft Excel公式。尽管如此，它还允许您扩展默认计算引擎，从而为您提供更大的权力和灵活性。

实现此功能时，使用以下属性和类。

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[CalculationData](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

以下代码实现了自定义计算引擎。它实现了接口**[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**，该接口具有**[Calculate(CalculationData data)](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)**方法。此方法针对所有公式进行调用。在此方法中，我们捕获**TODAY**函数并将系统日期加一天。因此，如果当前日期为2023年7月27日，则自定义引擎将将TODAY()计算为2023年7月28日。

### **编程示例**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **结果**

请检查上述示例代码的控制台输出，具有自定义引擎的A1的值（日期时间）应比没有自定义引擎的结果晚一天。

### **相关文章**

{{% alert color="primary" %}}

[在不将其写入工作表的情况下直接计算自定义函数](/cells/zh/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
