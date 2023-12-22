---
title: 实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎
description: 本文介绍如何通过使用 Aspose.Cells 库实现自定义计算引擎来扩展默认计算引擎。通过加载现有的Excel文件或创建一个新的Excel文件，我们可以使用Aspose.Cells提供的方法来实现自定义计算引擎并获取结果。最后，我们将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells, Excel, Custom Calculation Engine, extends the default calculation engine
type: docs
weight: 80
url: /zh/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
##  **实施自定义计算引擎**

Aspose.Cells拥有强大的计算引擎，可以计算几乎所有Microsoft Excel公式。尽管如此，它还允许您扩展默认计算引擎，从而为您提供更大的功能和灵活性。

以下属性和类用于实现此功能。

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[计算数据](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

以下代码实现了自定义计算引擎。它实现了接口**[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**其中有一个**[计算（CalculationData数据）](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)**方法。针对您的所有公式调用此方法。在这个方法中，我们捕获**TODAY**函数并向系统日期添加一天。因此，如果当前日期是 27/07/2023，则自定义引擎会将 TODAY() 计算为 28/07/2023。

###  **编程示例**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

###  **结果**

请检查上述示例代码的控制台输出，使用自定义引擎的 A1 的值（日期时间）应该比不使用自定义引擎的结果晚一天。

###  **相关文章**

{{% alert color="primary" %}}

[自定义函数直接计算，无需将其写入工作表](/cells/zh/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
