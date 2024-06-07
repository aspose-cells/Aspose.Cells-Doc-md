---
title: 使用AbstractCalculationEngine返回值范围
description: 该文章介绍了通过Aspose.Cells库在Microsoft Excel中使用抽象计算引擎返回一系列值。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法来获取值范围并返回结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells，Excel，返回一系列值的抽象计算引擎
type: docs
weight: 55
url: /zh/net/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells提供了[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)类，用于实现Microsoft Excel不支持的内置函数的自定义函数。

本文将解释如何从[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)返回值范围。

{{% /alert %}}

以下代码演示了如何使用[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)类，并通过其方法返回值范围。

创建一个具有函数*CalculateCustomFunction*的类。此类实现[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

现在将上述函数用于您的程序

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
