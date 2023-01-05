---
title: xlsx4j'de Özet Grafikler Oluşturun
type: docs
weight: 30
url: /tr/java/create-pivot-charts-in-xlsx4j/
---
## **Aspose.Cells - Pivot Grafikler Oluştur**
Pivot tablo, kayıtların etkileşimli bir özetidir. Örneğin, bir çalışma sayfasındaki bir listede yüzlerce fatura girişiniz olabilir. Bir pivot tablo, faturaları müşteriye, ürüne veya tarihe göre toplayabilir. Microsoft Excel ile, düğmeleri yeni bir konuma sürükleyerek pivot tablodaki bilgileri hızlı bir şekilde yeniden düzenlemek mümkündür.
Pivot grafik, pivot tablodaki verilerin etkileşimli bir grafik temsilidir. Pivot grafikler Excel 2000'de kullanılmaya başlandı. Pivot tablo otomatik olarak ara toplamlar ve toplamlar oluşturduğundan, pivot grafik kullanmak verilerin anlaşılmasını daha da kolaylaştırır.

Aspose.Cells pivot tabloları ve pivot çizelgeleri destekler.

**Java**

{{< highlight "java" >}}

 // Instantiating an Workbook object

Workbook workbook = new Workbook(dataDir + "AsposePivotTable.xls");

// Adding a new sheet

int sheetIndex = workbook.getWorksheets().add(SheetType.CHART);

Worksheet sheet3 = workbook.getWorksheets().get(sheetIndex);

// Naming the sheet

sheet3.setName("PivotChart");

// Adding a column chart

int chartIndex = sheet3.getCharts().add(ChartType.COLUMN, 0, 5, 28, 16);

Chart chart = sheet3.getCharts().get(chartIndex);

// Setting the pivot chart data source

chart.setPivotSource("PivotTable!PivotTable1");

chart.setHidePivotFieldButtons(false);

// Saving the Excel file

workbook.save(dataDir + "Aspose_PivotChart_Out.xls");


{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/createpivotcharts/AsposePivotChart.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Pivot Tablolar ve Pivot Grafikler Oluşturun](/cells/tr/java/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}
