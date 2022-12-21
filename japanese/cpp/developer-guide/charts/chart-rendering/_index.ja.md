---
title: チャートのレンダリング
type: docs
weight: 30
url: /ja/cpp/chart-rendering/
---
## **チャートの作成**

Aspose.Cells API は、トピックで詳述されているように、Excel チャートの真正性を作成することをサポートします[Excel チャートの作成とカスタマイズ](/cells/ja/cpp/creating-and-customizing-charts/)Aspose.Cells API を使用してチャートを画像および PDF 形式でレンダリングする方法を示すために、次のスニペットに従って列タイプのチャートを作成します。

{{< highlight "cpp" >}}

     // Create a new workbook

	intrusive_ptr<IWorkbook> workbook = Factory::CreateIWorkbook();

	// Get first worksheet which is created by default

	intrusive_ptr<IWorksheet> worksheet = workbook->GetIWorksheets()->GetObjectByIndex(0);

	// Adding sample values to cells

	worksheet->GetICells()->GetObjectByIndex(new String("A1"))->PutValue(50);

	worksheet->GetICells()->GetObjectByIndex(new String("A2"))->PutValue(100);

	worksheet->GetICells()->GetObjectByIndex(new String("A3"))->PutValue(150);

	worksheet->GetICells()->GetObjectByIndex(new String("B1"))->PutValue(4);

	worksheet->GetICells()->GetObjectByIndex(new String("B2"))->PutValue(20);

	worksheet->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(50);

	// Adding a chart to the worksheet

	int chartIndex = worksheet->GetICharts()->Add(Aspose::Cells::Charts::ChartType::ChartType_Column, 5, 0, 20, 8);

	// Accessing the instance of the newly added chart

	intrusive_ptr<Aspose::Cells::Charts::IChart> chart = worksheet->GetICharts()->GetObjectByIndex(chartIndex);

	// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"

	chart->GetNISeries()->Add(new String("A1:B3"), true);

{{< /highlight >}}

## **チャートのレンダリング**

Aspose.Cells API は、追加のツールやアプリケーションを必要とせずに、Excel チャートを画像や PDF 形式に変換することをサポートしています。レンダリング サポートを提供するために、Chart クラスは、アプリケーションの要件に最適なオーバーロードの真偽を使用して ToImage および ToPdf メソッドを公開しました。

### **グラフを画像にレンダリングする**

Chart.toImage メソッドには、単純なレンダリングだけでなく高度なレンダリングもサポートするための多数のオーバーロードがあります。アプリケーションの要件がチャートをデフォルトの寸法でレンダリングすることである場合、次のように Chart.toImage メソッドを使用することをお勧めします。

{{< highlight "cpp" >}}

 // Output directory path

StringPtr outDir = new String("..\\Data\\02_OutputDirectory\\");

// Path of output image file

StringPtr outputChartImage = outDir->StringAppend(new String("out1image.png"));

// Saving the chart to image file

chart->ToImage(outputChartImage, Aspose::Cells::System::Drawing::Imaging::ImageFormat::GetPng());

{{< /highlight >}}

### **グラフを PDF にレンダリング**

グラフを PDF 形式にレンダリングするために、Aspose.Cells API は、結果の PDF をディスク パスまたはストリームに保存する機能を備えた Chart.ToPdf メソッドを公開しました。

{{< highlight "cpp" >}}

 // Path of output pdf file

StringPtr outputPdfFile = outDir->StringAppend(new String("out1pdf.pdf"));

// Saving chart to PDF

chart->ToPdf(outputPdfFile);

{{< /highlight >}}

## **レンダリングでサポートされているグラフの種類**

現在、レンダリングがサポートされていないチャート タイプがいくつかあります。このようなチャート タイプには、次のものが含まれます。**N** の**下表の**列をサポート。

|**グラフの種類**|**チャートのサブタイプ**|**対応**|
|:- |:- |:- |
|**桁**|桁|**はい**|
||積み上げ列|**はい**|
||Column100PercentStacked|**はい**|
||列 3DClustered|**はい**|
||Column3D積み上げ|**はい**|
||Column3D100PercentStacked|**はい**|
||列 3D|**はい**|
|**バー**|バー|**はい**|
||棒積み上げ|**はい**|
||Bar100Percent積み上げ|**はい**|
||Bar3DClustered|**はい**|
||Bar3D積み上げ|**はい**|
||Bar3D100PercentStacked|**はい**|
|**ライン**|ライン|**はい**|
||LineStacked|**はい**|
||Line100PercentStacked|**はい**|
||LineWithDataMarkers|**はい**|
||LineStackedWithDataMarkers|**はい**|
||Line100PercentStackedWithDataMarkers|**はい**|
||Line3D|**はい**|
|**パイ**|パイ|**はい**|
||Pie3D|**はい**|
||パイパイ|**はい**|
||パイ爆発|**はい**|
||Pie3DExploded|**はい**|
||パイバー|**はい**|
|**散布**|散布|**はい**|
||ScatterConnectedByCurvesWithDataMarker|**はい**|
||ScatterConnectedByCurvesWithoutDataMarker|**はい**|
||ScatterConnectedByLinesWithDataMarker|**はい**|
||ScatterConnectedByLinesWithoutDataMarker|**はい**|
|**範囲**|範囲|**はい**|
||エリア積み上げ|**はい**|
||Area100PercentStacked|**はい**|
||エリア3D|**はい**|
||Area3D積み上げ|**はい**|
||Area3D100PercentStacked|**はい**|
|**ドーナツ**|ドーナツ|**はい**|
||ドーナツ爆発|**はい**|
|**レーダー**|レーダー|**はい**|
||RadarWithDataMarkers|**はい**|
||レーダーいっぱい|**はい**|
|**水面**|Surface3D|N|
||SurfaceWireframe3D|N|
||表面輪郭|N|
||SurfaceContourWireframe|N|
|**バブル**|バブル|**はい**|
||バブル3D|N|
|ストック|株価高低終値|**はい**|
||株式オープン高低クローズ|**はい**|
||在庫高低終値|**はい**|
||在庫量OpenHighLowClose|**はい**|
|**シリンダー**|シリンダー|**はい**|
||円柱積み上げ|**はい**|
||円柱 100%積み上げ|**はい**|
||円柱棒|**はい**|
||円柱棒積み上げ|**はい**|
||CylindricalBar100PercentStacked|**はい**|
||円筒柱 3D|**はい**|
|**円錐**|円錐|**はい**|
||円錐積み上げ|**はい**|
||円錐 100% 積み上げ|**はい**|
||円錐バー|**はい**|
||円錐棒積み上げ|**はい**|
||ConicalBar100PercentStacked|**はい**|
||ConicalColumn3D|**はい**|
|**ピラミッド**|ピラミッド|**はい**|
||ピラミッド積み上げ|**はい**|
||Pyramid100PercentStacked|**はい**|
||ピラミッドバー|**はい**|
||ピラミッド棒積み上げ|**はい**|
||PyramidBar100PercentStacked|**はい**|
||PyramidColumn3D|**はい**|
|**箱ひげ**|箱ひげ|よ|
|**漏斗**|漏斗|**はい**|
|**パレートライン**|パレートライン|**はい**|
|**サンバースト**|サンバースト|**はい**|
|**ツリーマップ**|ツリーマップ|**はい**|
|**滝**|滝|**はい**|
|**ヒストグラム**|ヒストグラム|よ|
|**地図**|地図|**な**|

{{% alert color="primary" %}}

サポートされていないチャート タイプを画像または PDF にレンダリングしようとすると、サイズが 0 の画像または空白の PDF になる可能性があります。

{{% /alert %}}
