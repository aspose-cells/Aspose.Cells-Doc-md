---
title: 数式を持つCSVファイルを読み込むまたはインポートする
type: docs
weight: 350
url: /ja/python-net/load-or-import-csv-file-with-formulas/
description: Aspose.Cells for Python via .NET APIを使用して、CSVファイルに数式を含む場合の読み込みまたはインポート
keywords: 数式付きのCSVファイルをロードまたはインポートするPython via NET、数式付きのCSVをExcelに変換する、数式付きのCSVをExcelファイルに変換する。
---

{{% alert color="primary" %}} 

CSVファイルには通常、テキストデータが含まれており、数式は含まれません。ただし、時々CSVファイルに数式が含まれていることがあります。このようなCSVファイルは、[TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/)を**true**に設定してロードする必要があります。このプロパティを**true**に設定すると、Aspose.Cellsは数式を通常のテキストではなく数式として扱います。Aspose.Cellsの数式計算エンジンが通常通り処理します。

{{% /alert %}} 

以下のコードは、数式を含むCSVファイルをロードおよびインポートする方法を示しています。任意のCSVファイルを使用できます。例として、このようなデータを含む[シンプルなcsvファイル](5115034.csv)を使用しています。

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



コードはまずCSVファイルをロードし、次にセルD4に再度インポートします。最後に、ワークブックオブジェクトをXSLX形式で保存します。[出力XLSXファイル](5115052.xlsx)は次のようになります。セルC3とF4に数式とその結果800が含まれていることがわかります。

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

{{< app/cells/assistant language="python-net" >}}
