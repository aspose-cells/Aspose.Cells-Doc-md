---
title: 使用ICustomFunction返回一系列值
type: docs
weight: 270
url: /zh/java/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

自 Aspose.Cells for Java 20.8 发布以来，[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) 已被弃用。 请使用 [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) 类。 [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) 类的使用在以下文章中有说明。

[使用AbstractCalculationEngine返回一系列值](/cells/zh/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells提供了[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)接口，用于实现Microsoft Excel不支持的内置函数的自定义函数。

通常在实现[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)接口方法时，您需要返回单个单元格值。但有时候，您需要返回值范围。本文将解释如何从[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)返回值范围。

{{% /alert %}}

## **使用ICustomFunction返回一系列值**

以下代码实现了[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)，并通过其方法返回值范围。请查看生成的[输出Excel文件](5472922.xlsx)和[pdf](5472925.pdf)以供参考。

创建一个带有*CalculateCustomFunction*函数的类。这个类实现了[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

现在将上述函数用于您的程序。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
