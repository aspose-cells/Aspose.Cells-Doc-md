﻿---
title: 实施自定义计算引擎以扩展 Aspose.Cells 的默认计算引擎
type: docs
weight: 80
url: /zh/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
## **实施自定义计算引擎**

Aspose.Cells具有强大的计算引擎，可以计算几乎所有的Microsoft Excel公式。尽管如此，它还允许您扩展默认计算引擎，从而为您提供更强大的功能和灵活性。

以下属性和类用于实现此功能。

- **[计算选项.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[抽象计算引擎](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[计算数据](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

以下代码实现自定义计算引擎。它实现了接口**[抽象计算引擎](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**它有一个**[计算（CalculationData 数据）](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)**方法。针对您的所有公式调用此方法。在这个方法中，我们捕获**和**公式并将其值增加 30。因此，如果 Aspose.Cells 计算值是 20，那么我们的自定义引擎将通过添加 30 使其变为 50。

### **编程范例**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **控制台输出**

这是上述示例代码的控制台输出。

{{< highlight "java" >}}

Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}

### **相关文章**

{{% alert color="primary" %}}

[自定义函数直接计算，无需写在工作表中](/cells/zh/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}