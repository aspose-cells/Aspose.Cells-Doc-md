---
title: 指定共享公式的最大行数
type: docs
weight: 40
url: /zh/java/specify-maximum-rows-of-shared-formula/
---
## **可能的使用场景**

共享公式的默认最大行数是 64。它可以是任何数字，例如它可以是 1000。共享公式的性能随着行数的不同而变化。因此，Aspose.Cells 提供了[**工作簿.设置.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)可用于指定共享公式的最大行数的属性。如果共享公式的总行数大于它，共享公式将被拆分为多个共享公式，如下面的屏幕截图所示。

![待办事项：图像_替代_文本](specify-maximum-rows-of-shared-formula_1.png)

## **指定共享公式的最大行数**

下面的示例代码解释了[**工作簿.设置.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)财产。它将共享公式的最大行数设置为 5，并在单元格 D1 中添加共享公式 100 行并保存到[输出Excel文件](61767869.xlsx).如果提取输出 Excel 文件的内容并检查*sheet1.xml*，您将看到共享公式每 5 行拆分一次，如上面的屏幕截图中突出显示的那样。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
