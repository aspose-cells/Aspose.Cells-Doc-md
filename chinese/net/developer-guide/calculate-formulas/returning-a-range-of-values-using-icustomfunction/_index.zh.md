---
title: 使用ICustomFunction返回一系列值
description: 该文章描述了如何使用Aspose.Cells库在Microsoft Excel中使用ICustomFunction返回一系列值。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法来获取值范围并返回结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells自从发布Aspose.Cells for Java 20.8以来，{0}已被弃用。请使用{1}类。如何使用{2}类在以下文章中有描述。
type: docs
weight: 50
url: /zh/net/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

自 Aspose.Cells for Java 20.8 发布以来，[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) 已被弃用。 请使用 [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) 类。 [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) 类的使用在以下文章中有说明。

[使用AbstractCalculationEngine返回一系列值](/cells/zh/net/returning-a-range-of-values-using-abstractcalculationengine/)。

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells提供了[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)接口，用于实现Microsoft Excel不支持的内置函数的自定义函数。

通常在实现[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)接口方法时，您需要返回单个单元格值。但有时候，您需要返回值范围。本文将解释如何从[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)返回值范围。

{{% /alert %}}

以下代码实现[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)，并通过其方法返回值范围。

创建一个具有函数*CalculateCustomFunction*的类。此类实现[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

现在将上述函数用于您的程序

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
