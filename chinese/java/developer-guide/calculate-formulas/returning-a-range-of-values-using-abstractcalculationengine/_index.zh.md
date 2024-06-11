---
title: 使用AbstractCalculationEngine返回一系列值
type: docs
weight: 275
url: /zh/java/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells提供[**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)类，用于实现Microsoft Excel不支持的用户定义或自定义函数。

本文将解释如何从[**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)返回值范围。

{{% /alert %}}

以下代码演示了使用[**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)的用法，并通过其方法返回值范围。

创建一个带有函数*CalculateCustomFunction*的类。此类扩展[**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

现在在您的程序中使用上述函数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ReturningRangeOfValues-1.java" >}}
