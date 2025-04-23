---
title: 指定共享公式的最大行数
type: docs
weight: 40
url: /zh/python-net/specify-maximum-rows-of-shared-formula/
---

## **可能的使用场景**

共享公式的默认最大行数为64。它可以是任何数字，例如可以设为1000。共享公式的性能会随着行数的不同而变化。因此，Aspose.Cells for Python via .NET 提供了 [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula) 属性，可以用来指定共享公式的最大行数。如果共享公式的总行数超过此值，共享公式将被拆分成多个共享公式，如下图所示。

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **指定共享公式的最大行数**

以下示例代码解释了[**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula)属性的用法。它将共享公式的最大行数设置为5，并在单元格D1中添加了针对100行的共享公式，并保存到[输出Excel文件](61767856.xlsx)中。如果您提取输出Excel文件的内容并检查*sheet1.xml*，您将看到共享公式在每5行之后分割，如上述截图所示。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SpecifyMaximumRowsOfSharedFormula.py" >}}

