---
title: Преобразовать диаграмму в изображения
type: docs
weight: 10
url: /ru/net/convert-chart-to-images/
---
## **Aspose.Cells - Преобразование диаграммы в изображения**
Диаграммы визуально привлекательны и позволяют пользователям легко видеть сравнения, закономерности и тенденции в данных.
Метод toImage класса Chart преобразует диаграмму в файл изображения, который можно сохранить на диск или в поток.

**C#**

{{< highlight "cs" >}}

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
## **Скачать рабочий код**
 Скачать**Преобразовать диаграмму в изображения** сформировать любой из перечисленных ниже сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Convert.Chart.To.Images.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Преобразование диаграммы в изображение](/cells/ru/net/converting-chart-to-image-in-svg-format/).

{{% /alert %}}
