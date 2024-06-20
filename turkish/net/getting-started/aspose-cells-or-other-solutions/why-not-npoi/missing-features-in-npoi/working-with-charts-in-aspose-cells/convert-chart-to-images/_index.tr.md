---
title: Grafiği Görüntüye Dönüştürme
type: docs
weight: 10
url: /tr/net/convert-chart-to-images/
---

## **Aspose.Cells - Grafiği Görüntüye Dönüştürme**
Grafikler görsel açıdan çekicidir ve kullanıcıların verilerde karşılaştırmaları, desenleri ve trendleri görmelerini kolaylaştırır.
Chart sınıfının toImage metodu, grafiği bir resim dosyasına dönüştürerek, diske veya akıma kaydedilebilecek bir resme dönüştürür.

**C#**

{{< highlight cs >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Obtaining the reference of the first worksheet

WorksheetCollection worksheets = workbook.Worksheets;

Worksheet sheet = worksheets[0];

// Adding some sample value to cells

Cells cells = sheet.Cells;

Cell cell = cells["A1"];

cell.Value = 50;

cell = cells["A2"];

cell.Value = 100;

cell = cells["A3"];

cell.Value = 150;

cell = cells["B1"];

cell.Value = 4;

cell = cells["B2"];

cell.Value = 20;

cell = cells["B3"];

cell.Value = 50;

ChartCollection charts = sheet.Charts;

// Adding a chart to the worksheet

int chartIndex = charts.Add(ChartType.Pyramid, 5, 0, 15, 5);

Chart chart = charts[chartIndex];

//Save the chart image file.

chart.ToImage("AsposeChartImage.png", ImageFormat.Png);

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen herhangi bir sosyal kodlama sitesinden **Grafiği Görüntüye Dönüştürme** formunu indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Convert.Chart.To.Images.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Grafiği SVG Formatında Görüntüye Dönüştürme](/cells/tr/net/converting-chart-to-image-in-svg-format/) sayfasını ziyaret edin.

{{% /alert %}}
