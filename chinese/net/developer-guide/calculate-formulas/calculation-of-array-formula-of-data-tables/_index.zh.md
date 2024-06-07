---
title: 数据表数组公式的计算
description: 如何使用Aspose.Cells库计算Microsoft Excel中数据表的数组公式。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法来计算数据表的数组公式并获得结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells、Excel、数据表、数组公式、计算
type: docs
weight: 70
url: /zh/net/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

您可以使用Microsoft Excel中的数据 > 数据表功能创建数据表。现在Aspose.Cells允许您计算数据表的数组公式。请使用[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)正常计算任何类型的公式。

{{% /alert %}}

在下面的示例代码中，我们使用了[源Excel文件](5115535.xlsx)。如果您将单元格B1的值更改为100，填充有黄色的数据表的值将变为120，如下图所示。示例代码生成了[输出PDF](5115538.pdf)。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

以下是用于从[源Excel文件](5115535.xlsx)生成[输出PDF](5115538.pdf)的示例代码。请阅读注释以获取更多信息。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-CalculationOfArrayFormula-CalculateArrayFormula.cs" >}}
