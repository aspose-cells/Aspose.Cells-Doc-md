---
title: 数式を含む CSV ファイルをロードまたはインポートする
type: docs
weight: 350
url: /ja/python-net/load-or-import-csv-file-with-formulas/
description: Aspose.Cells for Python via .NET API を使用して、数式を含む CSV ファイルをロードまたはインポートします。
keywords: Python Load or Import CSV file with Formulas, Convert CSV with Formulas to Excel in Python via NET, Python convert CSV with Formulas to xlsx, Load CSV with Formulas to Excel file.
---
{{% alert color="primary" %}} 

 CSV ファイルにはほとんどのテキスト データが含まれており、数式は含まれていません。ただし、CSV ファイルに数式が含まれる場合もあります。このような CSV ファイルは、[TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) *本当**として。このプロパティが *true** に設定されると、Aspose.Cells は数式を単純なテキストとして扱いません。これらは数式として扱われ、Aspose.Cells 数式計算エンジンは通常どおり処理します。

{{% /alert %}} 

次のコードは、数式を含む CSV ファイルをロードおよびインポートする方法を示しています。任意の CSV ファイルを使用できます。説明のために、以下を使用します。[単純なcsvファイル](5115034.csv)このデータが含まれています。ご覧のとおり、式が含まれています。

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



このコードは、最初に CSV ファイルをロードし、それからセル D4 に再度インポートします。最後に、ワークブック オブジェクトを XSLX 形式で保存します。の[出力XLSXファイル](5115052.xlsx)このように見えます。ご覧のとおり、セル C3 と F4 には数式とその結果 800 が含まれています。

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

