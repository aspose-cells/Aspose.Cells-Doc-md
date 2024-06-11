---
title: 设置共享公式
type: docs
weight: 10
url: /zh/net/setting-shared-formula/
---

{{% alert color="primary" %}}

如果您想在工作表中添加一个执行一些计算的函数。本文说明了如何使用Aspose.Cells实现此任务。

{{% /alert %}}

## 使用Aspose.Cells设置共享公式

假设您有一个填充有数据的工作表，格式如下所示的样本工作表。

|**只有一个列或数据的输入文件**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

您希望在B2中添加一个函数，用于计算第一行数据的销售税。税率为**9%**。计算销售税的公式是：**"=A2*0.09"**。本文介绍了如何使用Aspose.Cells应用此公式。

Aspose.Cells允许您使用[**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)属性指定一个公式。有两种选项可用于将公式添加到列中的其他单元格（B3、B4、B5等等）。

要么像为第一个单元格所做的那样，有效地设置每个单元格的公式，相应地更新单元格引用（A3*0.09，A4*0.09，A5*0.09等）。这需要更新每行的单元格引用。它还需要Aspose.Cells单独解析每个公式，这对于大型电子表格和复杂公式来说可能是耗时的。这还增加了额外的代码行数，尽管循环可以将其减少一些。

另一种方法是使用**共享公式**。使用共享公式，公式会自动更新每行的单元格引用，使得税款可以正确计算。这种[**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index) 方法比第一种方法更有效。

以下示例演示了如何使用它。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
