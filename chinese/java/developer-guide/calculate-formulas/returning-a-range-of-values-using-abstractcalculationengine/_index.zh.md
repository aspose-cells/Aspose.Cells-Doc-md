---
title: 使用AbstractCalculationEngine返回值范围
type: docs
weight: 275
url: /zh/java/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells提供了[**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)类，用于实现Microsoft Excel不支持的内置函数的自定义函数。

本文将解释如何从[**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)返回值范围。

{{% /alert %}}

以下代码演示了 [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) 的使用，并通过其方法返回值范围。

创建一个带有*CalculateCustomFunction*函数的类。这个类扩展了[**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

现在将上述函数用于您的程序。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ReturningRangeOfValues-1.java" >}}
