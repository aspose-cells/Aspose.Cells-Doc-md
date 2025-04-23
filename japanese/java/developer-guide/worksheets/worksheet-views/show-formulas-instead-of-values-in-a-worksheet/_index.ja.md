---
title: ワークシートで値ではなく数式を表示する
type: docs
weight: 100
url: /ja/java/show-formulas-instead-of-values-in-a-worksheet/
---

{{% alert color="primary" %}}

Microsoft Excelでは、**数式**リボンの**数式を表示**オプションを使用して、計算された値の代わりに数式を表示することができます。数式が表示されると、Microsoft Excelはワークシートに数式を表示します。Aspose.Cellsを使用して同じことを実現することができます。

{{% /alert %}} 

Aspose.Cellsは**[**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas)**プロパティを提供します。これを**true**に設定すると、Microsoft Excelが数式を表示するようになります。

次の画像は、セルA3に数式=Sum(A1:A2)があるワークシートを示しています。

**セルA3に数式があるワークシート**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_1.png)

次の画像は、Aspose.Cellsを使用して**[**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas)**プロパティを**true**に設定することで、計算された値の代わりに数式を表示しているワークシートを示しています。

**ワークシートには、計算値の代わりに数式が表示されています**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
{{< app/cells/assistant language="java" >}}
