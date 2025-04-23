---
title: Apache POIとAspose.Cellsを使用したズームファクター
type: docs
weight: 70
url: /ja/java/zoom-factor-using-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - ズームファクター**
Microsoft Excelには、ユーザーがワークシートのズームまたは拡大縮小率を設定できる機能があります。この機能により、ユーザーはワークシートの内容を小さなビューまたは大きなビューで表示できます。

Aspose.Cellsには、Microsoft Excelファイルを表すWorkbookクラスを提供しています。 Workbookクラスには、Excelファイル内の各ワークシートにアクセスできるWorksheetCollectionが含まれています。

ワークシートはWorksheetクラスで表されます。 Worksheetクラスには、ワークシートのズームファクターを設定するために使用されるさまざまなプロパティとメソッドが提供されています。

**Java**

{{< highlight java >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - ズームファクター**
Apache POIは、Sheet.setZoom（）メソッドを使用してズーム機能を利用できます。

**Java**

{{< highlight java >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)
{{< app/cells/assistant language="java" >}}
