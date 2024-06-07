---
title: 在工作表中显示公式而不是值
type: docs
weight: 100
url: /zh/java/show-formulas-instead-of-values-in-a-worksheet/
---

{{% alert color="primary" %}}

在Microsoft Excel中，可以使用**公式**选项从**公式**功能区显示公式而不是计算值。当显示公式时，Microsoft Excel会在工作表中显示公式。您可以使用Aspose.Cells实现相同的功能。

{{% /alert %}} 

Aspose.Cells提供了一个[**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas)属性。将其设置为**true**可使Microsoft Excel显示公式。

以下图像显示了单元格A3中带有公式的工作表：=Sum(A1:A2)。

**单元格A3中的公式的工作表**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_1.png)

以下图像显示了通过将[**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas)属性设置为**true**来启用而非计算值的公式。

**工作表现在显示公式而不是计算值**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
