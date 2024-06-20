---
title: データテーブルの配列式の計算
type: docs
weight: 550
url: /ja/java/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}} 

Microsoft Excelでデータ > シミュレーション > データテーブル...を使用してデータテーブルを作成できます。Aspose.Cellsでは、データテーブルの配列式を計算することができます。任意の種類の数式を計算するために、[Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\))を通常通り使用してください。

{{% /alert %}} 
## **データテーブルの配列式の計算**
以下のサンプルコードでは、[ソースエクセルファイル](5472579.xlsx)を使用しています。このファイルは以下の画像にも表示されています。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

セルB1の値を100に変更すると、黄色で塗られたデータテーブルの値が120になります。サンプルコードは、この画像に示されているようにデータテーブルの値が120である[出力PDF](5472577.pdf)を生成します。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

こちらは、[ソースエクセルファイル](5472579.xlsx)から[出力PDF](5472577.pdf)を生成するために使用されたサンプルコードです。詳細についてはコメントをご覧ください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
