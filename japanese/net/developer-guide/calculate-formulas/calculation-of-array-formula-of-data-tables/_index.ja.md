---
title: データテーブルの配列式の計算
type: docs
weight: 70
url: /ja/net/calculation-of-array-formula-of-data-tables/
---
{{% alert color="primary" %}}

 Microsoft Excel で、[データ] > [What-If 分析] > [データ テーブル...] を使用してデータ テーブルを作成できます。Aspose.Cells では、データ テーブルの配列式を計算できるようになりました。使ってください[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)あらゆる種類の数式を計算するための通常の方法です。

{{% /alert %}}

次のサンプル コードでは、[ソースエクセルファイル](5115535.xlsx) .セル B1 の値を 100 に変更すると、次の図に示すように、黄色で塗りつぶされたデータ テーブルの値が 120 になります。サンプル コードは、[出力 PDF](5115538.pdf).

![todo:画像_代替_文章](calculation-of-array-formula-of-data-tables_1.png)

![todo:画像_代替_文章](calculation-of-array-formula-of-data-tables_2.png)

生成に使用するサンプルコードは次のとおりです。[出力 PDF](5115538.pdf)から[ソースエクセルファイル](5115535.xlsx).詳細については、コメントをお読みください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-CalculationOfArrayFormula-CalculateArrayFormula.cs" >}}
