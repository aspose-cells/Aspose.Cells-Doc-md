---
title: 在键入新行的数据时，自动在表或列表对象中传播公式
linktitle: 设置表格公式
type: docs
weight: 260
url: /zh/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **可能的使用场景**
有时，您希望在输入新数据时，表或列表对象中的公式自动传播到新行。这是 Microsoft Excel 的默认行为。为了实现与 Aspose.Cells 相同的功能，请使用[ListColumn.Formula](https://reference.aspose.com/cells/net/aspose.cells.tables/listcolumn/properties/formula) 属性。
## **在新行中输入数据时，自动在表格或列表对象中传播公式**
以下示例代码创建一个表格或列表对象，使得列B中的公式在输入新数据时会自动传播到新行。请查看使用此代码生成的输出Excel文件。如果在单元格A3中输入任何数字，您会看到单元格B2中的公式会自动传播到单元格B3。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PropagateFormulaInTable-1.cs" >}}
