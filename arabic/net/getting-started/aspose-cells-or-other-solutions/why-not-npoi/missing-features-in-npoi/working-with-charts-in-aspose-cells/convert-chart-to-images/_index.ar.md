---
title: تحويل الرسم البياني إلى صور
type: docs
weight: 10
url: /ar/net/convert-chart-to-images/
---

## **Aspose.Cells - تحويل الرسم البياني إلى صور**
الرسوم البيانية جذابة بصريًا وتجعل من السهل على المستخدمين رؤية المقارنات والأنماط والاتجاهات في البيانات.
تقوم طريقة toImage في فئة Chart بتحويل الرسم البياني إلى ملف صورة يمكن حفظه على القرص أو تيار.

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
## **تحميل رمز التشغيل**
تحميل **تحويل الرسومات البيانية إلى صور** من أيّ من المواقع الرمزية الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Convert.Chart.To.Images.Aspose.Cells.zip)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [تحويل الرسم البياني إلى صورة](/cells/ar/net/converting-chart-to-image-in-svg-format/).

{{% /alert %}}
