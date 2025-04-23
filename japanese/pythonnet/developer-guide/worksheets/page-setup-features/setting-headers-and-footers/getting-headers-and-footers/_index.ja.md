---
title: ヘッダーまたはフッターの取得
type: docs
weight: 30
url: /ja/python-net/get-headers-or-footers/
description: この資料では、Aspose.Cells for Python via .NET APIを用いてExcelやOpenOfficeファイルからヘッダーおよびフッターをプログラムで取得する方法を説明します。
keywords: Python Excelライブラリ、Pythonによるヘッダーとフッターの取得、コマンドリストへのヘッダーとフッターの解析。
---

{{% alert color="primary" %}}

ヘッダーとフッターは、ページレイアウトビュー、印刷プレビュー、および印刷されたページでのみ表示されます。 

複数のワークシートでヘッダーやフッターを表示する場合は、ページ設定ダイアログボックスも使用できます。 

チャートシートやチャートなどの他のシートタイプでは、ページ設定ダイアログボックスを使用してのみヘッダーやフッターを挿入できます。

{{% /alert %}}

## **MS Excelでヘッダーとフッターを取得する方法**
1. ヘッダーやフッターを表示または変更したいワークシートをクリックします。
2. [表示]タブの[ワークブックの表示]グループで、[ページレイアウト]をクリックします。
  Excelはワークシートをページレイアウトビューで表示します。
3. ヘッダーやフッターを表示または編集するには、ワークシートページの上（ヘッダーの下）または下（フッターの上）にある左、中央、または右のヘッダーまたはフッターテキストボックスをクリックします。


## **Python ExcelライブラリAspose.Cellsを使用したヘッダーとフッターの取得方法**
 [**Worksheet.page_setup.get_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_header/#int)と[**Worksheet.page_setup.get_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_footer/#int)メソッドを使用すると、.Net開発者は簡単にファイルからヘッダーまたはフッターを取得できます。

1. ファイルを開くためのワークブックを作成します。
2. ヘッダーやフッターを取得したいワークシートを取得します。
3. 特定のセクションIDを持つヘッダーまたはフッターを取得します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Gets-Header-Footer.py" >}}

## **ヘッダーとフッターをコマンドリストに解析する方法**
ヘッダーまたはフッターテキストには、ページ番号、現在の日付、またはテキストの書式設定属性のプレースホルダーなど、特別なコマンドが含まれている可能性があります。

特別なコマンドは、先頭にアンパサンド（"&"）を付けた単一の文字で表されます。

ヘッダーとフッターの文字列は、ABNF文法を使用して構築されます。これはビューアなしには理解することが難しいです。

Aspose.Cells for Python via .NETは、ヘッダーとフッターをコマンドリストとして解析するための[**Worksheet.page_setup.get_commands**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_commands/#str)メソッドを提供します。

以下のコードは、ヘッダーまたはフッターをコマンドリストとして解析し、コマンドを処理する方法を示しています:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Parses-Header-Footer.py" >}}
