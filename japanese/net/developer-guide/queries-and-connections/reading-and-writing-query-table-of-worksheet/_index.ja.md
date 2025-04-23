---
title: ワークシートのクエリテーブルの読み取りと書き込み
type: docs
weight: 40
url: /ja/net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cellsは、Worksheet.QueryTablesコレクションを提供し、インデックスでQueryTable型のオブジェクトを返します。以下に2つのプロパティがあります

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

これらはどちらもBoolean値です。Microsoft ExcelでData > Connections > Propertiesから表示できます。

{{% /alert %}}

ワークシートのクエリテーブルの読み書き

以下のサンプルコードは、最初のワークシートの最初のQueryTableを読み込み、そのQueryTableプロパティの両方を出力します。その後、QueryTable.PreserveFormattingをtrueに設定します。

このコードで使用される元のExcelファイルとコードによって生成された出力Excelファイルは、以下のリンクからダウンロードできます。

- [元のExcelファイル](5115533.xlsx)
- [出力Excelファイル](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

コンソール出力

上記のサンプルコードのコンソール出力は次の通りです

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

クエリテーブルの結果範囲を取得

Aspose.Cellsには、クエリテーブルの結果範囲のアドレスを読み取るオプションがあります。次のコードは、クエリテーブルの結果範囲のアドレスを読み取る機能を示しています。サンプルファイルは[こちら](72417290.xlsx)からダウンロードできます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
{{< app/cells/assistant language="csharp" >}}
