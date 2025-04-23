---
title: 数式を持つCSVファイルを読み込むまたはインポートする
type: docs
weight: 350
url: /ja/net/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

CSVファイルには主にテキストデータが含まれ、数式は含まれていません。ただし、CSVファイルに数式が含まれることがあります。そのようなCSVファイルは、[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula)を**true**に設定して読み込む必要があります。このプロパティを**true**に設定すると、Aspose.Cellsは数式を単純なテキストとしてではなく、数式として扱い、通常通りAspose.Cellsの数式計算エンジンが処理します。

{{% /alert %}} 

以下のコードは、数式を含むCSVファイルをロードおよびインポートする方法を示しています。任意のCSVファイルを使用できます。例として、このようなデータを含む[シンプルなcsvファイル](5115034.csv)を使用しています。

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



コードはまずCSVファイルをロードし、次にセルD4に再度インポートします。最後に、ワークブックオブジェクトをXSLX形式で保存します。[出力XLSXファイル](5115052.xlsx)は次のようになります。セルC3とF4に数式とその結果800が含まれていることがわかります。

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

{{< app/cells/assistant language="csharp" >}}
