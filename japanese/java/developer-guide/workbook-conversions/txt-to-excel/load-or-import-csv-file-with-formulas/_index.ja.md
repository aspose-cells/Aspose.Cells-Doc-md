---
title: 数式を含む CSV ファイルのロードまたはインポート
type: docs
weight: 500
url: /ja/java/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

CSV ファイルにはほとんどがテキスト データが含まれており、数式は含まれていません。ただし、CSV ファイルにも数式が含まれている場合があります。このような CSV ファイルは、[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula)に**真実** .このプロパティが設定されると、**真実**、Aspose.Cells は、数式を単純なテキストとして扱いません。これらは数式として扱われ、Aspose.Cells 数式計算エンジンは通常どおり処理します。

{{% /alert %}} 
## **数式を含む CSV ファイルのロードまたはインポート**
次のコードは、式を含む CSV ファイルをロードおよびインポートする方法を示しています。任意の CSV ファイルを使用できます。説明のために、[シンプルなcsvファイル](5472505.csv)このデータが含まれています。ご覧のとおり、式が含まれています。

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

このコードは、最初に CSV ファイルをロードしてから、セル D4 に再度インポートします。最後に、ワークブック オブジェクトを XSLX 形式で保存します。の[出力 XLSX ファイル](5472503.xlsx)このように見えます。ご覧のとおり、セル C3 と F4 には数式とその結果 800 が含まれています。

![todo:画像_代替_文章](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
