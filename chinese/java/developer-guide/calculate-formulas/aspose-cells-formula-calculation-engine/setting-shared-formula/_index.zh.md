---
title: 设置共享公式
type: docs
weight: 10
url: /zh/java/setting-shared-formula/
---

{{% alert color="primary" %}} 

假设您有一个填充有数据的工作表，格式如下所示的样本工作表。

**带有一列或数据的输入文件** 

![todo:image_alt_text](setting-shared-formula_1.png)

您希望在B2中添加一个函数，用于计算第一行数据的销售税。税率为**9%**。计算销售税的公式是：**"=A2*0.09"**。本文介绍了如何使用Aspose.Cells应用此公式。

{{% /alert %}} 

Aspose.Cells允许您使用[Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)属性来指定公式，具体来说是 [Cell.setFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)和 [Cell.getFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)。

有两种选项可将公式添加到列中的其他单元格(B3、B4、B5等)。 

可以采取为第一个单元格所做的操作，有效地为每个单元格设置公式，相应地更新单元引用（`A3*0.09`、`A4*0.09`、`A5*0.09`等）。这需要更新每行的单元引用。它还需要Aspose.Cells逐个解析每个公式，对于大型电子表格和复杂公式来说可能耗时。尽管循环可以压缩额外的代码行，但这也会增加额外的代码行。

另一种方法是使用**共享公式**。共享公式会自动为每一行的单元格引用更新公式，确保税额计算正确。比起第一种方法，`Cell.setSharedFormula`方法更高效。

以下示例演示了如何使用它。下面的屏幕截图显示了输出文件。

**输出文件：应用共享公式** 

![todo:image_alt_text](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
{{< app/cells/assistant language="java" >}}
