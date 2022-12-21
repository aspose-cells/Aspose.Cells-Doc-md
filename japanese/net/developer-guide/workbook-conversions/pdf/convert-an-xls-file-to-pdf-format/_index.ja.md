---
title: XLS ファイルを PDF 形式に変換する
type: docs
weight: 30
url: /ja/net/convert-an-xls-file-to-pdf-format/
---
{{% alert color="primary" %}}

PDF (Portable Document Format) は、ドキュメントの作成に使用されたソフトウェア、ハードウェア、およびオペレーティング システムとは独立したドキュメントを表します。 PDF ファイルは、デバイスや解像度に依存しない方法で、テキスト、グラフィック、画像を任意に組み合わせたドキュメントにすることができます。 PDF ファイルは圧縮されることが多いため、元のファイルよりも容量が少なくなります。

場合によっては、Microsoft Excel ファイルを PDF に変換する必要があります。そのためには、PDF ドキュメントを世界中に配布できる、高速、安全、正確、かつ信頼性の高いソリューションが必要です。このタスクを実行できる変換ツールは多数あります。ただし、元の Excel ドキュメントのレイアウトが出力 PDF ファイルに保持されていることを確認する必要があります。画像、データの書式設定、フォント、属性、色、ページ設定の設定、テキストの向き、境界線、グラフなどを正確かつ正確にレンダリングする必要があります。[Aspose.Cells](https://products.aspose.com/cells/net/)忠実度の高い変換を保証します。

このドキュメントは、Microsoft Excel ドキュメント (画像、チャート、書式設定などを含む) を PDF に変換する方法を包括的に理解できるように設計されています。そのために、Aspose.Cells API を使用して Excel ファイルを PDF に変換する簡単なコンソール アプリケーションを Visual Studio.Net で作成する方法を示します。変換は、高い精度と精度で実行されます。

{{% /alert %}}

## **Excel から PDF への変換**

この例では、Excel ファイル (SampleInput.xlsx) をテンプレートとして使用します。ワークブックには、グラフと画像を含むワークシートが含まれています。各ワークシートには、フォント、属性、色、陰影効果、境界線を使用したさまざまな種類の形式が含まれています。最初のワークシートには縦棒グラフがあり、最後のワークシートには画像があります。

### **テンプレート Excel ファイル**

テンプレート ファイルには、グラフとメディアとしての画像を含む 3 つのワークシートがあります。以下のスクリーンショットに示すように、最初のワークシートにはグラフがあり、最後のワークシートには画像があります。

|![todo:画像_代替_文章](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:画像_代替_文章](Convert_an_XLS_File_to_PDF_Sheet2.png)|
|:- |:- |
|最初のワークシート**（販売予測）**| 2 番目のワークシート**（売上報告）**|
|![todo:画像_代替_文章](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:画像_代替_文章](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| 3 番目のワークシート**（データ入力）**|最後のワークシート**（画像）**|

### **変換プロセス**

1. Aspose.Cells をダウンロードしてインストールします。
1. Aspose.Cells for .NET をダウンロードします。
 1. 開発用コンピューターにインストールします。
1. プロジェクトを作成して参照を追加します。
 1. Visual Studio.Net を起動します。
 1. 新しいコンソール アプリケーションを作成します。
1. …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll への参照を追加します。
1. プロジェクトに変換コードを追加します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、スプレッドシートを PDF にレンダリングする直前に Workbook.CalculateFormula() を呼び出すことをお勧めします。これにより、式に依存する値が再計算され、正しい値が PDF に表示されます。

{{% /alert %}}

### **結果**

上記のコードを実行すると、アプリケーション ディレクトリの Files フォルダーに PDF ファイルが作成されます。
次のスクリーンショットは、PDF ページを示しています。ヘッダーとフッターも出力 PDF ファイルに保持されることに注意してください。

|![todo:画像_代替_文章](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:画像_代替_文章](Convert_an_XLS_File_to_PDF_Converted2.png)|
|:- |:- |
|最初のワークシート**（販売予測）**| 2 番目のワークシート**（売上報告）**|
|![todo:画像_代替_文章](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:画像_代替_文章](Convert_an_XLS_File_to_PDF_Converted4.png)|
| 3 番目のワークシート**（データ入力）**|最後のワークシート**（画像）**|
