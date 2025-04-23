---
title: ワークシートのクエリテーブルの読み取りと書き込み
type: docs
weight: 40
url: /ja/python-net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET は、Worksheet.QueryTables コレクションを提供し、インデックスから QueryTable オブジェクトを返します。これには以下の2つのプロパティがあります。

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

これらはどちらもBoolean値です。Microsoft ExcelでData > Connections > Propertiesから表示できます。

{{% /alert %}}

ワークシートのクエリテーブルの読み書き

以下のサンプルコードは、最初のワークシートの最初のQueryTableを読み込み、そのQueryTableプロパティの両方を出力します。その後、QueryTable.PreserveFormattingをtrueに設定します。

このコードで使用される元のExcelファイルとコードによって生成された出力Excelファイルは、以下のリンクからダウンロードできます。

- [元のExcelファイル](5115533.xlsx)
- [出力Excelファイル](5115537.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAndWritingQueryTable.py" >}}

コンソール出力

上記のサンプルコードのコンソール出力は次の通りです

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

クエリテーブルの結果範囲を取得

Aspose.Cells for Python via .NET は、クエリテーブルの結果範囲のアドレス（結果範囲）を読み取るオプションも提供します。次のコードは、クエリテーブルの結果範囲のアドレスを読み取る例です。サンプルファイルは [こちら](72417290.xlsx) からダウンロード可能です。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAddressOfResultRange.py" >}}

