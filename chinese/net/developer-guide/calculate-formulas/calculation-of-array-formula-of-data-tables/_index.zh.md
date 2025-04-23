---
title: 数据表的数组公式计算
description: 如何使用Aspose.Cells库为Microsoft Excel中的数据表计算数组公式。通过加载现有的Excel文件或创建一个新的Excel文件，我们可以使用Aspose.Cells提供的方法来计算数据表的数组公式并获得结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, 数据表, 数组公式, 计算
type: docs
weight: 70
url: /zh/net/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

您可以在Microsoft Excel中使用数据>数据表...来创建数据表。 Aspose.Cells现在允许您计算数据表的数组公式。请在计算任何类型的公式时使用[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)。

{{% /alert %}}

在以下示例代码中，我们使用了[source excel file](5115535.xlsx)。如果您将单元格B1的值更改为100，则填充为黄色的数据表的值将变为120，如下图所示。 示例代码生成了[output PDF](5115538.pdf)。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

以下是用于从[source excel file](5115535.xlsx)生成[output PDF](5115538.pdf)的示例代码。 请阅读注释以获取更多信息。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-CalculationOfArrayFormula-CalculateArrayFormula.cs" >}}
{{< app/cells/assistant language="csharp" >}}
