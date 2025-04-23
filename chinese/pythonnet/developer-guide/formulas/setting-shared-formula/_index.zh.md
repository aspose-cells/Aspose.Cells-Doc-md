---
title: 设置共享公式
type: docs
weight: 10
url: /zh/python-net/setting-shared-formula/
---

{{% alert color="primary" %}}

 如果你想在工作表中添加一个会进行计算的函数，本文说明如何用Aspose.Cells for Python via .NET实现此功能。

{{% /alert %}}

## 使用 Aspose.Cells for Python via .NET 设置共享公式

假设您有一个填充有数据的工作表，格式如下所示的样本工作表。

|**只有一个列或数据的输入文件**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

 你想在 B2 添加一个函数，用于计算第一行数据的销售税。税率为**9%**。计算销售税的公式是：**"=A2*0.09"**。本文讲解如何使用 Aspose.Cells for Python via .NET 应用此公式。

Aspose.Cells for Python via .NET 允许你使用 [**Cell.formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula) 属性来指定公式。有两种方法可以将公式添加到列中的其他单元格（B3、B4、B5 等）中。

要么像你对第一个单元格所做的那样，为每个单元格有效地设置公式，并相应更新单元格引用（A3*0.09、A4*0.09、A5*0.09 等）。这需要更新每一行的单元格引用。还需要 Aspose.Cells for Python via .NET 单独解析每个公式，这对于大型电子表格和复杂公式来说可能耗时较长。这也会多写一些代码行，虽然循环可以在一定程度上减少这些代码。

另一种方法是使用**共享公式**。使用共享公式，公式会自动更新每行的单元格引用，使得税款可以正确计算。这种[**Cell.set_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_shared_formula) 方法比第一种方法更有效。

以下示例演示了如何使用它。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSharedFormula-1.py" >}}

