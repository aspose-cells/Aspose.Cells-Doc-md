---
title: ヘッダーまたはフッターの取得
type: docs
weight: 30
url: /ja/net/get-headers-or-footers/
description: この記事では、C# API または .NET ライブラリを使用して、Excel または OpenOffice ファイルからヘッダーとフッターをプログラムで取得する方法について説明します。
---
{{% alert color="primary" %}}

ヘッダーとフッターは、ページ レイアウト ビュー、印刷プレビュー、および印刷ページにのみ表示されます。

一度に複数のワークシートのヘッダーまたはフッターを表示する場合は、[ページ設定] ダイアログ ボックスを使用することもできます。

グラフ シートやグラフなどの他のシート タイプの場合は、[ページ設定] ダイアログ ボックスを使用しないとヘッダーとフッターを挿入できません。

{{% /alert %}}

##  **MS Excelでヘッダーとフッターを取得する**
1. ヘッダーまたはフッターを表示または変更するワークシートをクリックします。
2. [Vie] タブの [ワークブック ビュー] グループで、[ページ レイアウト] をクリックします。
Excel では、ワークシートがページ レイアウト ビューで表示されます。
3. ヘッダーまたはフッターを表示または編集するには、ワークシート ページの上部または下部 (ヘッダーの下、またはフッターの上) の左、中央、または右のヘッダーまたはフッター テキスト ボックスをクリックします。


##  **.Net の Aspose.Cells を使用してヘッダーとフッターを取得する**
と[**Worksheet.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetHeader/)そして[**Worksheet.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFooter/)メソッドを使用すると、.Net 開発者はファイルからヘッダーまたはフッターを簡単に取得できます。

1. ファイルを開くためのワークブックを構築します。
2. ヘッダーまたはフッターを取得するワークシートを取得します。
3. 特定のセクション ID を持つヘッダーまたはフッターを取得します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}

##  **ヘッダーとフッターをコマンド リストに解析します**
ヘッダーまたはフッターのテキストには、ページ番号、現在の日付、またはテキストの書式設定属性のプレースホルダーなどの特別なコマンドを含めることができます。

特殊コマンドは、先頭にアンパサンド (「&」) を付けた 1 つの文字で表されます。

ヘッダーとフッターの文字列は、ABNF 文法を使用して構築されます。ビューアなしでは理解するのは簡単ではありません。

 .Net の場合は Aspose.Cells[**Worksheet.GetCommands**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetCommands/)ヘッダーとフッターをコマンド リストとして解析するメソッド。

次のコードは、ヘッダーまたはフッターをコマンド リストとして解析し、コマンドを処理する方法を示します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Parses-Header-Footer.cs" >}}
