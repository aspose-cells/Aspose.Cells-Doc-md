---
title: 在工作表中显示公式而不是值
type: docs
weight: 100
url: /zh/java/show-formulas-instead-of-values-in-a-worksheet/
---

{{% alert color="primary" %}}

可以在 Microsoft Excel 中使用**公式**选项卡中的*显示公式*选项来显示公式而不是计算出的值。显示公式时，Microsoft Excel 在工作表中显示公式。使用 Aspose.Cells 也可以实现相同的功能。

{{% /alert %}} 

Aspose.Cells 提供了一个 [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) 属性。将其设置为 **true** 可以设置 Microsoft Excel 显示公式。

下图显示了在单元格 A3 中有公式 =Sum(A1:A2) 的工作表。

**单元格 A3 中有公式的工作表**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_1.png)

下图显示了通过将 [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) 属性设为 **true**，启用了计算值的公式。

**工作表现在显示公式而不是计算值**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
