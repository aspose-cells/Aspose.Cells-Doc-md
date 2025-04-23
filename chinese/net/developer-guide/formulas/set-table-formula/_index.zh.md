---
title: 在输入新行的同时自动传播表或列表对象中的公式
linktitle: 设置Table公式
type: docs
weight: 260
url: /zh/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **可能的使用场景**
有时，您希望表或列表对象中的公式在输入新数据时自动传播到新行。这是Microsoft Excel的默认行为。为了使用Aspose.Cells实现相同的功能，请使用[ListColumn.Formula](https://reference.aspose.com/cells/net/aspose.cells.tables/listcolumn/properties/formula)属性。
## **在输入新数据时自动传播表或列表对象中的公式**
以下示例代码以一种使列B中的公式在输入新数据时自动传播到新行的方式创建了一个Table或List对象。请检查使用此代码生成的[输出Excel文件](5115469.xlsx)。如果在A3单元格中输入任何数字，您会看到，B2单元格中的公式会自动传播到B3单元格。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PropagateFormulaInTable-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
