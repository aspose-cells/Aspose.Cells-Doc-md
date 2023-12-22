---
title: Excel ワークシートの先頭行を固定する
linktitle: 行の固定
type: docs
weight: 190
url: /ja/net/how-to-freeze-rows-of-excel-worksheet
description: この記事では、.NET API を含む C# Library を使用してプログラムで Excel ワークシートの先頭行を固定する方法を説明します。
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

この記事では、先頭行を固定する方法を学びます。
共通の見出しの下に大量のデータがある場合、ワークシートを下にスクロールしても見出しが表示されなくなります。先頭の行を固定すると、残りのデータがスクロールされているときでも、その固定された部分が見えるようになります。上の行のヘッダーを簡単に確認できます。

{{% /alert %}}

##  **Excel で行を固定する**

**![Excel の先頭行を固定](Freeze-Rows.png)**


1. 先頭の行を固定したい場合は、まず固定する必要がある行の下の行を選択します。
2. 「表示」>「ペインの固定」をクリックします。
3. ドロップダウン メニューで、[最上位行を固定] をクリックします。
4. 下にスクロールすると、最初の行が常に一番上のビューに表示されます。

**![フォンゼン行](Frozen-Row.png)**

ご覧のとおり、1 行目は固定されており、下にスクロールしても最初の行は常にビューの一番上に表示されます。

行をフリーズすると、行ラベルを追跡せずに大規模なデータを表示できます。




##  **.Net の Aspose.Cells で行をフリーズ**
.Net の Aspose.Cells で行を凍結するのは簡単です。
をご利用ください。[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)選択した行で行をフィーズするメソッド。
1. ワークブックを構築してファイルを開くか、空のファイルを作成します。
2. Worksheet.FreezePanes() メソッドを使用して最初の行を固定します。
3. ファイルを保存します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

添付[サンプルソース Excel ファイル](../Freeze.xlsx).
