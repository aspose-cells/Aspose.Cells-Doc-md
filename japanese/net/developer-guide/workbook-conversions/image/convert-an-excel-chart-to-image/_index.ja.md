---
title: Excel チャートを画像に変換する
type: docs
weight: 20
url: /ja/net/convert-an-excel-chart-to-image/
---
{{% alert color="primary" %}}

グラフは視覚的に魅力的であり、ユーザーはデータの比較、パターン、および傾向を簡単に確認できます。たとえば、ワークシートの数値の列を分析するのではなく、売上が増減しているかどうか、または実際の売上が予測された売上とどのように比較されているかをグラフで一目で確認できます。人々は、理解しやすく維持しやすい方法で統計情報やグラフ情報を提示するように求められることがよくあります。写真が役立ちます。

アプリケーションまたは Web ページでグラフが必要になる場合があります。または、Word 文書、PDF ファイル、PowerPoint プレゼンテーション、またはその他のアプリケーションに必要な場合があります。いずれの場合も、グラフを画像としてレンダリングして、他の場所で使用できるようにします。

{{% /alert %}}

## **チャートを画像に変換する**

ここの例では、円グラフと列の char が画像に変換されます。

### **円グラフを画像ファイルに変換する**

まず、Microsoft Excel で円グラフを作成し、それを Aspose.Cells の画像ファイルに変換します。この例のコードは、テンプレート Microsoft Excel ファイルの円グラフに基づいて EMF 画像を作成します。

|**出力: 円グラフ画像**|
|:- |
|![todo:画像_代替_文章](convert-an-excel-chart-to-image_1.png)|

1. Microsoft Excel で円グラフを作成します。
 1. Microsoft Excel で新しいワークブックを開きました。
 1. ワークシートにデータを入力します。
 1. データに基づいて円グラフを作成しました。
 1. ファイルを保存します。

|**入力ファイル。**|
|:- |
|![todo:画像_代替_文章](convert-an-excel-chart-to-image_2.png)|

1. Aspose.Cells をダウンロードしてインストールします。
   1. [ダウンロード Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. 開発用コンピューターにインストールします。

全て[Aspose](http://www.aspose.com/)コンポーネントは、最初のインストール時に評価モードで動作します。評価モードには時間制限がなく、出力ドキュメントに透かしを挿入するだけです。

1. プロジェクトを作成します。
 1. Visual Studio.Net を起動します。
 1. 新しいコンソール アプリケーションを作成します。この例では C# コンソール アプリケーションを使用していますが、VB.NET も使用できます。
 1. 参照を追加します。このプロジェクトは Aspose.Cells を使用するため、Aspose.Cells への参照を追加します。
1. チャートを見つけて変換するコードを書きます。以下は、タスクを実行するためにコンポーネントによって使用されるコードです。ごくわずかなコード行が使用されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **縦棒グラフを画像ファイルに変換する**

最初に Microsoft Excel で縦棒グラフを作成し、上記のように画像ファイルに変換します。サンプル コードを実行すると、テンプレート Excel ファイルの縦棒グラフに基づいて JPEG ファイルが作成されます。

|**出力ファイル: 縦棒グラフ イメージ。**|
|:- |
|![todo:画像_代替_文章](convert-an-excel-chart-to-image_3.png)|

1. Microsoft Excel で縦棒グラフを作成します。
 1. Microsoft Excel で新しいワークブックを開きます。
 1. ワークシートにデータを入力します。
 1. データに基づいて縦棒グラフを作成します。
 1. ファイルを保存します。

|**入力ファイル。**|
|:- |
|![todo:画像_代替_文章](convert-an-excel-chart-to-image_4.png)|

1. 上記のように、参照を使用してプロジェクトをセットアップします。
1. グラフを画像に動的に変換します。以下は、タスクを実行するためにコンポーネントによって使用されるコードです。コードは前のものと似ています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
