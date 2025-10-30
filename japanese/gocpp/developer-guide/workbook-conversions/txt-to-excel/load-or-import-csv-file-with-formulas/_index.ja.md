---
title: C++を使って数式を含むCSVファイルを読み込むまたはインポートする方法
linktitle: 数式を持つCSVファイルを読み込むまたはインポートする
type: docs
weight: 350
url: /ja/go-cpp/load-or-import-csv-file-with-formulas/
description: 数式を含むCSVファイルをAspose.Cellsを使用してGolang経由でC++に読み込むまたはインポートする
---

{{% alert color="primary" %}} 

CSVファイルは主にテキストデータを含み、通常は数式を含まない。ただし、CSVファイルに数式が含まれる場合もあります。その場合は、[TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/go-cpp/txtloadoptions/gethasformula/)を**true**に設定して読み込む必要があります。このプロパティを**true**に設定すると、Aspose.Cellsは数式を単純なテキストとして扱わず、数式として処理します。Aspose.Cellsの数式計算エンジンが通常どおり処理します。

{{% /alert %}} 

以下のコード例は、数式を含むCSVファイルを読み込みインポートする方法を示しています。任意のCSVファイルを使用できます。例として、[シンプルなCSVファイル](5115034.csv)を使用し、このデータが含まれています。ご覧のとおり、数式を含んでいます。

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadOrImportCsvFileWithFormulas.go" >}}
まずCSVファイルを読み込み、その後セルD4に再度インポートします。最後に、ワークブックオブジェクトをXLSX形式で保存します。[出力されるXLSXファイル](5115052.xlsx)はこのようになります。ご覧のとおり、セルC3とF4に数式が含まれており、その結果は800です。

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
