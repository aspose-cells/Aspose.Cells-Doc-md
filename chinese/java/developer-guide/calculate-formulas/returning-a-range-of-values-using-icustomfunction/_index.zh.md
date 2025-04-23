---
title: 使用ICustomFunction返回一系列值
type: docs
weight: 270
url: /zh/java/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

从 Aspose.Cells for Java 20.8 发布开始，[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) 不再推荐使用，您应使用 [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) 类。[**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) 类的使用方式在以下文章中描述。

[使用AbstractCalculationEngine返回一系列值](/cells/zh/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells提供了[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)接口，用于实现Microsoft Excel不支持的用户定义或自定义函数。

当您实现[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)接口方法时，通常需要返回单个单元格值。但有时，您需要返回一系列的值。本文将解释如何从[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)返回值的一系列值。

{{% /alert %}}

## **使用ICustomFunction返回一系列值**

以下代码实现[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)并通过其方法返回一系列值。请查看生成的代码的[Excel文件](5472922.xlsx)和[pdf](5472925.pdf)以供参考。

创建一个带有函数*CalculateCustomFunction*的类。该类实现[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

现在在您的程序中使用上述函数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
{{< app/cells/assistant language="java" >}}
