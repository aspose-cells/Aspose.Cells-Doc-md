---
title: 在新行中输入数据时自动在表或列表对象中传播公式
type: docs
weight: 980
url: /zh/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---
## **可能的使用场景**
有时，您希望表或列表对象中的公式在输入新数据时自动传播到新行。这是 Microsoft Excel 的默认行为。为了实现与 Aspose.Cells 相同的功能，请使用[列表列.公式](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formula)财产。
## **在新行中输入数据时自动在表或列表对象中传播公式**
以下示例代码创建一个表或列表对象，这样当您输入新数据时，B 列中的公式将自动传播到新行。请检查[输出excel文件](5472519.xlsx)使用此代码生成。如果您在单元格 A3 中输入任何数字，您将看到，单元格 B2 中的公式会自动传播到单元格 B3。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
