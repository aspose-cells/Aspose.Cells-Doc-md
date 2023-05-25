---
title: Excel ワークシートのペインをフリーズする
linktitle: ペインをフリーズする
type: docs
weight: 190
url: /ja/net/how-to-freeze-panes-of-excel-worksheet
description: この記事では、.NET API の C# Library を使用してプログラムで Excel ワークシートのペインを固定する方法を説明します。
keywords: Freeze panes, Feeze window.
---
{{% alert color="primary" %}}

この記事では、ペインをフリーズする方法を学びます。
共通の見出しの下に大量のデータがある場合、ワークシートを下にスクロールしても見出しが表示されなくなります。そして、各レコードには多くのデータが含まれています。ペインをフリーズすると、残りのデータがスクロールされているときでも、そのフリーズした部分が見えるようになります。一番上の行または最初の列にあるヘッダーを簡単に確認できます。ペインの凍結および凍結解除では、データ自体は変更されず、データの表示のみが変更されます。

{{% /alert %}}

##  **Excelで**

**![Excel でペインをフリーズ](Freeze-panes.png)**


1. ペインを固定して行と列を固定したい場合は、最初にセル(B2など)を選択します。
2. 「表示」>「ペインの固定」をクリックします。
3. ドロップダウン メニューで、[ペインの固定] をクリックします。
4. 下または右にスクロールすると、最初の行と列が固定されます。

**![フォンゼンパンゲ](Frozen-Panes.png)**

ご覧のとおり、1 番目の行と列 A はフリーズされており、表示されている 2 番目の行は 32 で、表示されている 2 番目の列は D です。

ペインを固定すると、行や列のラベルを追跡せずに大規模なデータを表示できます。




##  **.Net の Aspose.Cells でペインをフリーズする**
.Net の場合、Aspose.Cells を使用してペインを固定するのは簡単です。をご利用ください。[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)選択した Cell でペインを固定するメソッド。
1. ワークブックを構築してファイルを開くか、空のファイルを作成します。
2. Worksheet.FreezePanes() メソッドを使用してペインを固定します。
3. ファイルを保存します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

添付[サンプルソース Excel ファイル](Freeze.xlsx).
