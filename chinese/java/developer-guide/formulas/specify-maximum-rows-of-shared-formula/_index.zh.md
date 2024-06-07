---
title: 指定共享公式的最大行数
type: docs
weight: 40
url: /zh/java/specify-maximum-rows-of-shared-formula/
---

## **可能的使用场景**

共享公式的默认最大行数为64。它可以是任何数字，例如1000。共享公式的性能随不同行数的变化而变化。因此，Aspose.Cells提供了[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)属性，用于指定共享公式的最大行数。如下截图显示：如果共享公式的总行数大于它，共享公式将拆分为多个共享公式。

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **指定共享公式的最大行数**

以下示例代码解释了[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)属性的用法。将共享公式的最大行数设置为5，并将共享公式添加到单元格D1中，跨100行，并保存到[输出Excel文件](61767869.xlsx)。如果提取输出Excel文件的内容并检查*sheet1.xml*，您将看到共享公式在每5行后拆分，如上述截图中所示。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
