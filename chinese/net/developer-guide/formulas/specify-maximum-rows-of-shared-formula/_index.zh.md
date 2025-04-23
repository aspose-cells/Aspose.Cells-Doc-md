---
title: 指定共享公式的最大行数
type: docs
weight: 40
url: /zh/net/specify-maximum-rows-of-shared-formula/
---

## **可能的使用场景**

共享公式的默认最大行数为64。它可以是任何数字，例如可以是1000。共享公式的性能会随着不同行数的改变而改变。因此，Aspose.Cells提供了[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula)属性，可以用于指定共享公式的最大行数。如果共享公式的总行数大于它，则共享公式将被分割为多个共享公式，如下面的截图所示。

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **指定共享公式的最大行数**

以下示例代码解释了[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula)属性的用法。它将共享公式的最大行数设置为5，并在单元格D1中添加了针对100行的共享公式，并保存到[输出Excel文件](61767856.xlsx)中。如果您提取输出Excel文件的内容并检查*sheet1.xml*，您将看到共享公式在每5行之后分割，如上述截图所示。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-SpecifyMaximumRowsOfSharedFormula.cs" >}}
{{< app/cells/assistant language="csharp" >}}
