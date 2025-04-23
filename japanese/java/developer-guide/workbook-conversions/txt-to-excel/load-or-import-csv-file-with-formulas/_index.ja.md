---
title: 数式を持つCSVファイルを読み込むまたはインポートする
type: docs
weight: 500
url: /ja/java/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

CSVファイルにはほとんどテキストデータしか含まれず、数式は含まれません。 ただし、時々CSVファイルに数式が含まれることがあります。 そのようなCSVファイルは、[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula)を**true**に設定してロードする必要があります。 このプロパティが**true**に設定されると、Aspose.Cellsは数式を単なるテキストとして扱いません。 それらは数式として扱われ、Aspose.Cellsの数式計算エンジンが通常どおり処理します。

{{% /alert %}} 
## **数式を持つCSVファイルを読み込むまたはインポートする**
次のコードは、数式を含むCSVファイルを読み込みおよびインポートする方法を示しています。 任意のCSVファイルを使用できます。 説明のために、[simple csv file](5472505.csv)を使用しており、このデータが含まれています。 数式が含まれていることがわかります。

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

コードはまずCSVファイルをロードし、次にセルD4に再インポートします。 最後に、ワークブックオブジェクトをXSLX形式で保存します。 [出力XLSXファイル](5472503.xlsx)は次のようになります。 セルC3とF4には数式が含まれ、その結果が800であることがわかります。

![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
{{< app/cells/assistant language="java" >}}
