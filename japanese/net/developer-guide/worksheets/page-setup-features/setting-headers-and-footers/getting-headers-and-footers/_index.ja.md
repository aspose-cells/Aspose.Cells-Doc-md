---
title: ヘッダーまたはフッターの取得
type: docs
weight: 30
url: /ja/net/get-headers-or-footers/
description: この記事では、C# APIまたは.NETライブラリを使用してExcelまたはOpenOfficeファイルからプログラムでヘッダーとフッターを取得する方法について説明します。
---

{{% alert color="primary" %}}

ヘッダーとフッターは、ページレイアウトビュー、印刷プレビュー、および印刷されたページでのみ表示されます。 

複数のワークシートでヘッダーやフッターを表示する場合は、ページ設定ダイアログボックスも使用できます。 

チャートシートやチャートなどの他のシートタイプでは、ページ設定ダイアログボックスを使用してのみヘッダーやフッターを挿入できます。

{{% /alert %}}

## **MS Excelでのヘッダーとフッターの取得**
1. ヘッダーやフッターを表示または変更したいワークシートをクリックします。
2. [表示]タブの[ワークブックの表示]グループで、[ページレイアウト]をクリックします。
  Excelはワークシートをページレイアウトビューで表示します。
3. ヘッダーやフッターを表示または編集するには、ワークシートページの上（ヘッダーの下）または下（フッターの上）にある左、中央、または右のヘッダーまたはフッターテキストボックスをクリックします。


## **Aspose.Cells for .Netを使用してヘッダーとフッターを取得する**
 [**Worksheet.PageSetup.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/getheader/)と[**Worksheet.PageSetup.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/getfooter/)メソッドを使用すると、.Net開発者は簡単にファイルからヘッダーまたはフッターを取得できます。

1. ファイルを開くためのワークブックを作成します。
2. ヘッダーやフッターを取得したいワークシートを取得します。
3. 特定のセクションIDを持つヘッダーまたはフッターを取得します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}

## **ヘッダーとフッターをコマンドリストに解析する**
ヘッダーまたはフッターテキストには、ページ番号、現在の日付、またはテキストの書式設定属性のプレースホルダーなど、特別なコマンドが含まれている可能性があります。

特別なコマンドは、先頭にアンパサンド（"&"）を付けた単一の文字で表されます。

ヘッダーとフッターの文字列は、ABNF文法を使用して構築されます。これはビューアなしには理解することが難しいです。

Aspose.Cells for .Netは、ヘッダーとフッターをコマンドリストとして解析するための[**Worksheet.PageSetup.GetCommands**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/getcommands/)メソッドを提供します。

以下のコードは、ヘッダーまたはフッターをコマンドリストとして解析し、コマンドを処理する方法を示しています:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Parses-Header-Footer.cs" >}}
{{< app/cells/assistant language="csharp" >}}
