---
title: ヘッダーとフッターの設定
type: docs
weight: 30
url: /ja/net/setting-headers-and-footers/
description: この記事では、C# APIまたは.NETライブラリを使用して、スクリプトコマンドを使用してExcelワークシートのヘッダーとフッターに画像をプログラムで挿入する方法について説明します。
keywords: C# でエクセルヘッダーフッターに画像を挿入し、C# でエクセルヘッダーフッタースクリプトコマンドを設定する
---

{{% alert color="primary" %}}

ヘッダーとフッターはそれぞれ上部の余白の下に表示されるテキスト行です。ワークシートにもヘッダーやフッターを追加することができます。ヘッダーやフッターには、ページ番号、著者名、トピック名、または日付と時刻などの有用な情報を表示することができます。ヘッダーとフッターはページ設定の設定を使用して管理されます。

{{% /alert %}}

## **ヘッダーとフッタの設定**

Aspose.Cells はランタイムでワークシートにヘッダーやフッターを追加することができますが、印刷のために事前に設計されたファイルでヘッダーとフッターを手動で設定することをお勧めします。Microsoft Excel を GUI ツールとして使用して、ヘッダーやフッターを設定して手間と開発時間を節約することができます。Aspose.Cells はそのファイルをインポートして設定を保存することができます。

ヘッダーやフッターをランタイムで追加するために、Aspose.Cells は特別な API 呼び出しとスクリプトコマンドを提供しています。

### **スクリプトコマンド**

スクリプトコマンドは、ヘッダーやフッターのフォーマットを設定する特別なコマンドです。

|**スクリプトコマンド**|**説明**|
| :- | :- |
|&P|現在のページ番号
|&G|画像
|&N|ページの総数
|&D|現在の日付
|&T|現在の時刻
|&A|ワークシート名
|&F|パスを除いたファイル名
|&&Text|は &Text を表示します。例： &&WO は &WO と表示されます|
|&"\<FontName>"|フォント名を表します。例: &"Arial"
|&"\<FontName>, \<FontStyle>"|スタイル付きのフォント名を表します。例: &"Arial,Bold"
|&\<FontSize>|フォントサイズを表します。例：「&14abc」。ただし、このコマンドの後にヘッダーに印刷されるプレーンな数字が続く場合、その数字はフォントサイズとスペースで区切る必要があります。例：「&14 123」。|

### **ヘッダーやフッタの設定**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) クラスは、ワークシートにヘッダーやフッターを追加するために使用される [**SetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader) と [**SetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter) という二つのメソッドを提供します。これらのメソッドは2つのパラメーターのみを取ります。

- **Section** – ヘッダーやフッターを配置するセクション。左、中央、右の3つのセクションがあり、それぞれ0、1、2で表されます。
- **Script** – ヘッダーやフッターのために使用するスクリプト。このスクリプトにはヘッダーやフッターをフォーマットするためのスクリプトコマンドが含まれます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

### **ヘッダーやフッターに画像を挿入**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) クラスには、ヘッダーやフッターに画像を追加するために使用される [**SetHeaderPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture) と [**SetFooterPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture) という追加のメソッドがあります。これらのメソッドは以下のパラメーターを取ります。

- **Section** – 画像が配置されるヘッダーやフッターセクション。左、中央、右の3つのセクションがあり、それぞれ0、1、2で表されます。
- **バイト配列** – グラフィカルデータ（バイナリデータはバイト配列のバッファに書き込む必要があります）。

以下のコードを実行し、ファイルを開いた後、ワークシートのヘッダーを確認してください。

1. **ファイル** メニューから **ページ設定** を選択します。ダイアログが表示されます。
1. **ヘッダー/フッター** タブを選択します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
