---
title: Excel チャートを画像に変換する
type: docs
weight: 20
url: /ja/python-net/convert-an-excel-chart-to-image/
description: Aspose.Cells for Python via .NET API を使用して、Excel チャートを画像に変換します。
keywords: PythonでExcelチャートを画像に変換する、PythonでExcelチャートを画像にエクスポートするvia NET、PythonでExcelチャートを画像に保存する。
---

{{% alert color="primary" %}}

チャートは視覚的に魅力的であり、データの比較、パターン、トレンドをユーザーに見やすく表示するのに役立ちます。例えば、ワークシートの数列を分析するよりも、チャートを見ると一目で売上が減少しているか増加しているか、実際の売上が予測された売上と比較してどうなっているかが分かります。人々は統計情報や図情報をわかりやすく、かつ簡単に維持できるように提示するように頻繁に求められます。図が手助けします。

時々、アプリケーションやWebページでチャートが必要になることがあります。また、Word文書やPDFファイル、PowerPointプレゼンテーションなど他のアプリケーションでもチャートが必要になるかもしれません。いずれの場合も、チャートを画像としてレンダリングして他の場所でも使用できるようにします。

{{% /alert %}}

## **チャートをイメージに変換する**

ここでは、円グラフと棒グラフを画像に変換しています。

### **円グラフを画像ファイルに変換する**

まず、Microsoft Excelでパイチャートを作成し、その後、Aspose.Cells for Python via .NETを使用して画像ファイルに変換します。この例のコードは、テンプレートのMicrosoft Excelファイルのパイチャートに基づいてEMFイメージを作成します。

|**出力: 円グラフ画像**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Microsoft Excelで円グラフを作成する:
   1. Microsoft Excelで新しいワークブックを開きます。
   1. ワークシートにデータを入力します。
   1. データに基づいて円グラフを作成します。
   1. ファイルを保存します。

|**入力ファイル**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

私たちはPythonパッケージをPyPiリポジトリにホストしています。

pypiからAspose.Cells for Pythonをインストールするには、次のようにコマンドを使用してください：$ pip install aspose-cells-python。

また、開発者環境に"Aspose.Cells for Python via .NET"をインストールする手順についても、ステップバイステップの手順に従うことができます。
1. Aspose.Cells for Python via .NETをダウンロードしてインストールする：
   1. [pypi](https://pypi.org/project/aspose-cells-python/) から Aspose.Cells for Python via .NET をインストールします。コマンドは次のとおりです: $ pip install aspose-cells-python。
   1. また、「Aspose.Cells for Python via .NET」を開発者環境にインストールする手順については、[ステップバイステップの手順](https://docs.aspose.com/cells/python-net/getting-started/)に従うこともできます。

全ての[Aspose](http://www.aspose.com/)コンポーネントは、最初にインストールした際に評価モードで動作します。評価モードには時間制限はなく、出力ドキュメントに透かしを挿入するだけです。

1. プロジェクトを作成します。
   1. Visual Studioを開始します。
   1. Pythonプロジェクトにライブラリ参照（ライブラリのインポート）を追加します。
   1. チャートを見つけて変換するコードを記述します。以下にコンポーネントがこのタスクを遂行するために使用するコードが示されています。ごく少数の行のコードが使用されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingPieChartToImageFile-1.py" >}}

### **棒グラフを画像ファイルに変換する**

まずMicrosoft Excelで棒グラフを作成し、上記のように画像ファイルに変換します。サンプルコードを実行した後、テンプレートExcelファイルの棒グラフに基づいてJPEGファイルが作成されます。

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingColumnChartToImage-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
