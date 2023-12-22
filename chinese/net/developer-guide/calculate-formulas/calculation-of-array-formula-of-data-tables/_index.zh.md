---
title: 数据表数组公式计算
description: 如何使用Aspose.Cells库计算Microsoft Excel中数据表的数组公式。通过加载现有的Excel文件或者新建一个Excel文件，我们可以使用Aspose.Cells提供的方法来计算数据表的数组公式并得到结果。最后，我们将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells, Excel, data tables, array formulas, calculations
type: docs
weight: 70
url: /zh/net/calculation-of-array-formula-of-data-tables/
---
{{% alert color="primary" %}}

您可以使用“数据”>“假设分析”>“数据表...”在 Microsoft Excel 中创建数据表。Aspose.Cells 现在允许您计算数据表的数组公式。请用[**工作簿.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)与计算任何类型的公式一样。

{{% /alert %}}

在下面的示例代码中，我们使用了[源 Excel 文件](5115535.xlsx)。如果将单元格 B1 的值更改为 100，则填充黄色的数据表的值将变为 120，如下图所示。示例代码生成[输出PDF](5115538.pdf).

![待办事项：图像_替代_文本](calculation-of-array-formula-of-data-tables_1.png)

![待办事项：图像_替代_文本](calculation-of-array-formula-of-data-tables_2.png)

这是用于生成的示例代码[输出PDF](5115538.pdf)来自[源 Excel 文件](5115535.xlsx)。请阅读评论以获取更多信息。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-CalculationOfArrayFormula-CalculateArrayFormula.cs" >}}
