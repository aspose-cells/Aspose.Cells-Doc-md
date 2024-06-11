---
title: 数据表的数组公式计算
type: docs
weight: 550
url: /zh/java/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}} 

您可以使用数据 > 此后数据 > 数据表...在Microsoft Excel中创建数据表。Aspose.Cells现在允许您计算数据表的数组公式。请使用[Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\))正常计算任何类型的公式。

{{% /alert %}} 
## **计算数据表的数组公式**
在下面的示例代码中，我们使用了这个[源Excel文件](5472579.xlsx)，它也显示在下面的图像中。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

如果修改单元格B1的值为100，则黄色填充的数据表中的值将变为120。示例代码生成了[输出PDF](5472577.pdf)，其中显示了数据表中的值为120，如下图所示。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

这是用于从[源Excel文件](5472579.xlsx)生成[输出PDF](5472577.pdf)的示例代码。有关更多信息，请阅读注释。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
