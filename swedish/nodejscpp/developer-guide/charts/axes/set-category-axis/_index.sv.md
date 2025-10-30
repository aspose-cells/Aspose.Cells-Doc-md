---
title: Hur man ställer in kategori axeln med Node.js via C++
linktitle: Hur man ställer in kategori axeln
description: Lär dig hur du ställer in kategori axeln i Aspose.Cells for Node.js via C++. Vår guide hjälper dig att förstå hur du definierar kategori axelns intervall, justerar dess egenskaper och formaterar dess etiketter.
keywords: Aspose.Cells for Node.js via C++, kategori axel, inställning, intervall, egenskaper, formatering.
type: docs
weight: 205
url: /sv/nodejs-cpp/how-to-set-category-axis/
---

## **Möjliga användningsscenario**
Efter att du har skapat ett diagram i ett arbetsblad kan du ställa in kategoriaxeln för det. I denna artikel visar vi hur du ställer in kategoriaxeln för ett Excel-diagram med hjälp av Aspose.Cells och exempel på kod.

## **Stegen i provkod**

1. Skapa en ny arbetsbok.

2. Skapa en ny diagram i den första arbetsbladet.

3. Lägg till några värden i celler i det första arbetsbladet.

4. Nu kan du ställa in kategori-axeln; det finns två sätt: med celldata eller med strängar direkt, båda visas i exempel-koden.

5. Ställ in värdeaxeln och spara arbetsboken för att visa resultatet.

## **Exempelkod**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const dataDir = ""; // Update with your path

// Create a new workbook
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CHART");

// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 8, 0, 20, 10);
const chart = worksheet.getCharts().get(chartIndex);

// Add some values to cells
worksheet.getCells().get("A1").putValue("Sales");
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(130);
worksheet.getCells().get("A5").putValue(160);
worksheet.getCells().get("A6").putValue(150);
worksheet.getCells().get("B1").putValue("Days");
worksheet.getCells().get("B2").putValue(1);
worksheet.getCells().get("B3").putValue(2);
worksheet.getCells().get("B4").putValue(3);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("B6").putValue(5);

// Some values in string
const Sales = "100,150,130,160,150";
const Days = "1,2,3,4,5";

// Set Category Axis Data with string
chart.getNSeries().setCategoryData(`{${Days}}`);
// Or you can set Category Axis Data with data in cells
// chart.getNSeries().setCategoryData("B2:B6");

// Add Series to the chart
chart.getNSeries().add("Demand1", true);
// Set value axis with string 
chart.getNSeries().get(0).setValues(`{${Sales}}`);
chart.getNSeries().add("Demand2", true);
// Set value axis with data in cells
chart.getNSeries().get(1).setValues("A2:A6");

// Set some Category Axis properties
chart.getCategoryAxis().getTickLabels().setRotationAngle(45);
chart.getCategoryAxis().getTickLabels().getFont().setSize(8);
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

// Save the workbook to view the result file
workbook.save(path + "Output.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
