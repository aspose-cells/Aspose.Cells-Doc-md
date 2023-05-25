---
title: ヘッダーとフッターの設定
type: docs
weight: 30
url: /ja/net/setting-headers-and-footers/
description: この記事では、C# API または .NET ライブラリを使用してスクリプト コマンドでヘッダーとフッターを設定し、Excel ワークシートのヘッダーとフッターにプログラムで画像を挿入する方法について説明します。
keywords: insert image in excel header footer c#, set excel header footer script commands c#
---
{{% alert color="primary" %}}

ヘッダーとフッターは、それぞれ上マージンの下または下マージンの上に表示されるテキスト行です。ワークシートにヘッダーとフッターを追加することもできます。ヘッダーとフッターを使用して、ページ番号、著者名、トピック名、日付と時刻などの役立つ情報を表示できます。ヘッダーとフッターはページ設定設定を使用して管理されます。

{{% /alert %}}

##  **ヘッダーとフッターの設定**

Aspose.Cells を使用すると、実行時にワークシートにヘッダーとフッターを追加できますが、印刷用に事前に設計されたファイルにヘッダーとフッターを手動で設定することをお勧めします。 Microsoft Excel を GUI ツールとして使用してヘッダーとフッターを設定し、労力と開発時間を節約できます。 Aspose.Cells はファイルをインポートして設定を保存できます。

実行時にヘッダーとフッターを追加するために、Aspose.Cells はヘッダーとフッターをフォーマットするための特別な API 呼び出しとスクリプト コマンドを提供します。

###  **スクリプトコマンド**

スクリプト コマンドは、ヘッダーとフッターの書式を設定できる特別なコマンドです。

|**スクリプトコマンド**|**説明**|
| :- | :- |
|&P|現在のページ番号|
|&G|絵|
|&N|総ページ数|
|&D|現在の日付|
|&T|現在時刻|
|&A|ワークシート名|
|&F|パスのないファイル名|
|&"\<FontName>"|フォント名を表します。例: &"Arial"|
|&"\<FontName>, \<FontStyle>"|フォント名をスタイルで表します。例: &"Arial、太字"|
|&\<FontSize>|フォントサイズを表します。例: 「&14abc」。ただし、このコマンドの後にヘッダーに印刷される単純な数値が続く場合は、フォント サイズとスペース文字で区切る必要があります。例: 「&14 123」。|

###  **ヘッダーとフッターを設定する**

の[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラスは 2 つのメソッドを提供します。[**ヘッダーの設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader)と[**フッターを設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter)、ワークシートにヘッダーとフッターを追加するために使用されます。これらのメソッドは次の 2 つのパラメータのみを取ります。

- **セクション**– ヘッダーまたはフッターを配置するセクション。左、中央、右の 3 つのセクションがあり、それぞれ 0、1、2 で表されます。
- **脚本**– ヘッダーまたはフッターに使用されるスクリプト。このスクリプトには、ヘッダーまたはフッターをフォーマットするためのスクリプト コマンドが含まれています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

###  **ヘッダーまたはフッターに画像を挿入する**

の[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラスには 2 つの追加メソッドがあります。[**SetHeaderPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture)と[**フッター画像の設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture)、ヘッダーとフッターに画像を追加するために使用されます。これらのメソッドは次のパラメータを受け取ります。

- **セクション**– 画像が配置されるヘッダーまたはフッター セクション。左、中央、右の 3 つのセクションがあり、それぞれ値 0、1、2 で表されます。
- **バイト配列**– グラフィック データ (バイナリ データはバイト配列のバッファに書き込まれる必要があります)。

以下のコードを実行してファイルを開いた後、次の方法でワークシートのヘッダーを確認します。

1. で**ファイル**メニューで、*ページ設定**を選択します。ダイアログが表示されます。
1. を選択**ヘッダー/フッター**タブ。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
