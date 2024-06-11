---
title: 在输入新行的同时自动传播表或列表对象中的公式
type: docs
weight: 980
url: /zh/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **可能的使用场景**
有时，您希望在输入新数据时，表格或列表对象中的公式会自动传播到新行。 这是Microsoft Excel的默认行为。 为了实现与Aspose.Cells相同的功能，请使用[ListColumn.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formula)属性。
## **在输入新数据时自动传播表或列表对象中的公式**
以下示例代码以这样的方式创建一个表格或列表对象，以便在输入新数据时列B中的公式会自动传播到新行。 请检查使用此代码生成的[输出Excel文件](5472519.xlsx)。 如果在单元格A3中输入任何数字，您将看到，单元格B2中的公式会自动传播到单元格B3。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
