---
title: Show Formulas instead of Values in a Worksheet
type: docs
weight: 100
url: /java/show-formulas-instead-of-values-in-a-worksheet/
---

{{% alert color="primary" %}}

It is possible to show formulas instead of calculated values in Microsoft Excel using t*Show Formulas* option from the **Formulas** ribbon. When formulas are shown, Microsoft Excel displays formulas in the worksheet. You can achieve the same thing using Aspose.Cells.

{{% /alert %}} 

Aspose.Cells provides a [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) property. Set this to **true** to set Microsoft Excel to display formulas.

The following image shows the worksheet which has a formula in cell A3: =Sum(A1:A2).

**Worksheet with formula in cell A3**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_1.png)

The following image shows the formula instead of the calculated value, enabled by setting the [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) property to **true** with Aspose.Cells.

**Worksheet now shows formula instead of the calculated value**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
