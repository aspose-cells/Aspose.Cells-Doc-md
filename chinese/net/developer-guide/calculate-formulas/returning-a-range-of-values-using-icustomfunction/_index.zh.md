---
title: 使用ICustomFunction返回一系列值
description: 本文描述了如何在Microsoft Excel中使用Aspose.Cells库和ICustomFunction来返回一系列值。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法获取一系列值并返回结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, ICustomFunction, 返回一系列值
type: docs
weight: 50
url: /zh/net/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

从 Aspose.Cells for Java 20.8 发布开始，[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) 不再推荐使用，您应使用 [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) 类。[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) 类的使用方式在以下文章中描述。

[使用AbstractCalculationEngine返回一系列值](/cells/zh/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells提供了[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)接口，用于实现Microsoft Excel不支持的用户定义或自定义函数。

当您实现[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)接口方法时，通常需要返回单个单元格值。但有时，您需要返回一系列的值。本文将解释如何从[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)返回值的一系列值。

{{% /alert %}}

以下代码实现[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)，并通过其方法返回一系列值。

创建一个带有函数 *CalculateCustomFunction* 的类。该类实现了 [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

现在将以上函数用于您的程序

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
