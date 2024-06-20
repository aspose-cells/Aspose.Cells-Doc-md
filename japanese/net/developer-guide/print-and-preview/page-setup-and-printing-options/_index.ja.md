---
title: ページ設定および印刷オプション
type: docs
weight: 60
url: /ja/net/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

開発者は、印刷プロセスを制御するためにページ設定と印刷設定を構成する必要があります。Aspose.Cellsではページ設定と印刷設定を制御するためのさまざまなオプションがサポートされています。

この記事では、Visual Studio.Netでコンソールアプリケーションを作成し、Aspose.Cells APIを使用してワークシートに簡単なコード行を適用してページ設定と印刷オプションを適用する方法を示します。

{{% /alert %}}

## **ページ設定および印刷設定の操作**

この例では、Microsoft Excelでワークブックを作成し、Aspose.Cellsを使用してページ設定と印刷オプションを設定しました。

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

1. Aspose.Cellsをダウンロードしてインストールします。
   1. [Aspose.Cells for .Net](https://downloads.aspose.com/cells/net) をダウンロードします。
   1. 開発コンピュータにインストールします。
      すべてのAsposeのコンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限はなく、生成された文書にウォーターマークを注入するだけです。
1. プロジェクトを作成します。
   1. Visual Studioを起動します。
   1. 新しいコンソールアプリケーションを作成します。
      この例ではC#コンソールアプリケーションを示しますが、VB.NETも使用できます。
1. 参照を追加します。
   1. この例ではAspose.Cellsを使用するため、プロジェクトにそのコンポーネントへの参照を追加します。例：
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. APIを呼び出すアプリケーションを記述します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPageSetup-1.cs" >}}

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPrintingOptions-1.cs" >}}
