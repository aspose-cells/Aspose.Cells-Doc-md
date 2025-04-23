---
title: Aspose.Cells でワークシート間でシェイプをコピーする
type: docs
weight: 30
url: /ja/net/copy-shapes-between-worksheets-in-aspose-cells/
---

{{% alert color="primary" %}} 

時々、ワークシート間で要素をコピーする必要があります。例えば、図やチャート、その他の描画オブジェクトなどです。Aspose.Cells はこの機能をサポートしています。チャート、画像、および他のオブジェクトを、最高の精度でコピーすることができます。

この記事では、ワークシート間でシェイプをコピーする方法について詳しく説明します。たとえば、Visual Studio.Net でコンソールアプリケーションを作成し、Aspose.Cells を使用してワークシート間で画像やチャートなどの描画オブジェクトをコピーします。

{{% /alert %}} 

ワークシートから別のワークシートにチャートをコピーするコードは以下の通りです

**C#**

{{< highlight csharp >}}

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

**注記:** 複数のシェイプをコピーする詳細については[こちら](/cells/ja/net/copy-shapes-between-worksheets/)をご覧ください
## **サンプルコードをダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **実行例のダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
