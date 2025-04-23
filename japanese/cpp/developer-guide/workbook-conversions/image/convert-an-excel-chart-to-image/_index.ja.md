---
title: Excelチャートを画像に変換するC++による方法
linktitle: Excel チャートを画像に変換する
type: docs
weight: 20
url: /ja/cpp/convert-an-excel-chart-to-image/
description: Aspose.Cellsを使用してExcelチャートを画像に変換する方法を学びます。
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
   1. [Aspose.Cells for C++をダウンロード](https://downloads.aspose.com/cells/cpp)。
   1. 開発コンピュータにインストールします。

全ての[Aspose](http://www.aspose.com/)コンポーネントは、最初にインストールした際に評価モードで動作します。評価モードには時間制限はなく、出力ドキュメントに透かしを挿入するだけです。

1. プロジェクトを作成します。
   1. C++の開発環境（例：Visual Studio）を開始します。
   1. 新しいコンソールアプリケーションを作成します。
   1. Aspose.Cellsへの参照を追加します。このプロジェクトではAspose.Cellsを使用しているため、ライブラリへの参照を追加してください。
   1. チャートを見つけて変換するコードを記述します。以下にコンポーネントがこのタスクを遂行するために使用するコードが示されています。ごく少数の行のコードが使用されます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the pie chart.
    Workbook workbook(srcDir + u"PieChart.xlsx");

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Convert the chart to an image file.
    chart.ToImage(srcDir + u"PieChart.out.emf", Aspose::Cells::Drawing::ImageType::Emf);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

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

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the column chart.
    U16String inputFilePath = srcDir + u"ColumnChart.xlsx";
    Workbook workbook(inputFilePath);

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Convert the chart to an image file.
    U16String outputImagePath = srcDir + u"ColumnChart.out.jpeg";
    chart.ToImage(outputImagePath, ImageType::Jpeg);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
