---
title: ワークシートで値の代わりに数式を表示する
type: docs
weight: 100
url: /ja/java/show-formulas-instead-of-values-in-a-worksheet/
---
{{% alert color="primary" %}}

を使用して Microsoft Excel で計算値の代わりに数式を表示することが可能です*数式を表示*からのオプション**数式**リボン。数式が表示されると、Microsoft Excel はワークシートに数式を表示します。 Aspose.Cells を使用して同じことを達成できます。

{{% /alert %}} 

Aspose.Cells は[**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas)財産。これを**真実**数式を表示するには、Microsoft Excel を設定します。

次の図は、セル A3 に数式が含まれているワークシートを示しています: =Sum(A1:A2)。

**セル A3 に数式を含むワークシート**

![todo:画像_代替_文章](show-formulas-instead-of-values-in-a-worksheet_1.png)

次の図は、計算値の代わりに式を示しています。[**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas)プロパティへ**真実** Aspose.Cellsで。

**ワークシートに計算値ではなく式が表示されるようになりました**

![todo:画像_代替_文章](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
