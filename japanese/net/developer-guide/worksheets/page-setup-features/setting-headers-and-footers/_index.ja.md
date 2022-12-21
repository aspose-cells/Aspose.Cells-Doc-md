---
title: ヘッダーとフッターの設定
type: docs
weight: 30
url: /ja/net/setting-headers-and-footers/
---
{{% alert color="primary" %}}

ヘッダーとフッターは、それぞれ上マージンの下または下マージンの上に表示されるテキスト行です。ワークシートにヘッダーとフッターを追加することもできます。ヘッダーとフッターを使用して、ページ番号、著者名、トピック名、日時などの有用な情報を表示できます。ヘッダーとフッターは、ページ設定の設定を使用して管理されます。

{{% /alert %}}

## **ヘッダーとフッターの設定**

Aspose.Cells を使用すると、実行時にワークシートにヘッダーとフッターを追加できますが、印刷用にあらかじめデザインされたファイルにヘッダーとフッターを手動で設定することをお勧めします。 Microsoft Excel を GUI ツールとして使用してヘッダーとフッターを設定し、労力と開発時間を節約できます。 Aspose.Cells ファイルをインポートして設定を保存できます。

実行時にヘッダーとフッターを追加するために、Aspose.Cells は特別な API 呼び出しとスクリプト コマンドを提供して、ヘッダーとフッターをフォーマットします。

### **スクリプト コマンド**

スクリプト コマンドは、ヘッダーとフッターの書式を設定できる特別なコマンドです。

|**スクリプト コマンド**|**説明**|
|:- |:- |
|&P|現在のページ番号|
|&G|絵|
|&N|総ページ数|
|&D|現在の日付|
|&T|現在時刻|
|&A|ワークシート名|
|&F|パスなしのファイル名|
|&"\<FontName>"|フォント名を表します。例: &"Arial"|
|&"\<FontName>, \<FontStyle>"|フォント名をスタイルで表します。例: &"Arial,Bold"|
|&\<FontSize>|フォントサイズを表します。例: 「&14abc」。ただし、このコマンドの後にヘッダーに印刷されるプレーンな数字が続く場合、これはフォント サイズからスペース文字で区切られる必要があります。例: 「&14 123」。|

### **ヘッダーとフッターを設定する**

の[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラスは 2 つのメソッドを提供します。[**SetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader)と[**SetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter)、ワークシートにヘッダーとフッターを追加するために使用されます。これらのメソッドは、次の 2 つのパラメーターのみを受け取ります。

- **セクション** – ヘッダーまたはフッターを配置するセクション。左、中央、右の 3 つのセクションがあり、それぞれ 0、1、2 で表されます。
- **脚本**– ヘッダーまたはフッターに使用するスクリプト。このスクリプトには、ヘッダーまたはフッターをフォーマットするためのスクリプト コマンドが含まれています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

### **ヘッダーまたはフッターに画像を挿入する**

の[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラスには 2 つの追加メソッドがあり、[**SetHeaderPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture)と[**SetFooterPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture)、ヘッダーとフッターに画像を追加するために使用されます。これらのメソッドはパラメータを取ります:

- **セクション**– 画像が配置されるヘッダーまたはフッター セクション。左、中央、右の 3 つのセクションがあり、それぞれ値 0、1、2 で表されます。
- **バイト配列**– グラフィカル データ (バイナリ データはバイト配列のバッファに書き込む必要があります)。

以下のコードを実行してファイルを開いた後、次の方法でワークシートのヘッダーを確認します。

1. 上で**ファイル**メニュー、選択**ページ設定**.ダイアログが表示されます。
1. を選択**ヘッダー/フッター**タブ。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
