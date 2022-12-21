---
title: Apache POI と Aspose.Cells を使用したズーム率
type: docs
weight: 70
url: /ja/java/zoom-factor-using-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - ズーム係数**
Microsoft Excel には、ユーザーがワークシートのズームまたは倍率を設定できる機能があります。この機能は、ユーザーがワークシートの内容を小さいビューまたは大きいビューで表示するのに役立ちます。

Aspose.Cells は、Microsoft Excel ファイルを表すクラス Workbook を提供します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを可能にする WorksheetCollection が含まれています。

ワークシートは Worksheet クラスによって表されます。 Worksheet クラスは、ワークシートを管理するための幅広いプロパティとメソッドを提供します。ワークシートのズーム倍率を設定するには、Worksheet クラスの setZoom メソッドを使用します。

**Java**

{{< highlight "java" >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - ズーム率**
Apache POI は Sheet.setZoom() メソッドでズーム機能を提供します。

**Java**

{{< highlight "java" >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)
