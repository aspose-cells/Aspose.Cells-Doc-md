---
title: 在工作表中显示公式而不是值
type: docs
weight: 100
url: /zh/java/show-formulas-instead-of-values-in-a-worksheet/
---
{{% alert color="primary" %}}

可以使用 t 在 Microsoft Excel 中显示公式而不是计算值*显示公式*选项从**公式**丝带。显示公式时，Microsoft Excel 在工作表中显示公式。您可以使用 Aspose.Cells 实现相同的目的。

{{% /alert %}} 

Aspose.Cells提供了[**工作表.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas)财产。将此设置为**真的**设置Microsoft Excel显示公式。

下图显示了在单元格 A3 中具有公式的工作表：=Sum(A1:A2)。

**单元格 A3 中包含公式的工作表**

![待办事项：图像_替代_文本](show-formulas-instead-of-values-in-a-worksheet_1.png)

下图显示了公式而不是计算值，通过设置启用[**工作表.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas)财产给**真的**与 Aspose.Cells。

**工作表现在显示公式而不是计算值**

![待办事项：图像_替代_文本](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
