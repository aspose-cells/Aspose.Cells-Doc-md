---
title: チャートの位置とサイズを変更する
type: docs
weight: 20
url: /ja/java/change-chart-position-and-size/
---
## **Aspose.Cells - チャートの位置とサイズの変更**
グラフの位置 (X、Y 座標) とサイズ (高さ、幅) を変更するには、Aspose.Cells を使用して次のプロパティを使用します。

1. Chart.getChartObject().get/setWidth()
1. Chart.getChartObject().get/setHeight()
1. Chart.getChartObject().get/setX()
1. Chart.getChartObject().get/setY()

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook(dataDir + "AsposeChart.xls");

Worksheet worksheet = workbook.getWorksheets().get(0);

//Load the chart from source worksheet

Chart chart = worksheet.getCharts().get(0);

//Resize the chart

chart.getChartObject().setWidth(400);

chart.getChartObject().setHeight(300);

//Reposition the chart

chart.getChartObject().setX(250);

chart.getChartObject().setY(150);

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChangeChartPositionAndSize.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[グラフの位置とサイズを変更する](/cells/ja/java/change-chart-position-and-size/).

{{% /alert %}}
