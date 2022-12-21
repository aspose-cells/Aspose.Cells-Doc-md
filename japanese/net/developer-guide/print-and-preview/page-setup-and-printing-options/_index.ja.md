---
title: ページ設定と印刷オプション
type: docs
weight: 60
url: /ja/net/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

開発者は、印刷プロセスを制御するためにページ設定と印刷設定を構成する必要がある場合があります。ページ設定と印刷設定にはさまざまなオプションがあり、Aspose.Cells で完全にサポートされています。

この記事では、Visual Studio.Net でコンソール アプリケーションを作成し、Aspose.Cells API.

{{% /alert %}}

## **ページおよび印刷設定の操作**

この例では、Microsoft Excel でワークブックを作成し、Aspose.Cells を使用してページ設定と印刷オプションを設定しました。

### **Aspose.Cells を使用してページ設定オプションを設定する**

まず、Microsoft Excel で簡単なワークシートを作成します。次に、ページ設定オプションを適用します。コードを実行すると、下のスクリーンショットのようにページ設定オプションが変更されます。

|**出力ファイル。**|
|:- |
|![todo:画像_代替_文章](page-setup-and-printing-options_1.png)|

1. Microsoft Excel でいくつかのデータを含むワークシートを作成します。
 1. Microsoft Excel で新しいワークブックを開きます。
 1. データを追加します。
1. ページ設定オプションを設定します。
ページ設定オプションをファイルに適用します。以下は、新しいオプションが適用される前のデフォルト オプションのスクリーンショットです。

|**デフォルトのページ設定オプション。**|
|:- |
|![todo:画像_代替_文章](page-setup-and-printing-options_2.png)|

1. Aspose.Cells をダウンロードしてインストールします。
   1. [ダウンロード](https://downloads.aspose.com/cells/net) .Net の場合は Aspose.Cells。
 1. 開発用コンピューターにインストールします。
 Aspose コンポーネントはすべて、インストールすると評価モードで動作します。評価モードには時間制限がなく、生成されたドキュメントに透かしを挿入するだけです。
1. プロジェクトを作成します。
 1. Visual Studio を起動します。ネット。
 1. 新しいコンソール アプリケーションを作成します。
この例では C# コンソール アプリケーションを示していますが、VB.NET も使用できます。
1. 参照を追加します。
 1. この例では Aspose.Cells を使用しているため、そのコンポーネントへの参照をプロジェクトに追加します。例えば：
 …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. API を呼び出すアプリケーションを作成します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPageSetup-1.cs" >}}

### **印刷オプションの設定**

ページ設定には、ユーザーがワークシート ページの印刷方法を制御できるいくつかの印刷オプション (シート オプションとも呼ばれます) も用意されています。ユーザーは次のことができます。

- ワークシートの特定の印刷領域を選択します。
- タイトルを印刷します。
- グリッド線を印刷します。
- 行/列の見出しを印刷します。
- ドラフト品質を実現します。
- コメントを印刷します。
- セル エラーを出力します。
- ページの順序を定義します。

次の例では、上記の例で作成したファイル (PageSetup.xls) に印刷オプションを適用します。以下のスクリーンショットは、新しいオプションが適用される前のデフォルトの印刷オプションを示しています。

|**入力ドキュメント**|
|:- |
|![todo:画像_代替_文章](page-setup-and-printing-options_3.png)|
コードを実行すると、印刷オプションが変更されます。

|**出力ファイル**|
|:- |
|![todo:画像_代替_文章](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPrintingOptions-1.cs" >}}
