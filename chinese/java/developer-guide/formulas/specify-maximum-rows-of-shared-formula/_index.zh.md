---
title: 指定共享公式的最大行数
type: docs
weight: 40
url: /zh/java/specify-maximum-rows-of-shared-formula/
---

## **可能的使用场景**

默认的共享公式最大行数为 64。它可以是任何数字，例如可以是 1000。共享公式的性能会随着不同行数的改变而改变。因此，Aspose.Cells 提供了 [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula) 属性，可用于指定共享公式的最大行数。如果共享公式的总行数大于它，则共享公式将被拆分为多个共享公式，如下图所示。

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **指定共享公式的最大行数**

以下示例代码解释了[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)属性的用法。它将共享公式的最大行数设置为5，并在单元格D1添加共享公式，共100行，并保存到[输出Excel文件](61767869.xlsx)。如果您提取输出的Excel文件并检查*sheet1.xml*，您将看到共享公式在每5行后拆分，如上方屏幕截图所示。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
{{< app/cells/assistant language="java" >}}
