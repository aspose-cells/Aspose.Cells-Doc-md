---
title: 在键入新行的数据时，自动在表或列表对象中传播公式
type: docs
weight: 980
url: /zh/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **可能的使用场景**
有时，您希望表格或列表对象中的公式在输入新数据时会自动传播到新行。这是Microsoft Excel的默认行为。为了实现与Aspose.Cells相同的效果，请使用[ListColumn.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formula)属性。
## **在新行中输入数据时，自动在表格或列表对象中传播公式**
以下示例代码以一种使列B中的公式在输入新数据时自动传播到新行的方式创建了表格或列表对象。请检查使用此代码生成的[输出excel文件](5472519.xlsx)。如果在单元格A3中输入任何数字，您会看到单元格B2中的公式自动传播到单元格B3。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
