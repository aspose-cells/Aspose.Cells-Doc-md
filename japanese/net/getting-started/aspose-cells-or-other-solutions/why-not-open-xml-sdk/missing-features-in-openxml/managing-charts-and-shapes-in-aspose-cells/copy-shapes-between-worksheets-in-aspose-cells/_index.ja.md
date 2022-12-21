---
title: Aspose.Cells のワークシート間で図形をコピーする
type: docs
weight: 30
url: /ja/net/copy-shapes-between-worksheets-in-aspose-cells/
---
{{% alert color="primary" %}} 

画像、グラフ、その他の描画オブジェクトなど、ワークシート上の要素をワークシート間でコピーする必要がある場合があります。 Aspose.Cells はこの機能をサポートしています。チャート、画像、その他のオブジェクトを最高の精度でコピーできます。

この記事では、ワークシート間で図形をコピーする方法について詳しく説明します。たとえば、Visual Studio.Net でコンソール アプリケーションを作成し、Aspose.Cells を使用してワークシート間で画像、グラフ、その他の描画オブジェクトをコピーします。

{{% /alert %}} 

以下は、ワークシートから別のワークシートにチャートをコピーするためのコードです

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Copy Shapes between Worksheets.xlsx";

//Open the template file

Workbook workbook = new Workbook(FileName);

//Get the Chart from the "Chart" worksheet.

Aspose.Cells.Charts.Chart source = workbook.Worksheets["Chart"].Charts[0];

Aspose.Cells.Drawing.ChartShape cshape = source.ChartObject;

//Copy the Chart to the Result Worksheet

workbook.Worksheets["Result"].Shapes.AddCopy(cshape, 20, 0, 2, 0);

//Save the Worksheet

workbook.Save(FileName);



{{< /highlight >}}

**ノート：**複数の図形をコピーする方法の詳細については、訪問する必要があります[ここ](/cells/ja/net/copy-shapes-between-worksheets/)
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **実行例をダウンロード**
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
