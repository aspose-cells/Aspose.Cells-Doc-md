---
title: 指定共享公式的最大行数
type: docs
weight: 40
url: /zh/net/specify-maximum-rows-of-shared-formula/
---

## **可能的使用场景**

共享公式的默认最大行数为64。它可以是任何数字，例如可以是1000。共享公式的性能会随着不同行数的变化而变化。因此，Aspose.Cells提供了[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula)属性，可用于指定共享公式的最大行数。如果共享公式的总行数大于它，共享公式将会分裂成几个共享公式，如下面的截图所示。

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **指定共享公式的最大行数**

以下示例代码解释了如何使用[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula)属性。它将共享公式的最大行数设置为5，并在单元格D1中为100行添加共享公式，并保存到输出Excel文件。如果提取输出Excel文件的内容并检查sheet1.xml，您会看到在每5行后共享公式会分裂，如上图所示。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-SpecifyMaximumRowsOfSharedFormula.cs" >}}
