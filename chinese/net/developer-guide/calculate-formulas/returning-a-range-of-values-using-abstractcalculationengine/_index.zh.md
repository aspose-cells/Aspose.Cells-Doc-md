---
title: 使用 AbstractCalculationEngine 返回一系列值
description: 本文介绍了一个抽象计算引擎，它使用 Aspose.Cells 库返回 Microsoft Excel 中的一系列值。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法来获取一定范围的值并返回结果。最后，我们将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells, Excel, an abstract calculation engine that returns a series of values
type: docs
weight: 55
url: /zh/net/returning-a-range-of-values-using-abstractcalculationengine/
---
{{% alert color="primary" %}}

 Aspose.Cells提供[**抽象计算引擎**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)类，用于实现 Microsoft Excel 不支持的用户定义或自定义函数作为内置函数。

本文将解释如何返回值的范围[**抽象计算引擎**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{% /alert %}}

下面的代码演示了使用[**抽象计算引擎**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)类并通过其方法返回值的范围。

创建一个带有函数 *CalculateCustomFunction* 的类。这个类实现了[**抽象计算引擎**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

现在在您的程序中使用上面的函数

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
