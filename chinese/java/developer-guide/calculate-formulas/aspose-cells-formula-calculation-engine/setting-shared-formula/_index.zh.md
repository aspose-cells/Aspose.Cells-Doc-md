---
title: 设置共享公式
type: docs
weight: 10
url: /zh/java/setting-shared-formula/
---
{{% alert color="primary" %}} 

假设您有一个工作表，其中填充的数据格式类似于以下示例工作表。

**包含一列或数据的输入文件** 

![待办事项：图片_替代_文本](setting-shared-formula_1.png)

您想要在 B2 中添加一个函数来计算第一行数据的销售税。税收是**9%**.计算销售税的公式是：**“=A2*0.09”**.本文介绍如何将此公式应用于 Aspose.Cells。

{{% /alert %}} 

 Aspose.Cells 允许您使用[Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)财产，特别是[Cell.setFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)和[Cell.getFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula).

有两个选项可用于将公式添加到列中的其他单元格（B3、B4、B5 等）。

要么做你对第一个单元格所做的，有效地为每个单元格设置公式，相应地更新单元格引用（A3*0.09，A4*0.09、A5*0.09 等）。这需要更新每一行的单元格引用。它还需要 Aspose.Cells 来单独解析每个公式，这对于大型电子表格和复杂的公式来说可能很耗时。它还添加了额外的代码行，尽管循环可以在一定程度上减少它们。

另一种方法是使用**共享公式**.使用共享公式，公式会自动更新每行中的单元格引用，以便正确计算税金。这[Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula\(java.lang.String,%20int,%20int\)方法比第一种方法更有效。

下面的例子演示了如何使用它。下面的屏幕截图显示了输出文件。

**输出文件：应用共享公式** 

![待办事项：图片_替代_文本](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
