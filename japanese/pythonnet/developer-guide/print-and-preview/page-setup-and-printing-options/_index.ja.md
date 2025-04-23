---
title: ページ設定および印刷オプション
type: docs
weight: 60
url: /ja/python-net/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

時には、印刷プロセスを制御するためにページ設定や印刷設定を構成する必要があります。ページ設定と印刷設定はさまざまなオプションを提供し、Aspose.Cells for Python via .NETで完全にサポートされています。

この資料では、Visual Studio.Netでコンソールアプリケーションを作成し、少ないコード行でAspose.Cells for Python via .NET APIを使ってページ設定や印刷オプションをワークシートに適用する方法を示します。

{{% /alert %}}

## **ページ設定および印刷設定の操作**

この例では、Microsoft Excelで作成したワークブックを用いて、Aspose.Cells for Python via .NETを使ってページ設定と印刷オプションを設定しています。

### **Aspose.Cellsを使用してページ設定オプションを設定する**

まず、Microsoft Excelで簡単なワークシートを作成します。次に、ページ設定オプションを適用します。コードを実行すると、以下のスクリーンショットのようにページ設定オプションが変更されます。

|**出力ファイル。**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. Microsoft Excelのワークシートにいくつかのデータを作成します。
   1. Microsoft Excelで新しいブックを開きます。
   1. いくつかのデータを追加します。
1. ページ設定オプションを設定します。
   ファイルにページ設定オプションを適用します。以下は、新しいオプションが適用される前のデフォルトオプションのスクリーンショットです。

|**デフォルトのページ設定オプション。**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPageSetup-1.py" >}}

### **印刷オプションの設定**

ページ設定設定には、ワークシートページの印刷方法を制御するいくつかの印刷オプション（シートオプションとも呼ばれる）も提供されます。これにより、ユーザーは次のような操作ができます。

- ワークシートの特定の印刷エリアを選択します。
- タイトルを印刷する。
- グリッド線を印刷する。
- 行/列見出しを印刷します。
- 下書き品質を実現する。
- コメントを印刷する。
- セルエラーを印刷する。
- ページ順序を定義する。

次の例では、上記の例（PageSetup.xls）で作成されたファイルに印刷オプションを適用します。以下のスクリーンショットは、新しいオプションが適用される前のデフォルトの印刷オプションを示しています。

|**入力ドキュメント**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
コードを実行すると、印刷オプションが変更されます。

|**出力ファイル**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPrintingOptions-1.py" >}}
