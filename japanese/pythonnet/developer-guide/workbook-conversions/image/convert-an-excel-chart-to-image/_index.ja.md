---
title: Excel グラフを画像に変換する
type: docs
weight: 20
url: /ja/python-net/convert-an-excel-chart-to-image/
description: Aspose.Cells for Python via .NET API を使用して、Excel グラフを画像に変換します。
keywords: Python Convert an Excel Chart to Image, Export an Excel Chart to Image in Python via NET, Python Save an Excel Chart to Image.
---
{{% alert color="primary" %}}

グラフは視覚的に魅力的で、ユーザーはデータの比較、パターン、傾向を簡単に確認できます。たとえば、ワークシートの数値の列を分析するのではなく、グラフを使用すると、売上が減少しているか増加しているか、または実際の売上が予測売上とどのように比較されているかが一目でわかります。統計情報やグラフ情報をわかりやすく、管理しやすい方法で提示することが求められることがよくあります。写真が役に立ちます。

場合によっては、アプリケーションや Web ページでグラフが必要になることがあります。あるいは、Word 文書、PDF ファイル、PowerPoint プレゼンテーション、またはその他のアプリケーションで必要になる場合もあります。いずれの場合も、他の場所で使用できるように、グラフを画像としてレンダリングする必要があります。

{{% /alert %}}

##  **チャートを画像に変換する**

ここの例では、円グラフと縦棒グラフが画像に変換されます。

###  **円グラフを画像ファイルに変換する**

まず、Microsoft Excel で円グラフを作成し、それを Aspose.Cells for Python via .NET の画像ファイルに変換します。この例のコードは、テンプレート Microsoft Excel ファイル内の円グラフに基づいて EMF 画像を作成します。

|**出力: 円グラフ画像**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Microsoft Excel で円グラフを作成します。
 1. Microsoft Excel で新しいワークブックを開きました。
 1. ワークシートにデータを入力します。
 1. データに基づいて円グラフを作成しました。
 1. ファイルを保存します。

|**入力ファイル。**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

Python パッケージは PyPi リポジトリでホストされています。

pypi から Aspose.Cells for Python をインストールし、次のコマンドを使用します: $ pip install aspose-cells-python。

また、「Aspose.Cells for Python via .NET」を開発者環境にインストールする方法に関する段階的な手順に従うこともできます。
1. Aspose.Cells for Python via .NET をダウンロードしてインストールします。
 1. Aspose.Cells for Python via .NET を次からインストールします。[ピピ](https://pypi.org/project/aspose-cells-python/)、コマンドを $ pip install aspose-cells-python として使用します。
 1. また、次のこともできます。[段階的な説明](https://docs.aspose.com/cells/python-net/getting-started/)「Aspose.Cells for Python via .NET」を開発者環境にインストールする方法について説明します。

全て[Aspose](http://www.aspose.com/)コンポーネントは、最初にインストールされたときは評価モードで動作します。評価モードには時間制限がなく、出力ドキュメントにウォーターマークが挿入されるだけです。

1. プロジェクトを作成します。
 1. Visual Studio を起動します。
 1. ライブラリ参照を Python プロジェクトに追加します (ライブラリをインポートします)。
 1. チャートを検索して変換するコードを作成します。以下は、タスクを実行するためにコンポーネントによって使用されるコードです。使用されるコード行はほとんどありません。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingPieChartToImageFile-1.py" >}}

###  **縦棒グラフを画像ファイルに変換する**

まず、Microsoft Excel で縦棒グラフを作成し、上記のように画像ファイルに変換します。サンプルコードを実行すると、テンプレート Excel ファイルの縦棒グラフに基づいて JPEG ファイルが作成されます。

|**出力ファイル: 縦棒グラフの画像。**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Microsoft Excel で縦棒グラフを作成します。
 1. Microsoft Excel で新しいワークブックを開きます。
 1. ワークシートにデータを入力します。
 1. データに基づいて縦棒グラフを作成します。
 1. ファイルを保存します。

|**入力ファイル。**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. 上で説明したように、参照を使用してプロジェクトをセットアップします。
1. グラフを動的に画像に変換します。以下は、タスクを実行するためにコンポーネントによって使用されるコードです。コードは前のコードと似ています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingColumnChartToImage-1.py" >}}
