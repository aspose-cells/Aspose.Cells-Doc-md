---
title: Excel ワークシートの最初の列を固定する
linktitle: 列の固定
type: docs
weight: 190
url: /ja/net/how-to-freeze-columns-of-excel-worksheet
description: この記事では、.NET API の C# Library を使用してプログラムで Excel ワークシートの左側の列を固定する方法を説明します。
keywords: Freeze left columns, Feeze first columns, Lock the column(s)
---
{{% alert color="primary" %}}

この記事では、左側の列を固定する方法を学びます。
行に大量のデータがあり、ワークシートを水平方向に下にスクロールすると左側の列が表示されない場合。最初の列をフリーズしてロックすると、残りのデータがスクロールされているときでも、そのフリーズされた部分を確認できるようになります。左側の列のヘッダーを簡単に確認できます。

{{% /alert %}}

##  **Excel の列を固定する**

**![Excel の左列を固定](freeze-columns.png)**


1. 左側の列を固定したい場合は、まず固定する必要がある列の下の列を選択します。
2. 「表示」>「ペインの固定」をクリックします。
3. ドロップダウン メニューで、[最初の列を固定] をクリックします。
4. 下にスクロールすると、最初の列が常に左側のビューに表示されます。

**![フォンゼン列](frozen-columns.png)**

ご覧のとおり、最初の列が固定されており、水平方向にスクロールすると、最初の列は常にビューの上部でロックされます。

列を固定すると、最初の列を追跡せずに長いデータを表示できます。




##  **.Net の Aspose.Cells で列をフリーズ**
.Net の場合、最初の列を Aspose.Cells で固定するのは簡単です。
をご利用ください。[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)選択した列で列をフィーズするメソッド。
1. ワークブックを構築してファイルを開くか、空のファイルを作成します。
2. Worksheet.FreezePanes() メソッドを使用して最初の列を固定します。
3. ファイルを保存します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

添付[サンプルソース Excel ファイル](Freeze.xlsx).
