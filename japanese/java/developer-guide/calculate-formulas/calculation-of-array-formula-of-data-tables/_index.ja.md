---
title: データテーブルの配列式の計算
type: docs
weight: 550
url: /ja/java/calculation-of-array-formula-of-data-tables/
---
{{% alert color="primary" %}} 

Microsoft Excel で [データ] > [What-If 分析] > [データ テーブル...] を使用してデータ テーブルを作成できます。Aspose.Cells では、データ テーブルの配列式を計算できるようになりました。使ってください[Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) あらゆる種類の数式を計算するための通常の方法です。

{{% /alert %}} 
## **データテーブルの配列式の計算**
次のサンプル コードでは、これを使用しました。[ソースエクセルファイル](5472579.xlsx)これは次の画像にも示されています。

![todo:画像_代替_文章](calculation-of-array-formula-of-data-tables_1.png)

セル B1 の値を 100 に変更すると、黄色で塗りつぶされたデータ テーブルの値は 120 になります。サンプル コードは、[PDF出力](5472577.pdf)この画像に示すように、データ テーブルの値として 120 が表示されます。

![todo:画像_代替_文章](calculation-of-array-formula-of-data-tables_2.png)

生成に使用するサンプルコードは次のとおりです。[PDF出力](5472577.pdf)から[ソースエクセルファイル](5472579.xlsx).詳細については、コメントをお読みください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
