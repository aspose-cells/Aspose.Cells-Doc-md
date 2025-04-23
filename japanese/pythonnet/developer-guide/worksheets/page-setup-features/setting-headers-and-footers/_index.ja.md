---
title: ヘッダーとフッターの設定
type: docs
weight: 30
url: /ja/python-net/setting-headers-and-footers/
description: この記事では、Aspose.Cells for Python via .NET APIを使用して、スクリプトコマンドでヘッダーとフッターを設定することによって、Excelワークシートのヘッダーとフッターに画像をプログラム的に挿入する方法を説明します。
keywords: Python Excel ライブラリ、Python で Excel のヘッダーとフッターに画像を挿入、スクリプトコマンドを使用して Excel のヘッダーとフッターを設定する方法。
---

{{% alert color="primary" %}}

ヘッダーとフッターはそれぞれ上部の余白の下に表示されるテキスト行です。ワークシートにもヘッダーやフッターを追加することができます。ヘッダーやフッターには、ページ番号、著者名、トピック名、または日付と時刻などの有用な情報を表示することができます。ヘッダーとフッターはページ設定の設定を使用して管理されます。

{{% /alert %}}

## **ヘッダーとフッタの設定**

Aspose.Cells for Python via .NET を使用すると、実行時にワークシートにヘッダーとフッターを追加できますが、印刷のために事前にデザインされたファイルで手動で設定することをお勧めします。Microsoft ExcelをGUIツールとして使用してヘッダーとフッターを設定し、労力と開発時間を節約できます。Aspose.Cells for Python via .NET はファイルをインポートして設定を保存できます。

実行時にヘッダーとフッターを追加するには、Aspose.Cells for Python via .NET がヘッダーとフッターの書式設定に役立つ特別なAPI呼び出しとスクリプトコマンドを提供します。

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
|&"\<FontName>"|フォント名を表します。例: &"Arial"
|&"\<FontName>, \<FontStyle>"|スタイル付きのフォント名を表します。例: &"Arial,Bold"
|&\<FontSize>|フォントサイズを表します。例：「&14abc」。ただし、このコマンドの後にヘッダーに印刷されるプレーンな数字が続く場合、その数字はフォントサイズとスペースで区切る必要があります。例：「&14 123」。|

### **ヘッダーとフッターを設定する方法**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) クラスは、ワークシートにヘッダーやフッターを追加するために使用される [**set_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header/#int-str) と [**set_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer/#int-str) という二つのメソッドを提供します。これらのメソッドは2つのパラメーターのみを取ります。

- **Section** – ヘッダーやフッターを配置するセクション。左、中央、右の3つのセクションがあり、それぞれ0、1、2で表されます。
- **Script** – ヘッダーやフッターのために使用するスクリプト。このスクリプトにはヘッダーやフッターをフォーマットするためのスクリプトコマンドが含まれます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.py" >}}

### **ヘッダーまたはフッターに画像を挿入する方法**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) クラスには、ヘッダーやフッターに画像を追加するために使用される [**set_header_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header_picture/#int-bytes) と [**set_footer_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer_picture/#int-bytes) という追加のメソッドがあります。これらのメソッドは以下のパラメーターを取ります。

- **Section** – 画像が配置されるヘッダーやフッターセクション。左、中央、右の3つのセクションがあり、それぞれ0、1、2で表されます。
- **バイト配列** – グラフィカルデータ（バイナリデータはバイト配列のバッファに書き込む必要があります）。

以下のコードを実行し、ファイルを開いた後、ワークシートのヘッダーを確認してください。

1. **ファイル** メニューから **ページ設定** を選択します。ダイアログが表示されます。
1. **ヘッダー/フッター** タブを選択します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.py" >}}
