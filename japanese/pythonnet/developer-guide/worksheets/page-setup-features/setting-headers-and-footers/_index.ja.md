---
title: ヘッダーとフッターの設定
type: docs
weight: 30
url: /ja/python-net/setting-headers-and-footers/
description: この記事では、Aspose.Cells for Python via .NET APIを使用してスクリプトコマンドを設定してExcelワークシートのヘッダーとフッターに画像をプログラムで挿入する方法について説明します。
keywords: Python Excelライブラリ、Excelヘッダーフッターに画像を挿入、Pythonを使用してExcelヘッダーフッタースクリプトコマンドを設定します。
---

{{% alert color="primary" %}}

ヘッダーとフッターはそれぞれ上部の余白の下に表示されるテキスト行です。ワークシートにもヘッダーやフッターを追加することができます。ヘッダーやフッターには、ページ番号、著者名、トピック名、または日付と時刻などの有用な情報を表示することができます。ヘッダーとフッターはページ設定の設定を使用して管理されます。

{{% /alert %}}

## **ヘッダーとフッタの設定**

Aspose.Cells for Python via .NETを使用すると、ランタイムでワークシートにヘッダーとフッターを追加できますが、印刷用に事前に設計されたファイルでヘッダーとフッターを手動で設定することをお勧めします。労力と開発時間を節約するために、Microsoft ExcelをGUIツールとして使用してヘッダーとフッターを設定することができます。Aspose.Cells for Python via .NETはファイルをインポートして設定を保存できます。

ランタイムでヘッダーとフッターを追加するには、Aspose.Cells for Python via .NETは特別なAPI呼び出しとスクリプトコマンドを提供して、ヘッダーとフッターを書式設定します。

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
フォントサイズを表します。例：“&14abc”。ただし、このコマンドに続いてヘッダーに印刷するプレーンな数字がある場合、フォントサイズとは空白文字で区切られている必要があります。例：“&14 123”。

### **ヘッダーとフッターの設定方法**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) クラスは、ワークシートにヘッダーやフッターを追加するために使用される [**set_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header/#int-str) と [**set_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer/#int-str) という二つのメソッドを提供します。これらのメソッドは2つのパラメーターのみを取ります。

- **Section** – ヘッダーやフッターを配置するセクション。左、中央、右の3つのセクションがあり、それぞれ0、1、2で表されます。
- **Script** – ヘッダーやフッターのために使用するスクリプト。このスクリプトにはヘッダーやフッターをフォーマットするためのスクリプトコマンドが含まれます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.py" >}}

### **ヘッダーやフッターに画像を挿入する方法**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) クラスには、ヘッダーやフッターに画像を追加するために使用される [**set_header_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header_picture/#int-bytes) と [**set_footer_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer_picture/#int-bytes) という追加のメソッドがあります。これらのメソッドは以下のパラメーターを取ります。

- **Section** – 画像が配置されるヘッダーやフッターセクション。左、中央、右の3つのセクションがあり、それぞれ0、1、2で表されます。
- **バイト配列** – グラフィカルデータ（バイナリデータはバイト配列のバッファに書き込む必要があります）。

以下のコードを実行し、ファイルを開いた後、ワークシートのヘッダーを確認してください。

1. **ファイル** メニューから **ページ設定** を選択します。ダイアログが表示されます。
1. **ヘッダー/フッター** タブを選択します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.py" >}}
