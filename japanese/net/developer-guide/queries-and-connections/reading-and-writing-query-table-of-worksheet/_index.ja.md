---
title: ワークシートのクエリ テーブルの読み取りと書き込み
type: docs
weight: 40
url: /ja/net/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells は、インデックスによってタイプ QueryTable のオブジェクトを返す Worksheet.QueryTables コレクションを提供します。次の 2 つのプロパティがあります。

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

これらは両方ともブール値です。それらは、[データ] > [接続] > [プロパティ] を使用して Microsoft Excel で表示できます。

{{% /alert %}}

## ワークシートのクエリ テーブルの読み取りと書き込み

次のサンプル コードは、最初のワークシートの最初の QueryTable を読み取り、両方の QueryTable プロパティを出力します。次に、QueryTable.PreserveFormatting を true に設定します。

このコードで使用されているソース Excel ファイルと、コードによって生成された出力 Excel ファイルは、次のリンクからダウンロードできます。

- [ソース Excel ファイル](5115533.xlsx)
- [出力 Excel ファイル](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### コンソール出力

上記のサンプル コードのコンソール出力は次のとおりです。

{{< highlight "java" >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## クエリ テーブルの結果範囲を取得する

 Aspose.Cells は、アドレス、つまりクエリ テーブルのセルの結果範囲を読み取るオプションを提供します。次のコードは、クエリ テーブルの結果範囲のアドレスを読み取ることにより、この機能を示しています。サンプルファイルをダウンロードできます[ここ](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
