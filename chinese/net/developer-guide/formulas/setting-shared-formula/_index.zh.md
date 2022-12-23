---
title: 设置共享公式
type: docs
weight: 10
url: /zh/net/setting-shared-formula/
---
{{% alert color="primary" %}}

如果你想在工作表中添加一个函数来做一些计算。本文介绍如何使用 Aspose.Cells 完成此任务。

{{% /alert %}}

## 使用 Aspose.Cells 设置共享公式

假设您有一个工作表，其中填充的数据格式类似于以下示例工作表。

|**包含一列或数据的输入文件**|
|:- |
|![待办事项：图片_替代_文本](setting-shared-formula_1.png)|

您想要在 B2 中添加一个函数来计算第一行数据的销售税。税收是**9%**.计算销售税的公式是：**“=A2*0.09”**.本文介绍如何将此公式应用于 Aspose.Cells。

 Aspose.Cells 允许您使用[**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)财产。有两个选项可用于将公式添加到列中的其他单元格（B3、B4、B5 等）。

要么做你对第一个单元格所做的，有效地为每个单元格设置公式，相应地更新单元格引用（A3*0.09，A4*0.09、A5*0.09 等）。这需要更新每一行的单元格引用。它还需要 Aspose.Cells 来单独解析每个公式，这对于大型电子表格和复杂的公式来说可能很耗时。它还添加了额外的代码行，尽管循环可以在一定程度上减少它们。

另一种方法是使用**共享公式**.使用共享公式，公式会自动更新每行中的单元格引用，以便正确计算税金。这[**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index)方法比第一种方法更有效。

下面的例子演示了如何使用它。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
