---
title: 数据表数组公式的计算
type: docs
weight: 550
url: /zh/java/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}} 

您可以在Microsoft Excel中使用 数据 > 数据表分析 > 数据表... 创建数据表。Aspose.Cells现在允许您计算数据表的数组公式。请使用[Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\))来正常计算任何类型的公式。

{{% /alert %}} 
## **数据表数组公式的计算**
在以下示例代码中，我们使用了这个[源Excel文件](5472579.xlsx)，该文件也显示在下面的图片中。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

如果将单元格B1的值更改为100，则填充为黄色的数据表的值将变为120。示例代码将生成[输出PDF](5472577.pdf)，其中显示数据表中的值为120，如图所示。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

以下是用于从[源Excel文件](5472579.xlsx)生成[输出PDF](5472577.pdf)的示例代码。请阅读注释获取更多信息。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
