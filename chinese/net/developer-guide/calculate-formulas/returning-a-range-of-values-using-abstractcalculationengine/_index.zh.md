---
title: 使用AbstractCalculationEngine返回一系列值
description: 本文介绍了在 Microsoft Excel 中使用 Aspose.Cells 库返回一系列值的抽象计算引擎。通过加载现有的 Excel 文件或创建新的 Excel 文件，我们可以使用 Aspose.Cells 提供的方法获得一系列值并返回结果。最后，将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells, Excel, 返回一系列值的抽象计算引擎
type: docs
weight: 55
url: /zh/net/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells提供[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)类，用于实现Microsoft Excel不支持的用户定义或自定义函数。

本文将解释如何从[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)返回值范围。

{{% /alert %}}

以下代码演示了使用 [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) 类，并通过其方法返回一系列值。

创建一个带有函数 *CalculateCustomFunction* 的类。该类实现了 [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

现在将以上函数用于您的程序

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
