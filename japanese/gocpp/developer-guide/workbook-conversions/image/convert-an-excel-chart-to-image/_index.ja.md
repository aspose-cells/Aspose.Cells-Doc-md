---
title: Excelチャートを画像に変換(C++) via Golang
linktitle: Excel チャートを画像に変換する
type: docs
weight: 20
url: /ja/go-cpp/convert-an-excel-chart-to-image/
description: Aspose.Cellsを使用してExcelチャートを画像に変換する方法をGolange経由で学びます。
---

{{% alert color="primary" %}}

チャートは視覚的に魅力的で、データの比較、パターン、傾向を簡単に把握できるため便利です。例えば、ワークシートの列を分析する代わりに、チャートは売上の増減や予測売上との比較を一目で示します。多くの人は統計的およびグラフィカルな情報をわかりやすく維持しやすい形で提示することを求められます。画像はその助けとなります。

時には、アプリケーションやウェブページにチャートが必要になることがあります。または、それらがWordドキュメント、PDF、PowerPoint、または他のアプリケーション向けに必要になることもあります。各ケースで、チャートを画像としてレンダリングし、他所で使用できるようにしたいです。

{{% /alert %}}

## **チャートをイメージに変換する**

ここでは、円グラフと棒グラフを画像に変換しています。

### **円グラフを画像ファイルに変換する**

まず、Microsoft Excelで円グラフを作成し、その後Aspose.Cellsで画像ファイルに変換します。この例のコードは、テンプレートとなるMicrosoft Excelファイルの円グラフに基づいてEMF画像を作成します。

|**出力: 円グラフ画像**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Microsoft Excelで円グラフを作成:
   1. Microsoft Excelで新しいブックを開きます。
   1. ワークシートにデータを入力します。
   1. データに基づいて円グラフを作成します。
   1. ファイルを保存します。

|**入力ファイル**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Aspose.Cellsをダウンロードしてインストールします。
   1. [Aspose.Cells for C++をダウンロード](https://downloads.aspose.com/cells/go-cpp/)。
   1. 開発コンピュータにインストールします。

全ての[Aspose](http://www.aspose.com/)コンポーネントは、最初にインストールした際に評価モードで動作します。評価モードには時間制限はなく、出力ドキュメントに透かしを挿入するだけです。

1. プロジェクトを作成します。
   1. C++の開発環境（例：Visual Studio）を開始します。
   1. 新しいコンソールアプリケーションを作成します。
   1. Aspose.Cellsへの参照を追加します。このプロジェクトではAspose.Cellsを使用しているため、ライブラリへの参照を追加してください。
   1. チャートを見つけて変換するコードを記述します。以下にコンポーネントがこのタスクを遂行するために使用するコードが示されています。ごく少数の行のコードが使用されます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertAnExcelChartToImage.go" >}}
### **棒グラフを画像ファイルに変換する**

まず、Microsoft Excelで縦棒グラフを作成し、それを画像ファイルに変換します。サンプルコードを実行した後、テンプレートExcelファイルの縦棒グラフに基づいてJPEGファイルが作成されます。

|**出力ファイル: 棒グラフ画像**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Microsoft Excelで棒グラフを作成します:
   1. Microsoft Excelで新しいブックを開きます。
   1. ワークシートにデータを入力します。
   1. データに基づいて棒グラフを作成します。
   1. ファイルを保存します。

|**入力ファイル**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. 上記のように説明した参照を含むプロジェクトを設定します。
1. チャートを動的に画像に変換します。以下にコンポーネントがこのタスクを遂行するために使用するコードが示されています。このコードは前述のものと似ています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertAnExcelChartToImage-1.go" >}}
