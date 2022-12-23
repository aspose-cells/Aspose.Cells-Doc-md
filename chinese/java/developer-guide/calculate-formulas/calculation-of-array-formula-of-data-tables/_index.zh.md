---
title: 数据表数组公式计算
type: docs
weight: 550
url: /zh/java/calculation-of-array-formula-of-data-tables/
---
{{% alert color="primary" %}} 

您可以在 Microsoft Excel 中使用“数据”>“假设分析”>“数据表...”创建数据表。Aspose.Cells 现在允许您计算数据表的数组公式。请用[工作簿.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) 正常计算任何类型的公式。

{{% /alert %}} 
## **数据表数组公式计算**
在下面的示例代码中，我们使用了这个[源文件](5472579.xlsx)也显示在下图中。

![待办事项：图片_替代_文本](calculation-of-array-formula-of-data-tables_1.png)

如果将B1单元格的值改为100，则用黄色填充的数据表的值将变为120。示例代码生成[输出 PDF](5472577.pdf)如图所示，它在数据表中显示 120 作为值。

![待办事项：图片_替代_文本](calculation-of-array-formula-of-data-tables_2.png)

这是用于生成的示例代码[输出 PDF](5472577.pdf)来自[源文件](5472579.xlsx).请阅读评论以获取更多信息。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
