---
title: 设置共享公式
type: docs
weight: 10
url: /zh/java/setting-shared-formula/
---

{{% alert color="primary" %}} 

假设您有一个填充有数据的工作表，格式如下所示。

**带有一列或数据的输入文件** 

![todo:image_alt_text](setting-shared-formula_1.png)

您希望在B2中添加一个函数，用于为数据的第一行计算销售税。税率为**9%**。计算销售税的公式是：**"=A2*0.09"**。本文解释了如何使用Aspose.Cells应用此公式。

{{% /alert %}} 

Aspose.Cells 允许您使用[Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) 属性来指定公式，特别是[Cell.setFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) 和 [Cell.getFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)。

在列中向其他单元格（B3、B4、B5等）添加公式有两个选项。

也可以像第一个单元格那样处理第一个单元格，有效地为每个单元格设置公式，并相应更新单元格引用（`A3*0.09`、`A4*0.09`、`A5*0.09`等）。这需要更新每行的单元格引用。它还需要 Aspose.Cells 逐个解析每个公式，对于大型电子表格和复杂公式来说，可能很耗时。虽然循环可以把代码线减少一些，但也需添加额外的代码行。

另一种方法是使用**共享公式**。使用共享公式，可以自动更新每行中的单元格引用，以便正确计算税款。[Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula\(java.lang.String,%20int,%20int\)) 方法比第一种方法更有效。

以下示例演示了如何使用它。下面的截图显示了输出文件。

**输出文件：应用共享公式** 

![todo:image_alt_text](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
