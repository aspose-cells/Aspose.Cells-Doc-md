---
title: 数式を含む CSV ファイルの読み込みまたはインポート
type: docs
weight: 350
url: /ja/net/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

 CSV ファイルにはほとんどがテキスト データが含まれており、数式は含まれていません。ただし、CSV ファイルにも数式が含まれている場合があります。このような CSV ファイルは、[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula)なので**真実** .このプロパティが設定されると**真実**、Aspose.Cells は、数式を単純なテキストとして扱いません。これらは数式として扱われ、Aspose.Cells 数式計算エンジンは通常どおり処理します。

{{% /alert %}} 

次のコードは、数式を含む CSV ファイルを読み込んでインポートする方法を示しています。任意の CSV ファイルを使用できます。説明のために、[シンプルなcsvファイル](5115034.csv)このデータが含まれています。ご覧のとおり、式が含まれています。

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



このコードは、最初に CSV ファイルをロードし、次にセル D4 で再度インポートします。最後に、ワークブック オブジェクトを XSLX 形式で保存します。の[出力XLSXファイル](5115052.xlsx)このように見えます。ご覧のとおり、セル C3 と F4 には数式とその結果 800 が含まれています。

|![todo:画像_代替_文章](load-or-import-csv-file-with-formulas_1.png)|
|:- |

