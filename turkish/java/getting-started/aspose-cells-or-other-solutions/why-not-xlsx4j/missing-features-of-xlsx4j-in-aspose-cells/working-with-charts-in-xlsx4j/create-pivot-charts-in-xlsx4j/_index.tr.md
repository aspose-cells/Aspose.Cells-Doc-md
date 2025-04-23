---
title: xlsx4j de Pivot Grafik Oluşturma
type: docs
weight: 30
url: /tr/java/create-pivot-charts-in-xlsx4j/
---

## **Aspose.Cells - Pivot Grafik Oluşturma**
Bir özet tablo, kayıtların etkileşimli bir özeti. Örneğin, bir çalışma sayfasındaki bir listede yüzlerce fatura girişiniz olabilir. Bir özet tablo, faturaları müşteri, ürün veya tarihe göre toplayabilir. Microsoft Excel ile özet tablonun düğmeleri sürüklenerek bilgileri hızlı bir şekilde yeniden düzenlemek mümkündür.
Bir özet grafik, bir özet tablonun verilerinin etkileşimli grafiksel bir temsilidir. Özet grafikler Excel 2000'de tanıtılmıştır. Özet grafik kullanmak, özet tablonun alt toplamlarını ve toplamlarını otomatik olarak oluşturduğu için verileri anlamak daha da kolaylaştırır.

Aspose.Cells, pivot tabloları ve pivot grafiklerini destekler.

**Java**

{{< highlight java >}}

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
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/createpivotcharts/AsposePivotChart.java)

{{% alert color="primary" %}} 

Daha fazla ayrıntı için [Pivot Tabloları ve Pivot Grafikler Oluşturma](/cells/tr/java/create-pivot-tables-and-pivot-charts/) sayfasını ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
