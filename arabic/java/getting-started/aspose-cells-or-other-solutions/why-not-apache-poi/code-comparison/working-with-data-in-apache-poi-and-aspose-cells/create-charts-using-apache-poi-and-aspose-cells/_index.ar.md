---
title: إنشاء الرسوم البيانية باستخدام Apache POI و Aspose.Cells
type: docs
weight: 50
url: /ar/java/create-charts-using-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - إنشاء الرسوم البيانية**
من الممكن إضافة مجموعة متنوعة من الرسوم البيانية إلى جداول البيانات بمساعدة Aspose.Cells. Aspose.Cells توفر العديد من كائنات الرسم البياني المرنة.

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the newly added worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

//Adding a sample value to "A1" cell

cells.get("A1").setValue(50);

//Adding a sample value to "A2" cell

cells.get("A2").setValue(100);

//Adding a sample value to "A3" cell

cells.get("A3").setValue(150);

//Adding a sample value to "A4" cell

cells.get("A4").setValue(200);

//Adding a sample value to "B1" cell

cells.get("B1").setValue(60);

//Adding a sample value to "B2" cell

cells.get("B2").setValue(32);

//Adding a sample value to "B3" cell

cells.get("B3").setValue(50);

//Adding a sample value to "B4" cell

cells.get("B4").setValue(40);

//Adding a chart to the worksheet and

//accessing the instance of the newly added chart

int chartIndex = worksheet.getCharts().add(ChartType.COLUMN,5,0,15,5);

Chart chart = worksheet.getCharts().get(chartIndex);

//Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"

SeriesCollection nSeries = chart.getNSeries();

nSeries.add("A1:B4",true);

//Setting the chart type of 2nd NSeries to display as line chart

Series series = nSeries.get(1);

series.setType(ChartType.LINE);

{{< /highlight >}}
## **Apache POI SS (HSSF + XSSF) - إنشاء الرسوم البيانية**
**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("linechart");

final int NUM_OF_ROWS = 3;

final int NUM_OF_COLUMNS = 10;

// Create a row and put some cells in it. Rows are 0 based.

Row row;

Cell cell;

for (int rowIndex = 0; rowIndex < NUM_OF_ROWS; rowIndex++) {

    row = sheet.createRow((short) rowIndex);

    for (int colIndex = 0; colIndex < NUM_OF_COLUMNS; colIndex++) {

        cell = row.createCell((short) colIndex);

        cell.setCellValue(colIndex * (rowIndex + 1));

    }

}

Drawing drawing = sheet.createDrawingPatriarch();

ClientAnchor anchor = drawing.createAnchor(0, 0, 0, 0, 0, 5, 10, 15);

Chart chart = drawing.createChart(anchor);

ChartLegend legend = chart.getOrCreateLegend();

legend.setPosition(LegendPosition.TOP_RIGHT);

LineChartData data = chart.getChartDataFactory().createLineChartData();

// Use a category axis for the bottom axis.

ChartAxis bottomAxis = chart.getChartAxisFactory().createCategoryAxis(AxisPosition.BOTTOM);

ValueAxis leftAxis = chart.getChartAxisFactory().createValueAxis(AxisPosition.LEFT);

leftAxis.setCrosses(AxisCrosses.AUTO_ZERO);

ChartDataSource<Number> xs = DataSources.fromNumericCellRange(sheet, new CellRangeAddress(0, 0, 0, NUM_OF_COLUMNS - 1));

ChartDataSource<Number> ys1 = DataSources.fromNumericCellRange(sheet, new CellRangeAddress(1, 1, 0, NUM_OF_COLUMNS - 1));

ChartDataSource<Number> ys2 = DataSources.fromNumericCellRange(sheet, new CellRangeAddress(2, 2, 0, NUM_OF_COLUMNS - 1));


data.addSeries(xs, ys1);

data.addSeries(xs, ys2);

chart.plot(data, bottomAxis, leftAxis);

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل أمثلة تشغيل لـ **إنشاء المخططات باستخدام Apache POI و Aspose.Cells** من أي من مواقع ترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells-Java-vs-POI-SS-v1.5)
## **تحميل مصدر الكود**
تنزيل الشفرة المصدرية لـ **إنشاء المخططات باستخدام Apache POI و Aspose.Cells** من أي من مواقع ترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [إنشاء المخططات المخصصة](/cells/ar/java/creating-and-customizing-charts/).

{{% /alert %}}
