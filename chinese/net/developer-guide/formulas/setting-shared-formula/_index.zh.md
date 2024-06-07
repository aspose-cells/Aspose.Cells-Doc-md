---
title: 设置共享公式
type: docs
weight: 10
url: /zh/net/setting-shared-formula/
---

{{% alert color="primary" %}}

如果要在工作表中添加一个用于进行某些计算的函数。本文解释了如何使用Aspose.Cells来实现此任务。

{{% /alert %}}

## 使用Aspose.Cells设置共享公式

假设您有一个填充有数据的工作表，格式如下所示。

|**带有一列数据的输入文件**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

您希望在B2中添加一个函数，用于为数据的第一行计算销售税。税率为**9%**。计算销售税的公式是：**"=A2*0.09"**。本文解释了如何使用Aspose.Cells应用此公式。

Aspose.Cells允许您使用[**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)属性指定公式。在为该列中的其他单元格（B3、B4、B5等等）添加公式时有两个选项。

要么像为第一个单元格所做的那样，为每个单元格设置公式，随着更新单元格引用（A3*0.09, A4*0.09, A5*0.09等等）。这要求更新每行的单元格引用。它还需要Aspose.Cells逐个解析每个公式，这可能会对大型电子表格和复杂公式耗时。虽然循环可以将其减少，但也会增加额外的代码行。

另一种方法是使用**共享公式**。使用共享公式，公式会自动更新每行中的单元格引用，以便税金正确计算。与第一种方法相比，[**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index)方法更高效。

以下示例演示了如何使用它。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
