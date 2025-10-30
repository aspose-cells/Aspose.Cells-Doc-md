---
title: Hur man skapar ett dynamiskt diagram med dropdownlista med Node.js via C++
linktitle: Hur man skapar dynamiskt diagram med rullistan
description: Lär dig hur man skapar ett dynamiskt diagram som uppdateras baserat på ett dropdownsval med Aspose.Cells for Node.js via C++. Vår steg för steg guide visar hur du integrerar en dropdownlista i ditt diagram för flexibel datavisualisering.
keywords: Aspose.Cells for Node.js via C++, Dynamiskt diagram, Dropdownlista, Datavisualisering, Integration, Flexibel visualisering.
type: docs
weight: 76
url: /sv/nodejs-cpp/create-dynamic-chart-with-dropdownlist/
---

## **Möjliga användningsscenario**
Ett dynamiskt diagram med rullistan i Excel är ett kraftfullt verktyg som låter användare skapa interaktiva diagram som dynamiskt kan uppdateras baserat på den valda data. Denna funktion är särskilt användbar i situationer där det finns ett behov av att analysera flera dataset eller jämföra olika scenarier.

En vanlig tillämpning av ett dynamiskt diagram med rullistan är inom finansiell analys. Till exempel kan ett företag ha flera uppsättningar av finansiella data för olika år eller avdelningar. Genom att använda en rullista kan användare välja det specifika dataset de vill analysera, och diagrammet kommer automatiskt att uppdateras för att visa den motsvarande informationen. Detta möjliggör enkel jämförelse och identifiering av trender eller mönster.

En annan tillämpning är inom försäljning och marknadsföring. Ett företag kan ha försäljningsdata för olika produkter eller regioner. Med ett dynamiskt diagram med rullista kan användare välja en specifik produkt eller region från rullistan, och diagrammet kommer dynamiskt att uppdateras för att visa försäljningsprestandan för det valda alternativet. Detta hjälper till att identifiera de bäst presterande områdena eller produkterna och fatta data-drivna beslut.

Sammanfattningsvis ger ett dynamiskt diagram med rullista i Excel ett flexibelt och interaktivt sätt att visualisera och analysera data. Det är värdefullt i situationer där det finns ett behov av att jämföra flera dataset eller utforska olika scenarier, vilket gör det till ett mångsidigt verktyg för finansiell analys, försäljning och marknadsföring samt många andra tillämpningar.

## **Använd Aspose Cells för att skapa dynamiskt diagram med rullista**
 I följande avsnitt visar vi hur du skapar ett dynamiskt diagram med Dropdownlist med Aspose.Cells for Node.js via C++. Vi visar koden för exemplet, samt Excel-filen som skapats med denna kod.

## **Exempelkod**
Följande exempelkod kommer att generera [Dynamic Chart with Dropdownlist File](DynamicChartWithDropdownlist.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A3").putValue("Tea");
sheet.getCells().get("A4").putValue("Coffee");
sheet.getCells().get("A5").putValue("Sugar");

// In this example, we will add 12 months of data
sheet.getCells().get("B2").putValue("Jan");
sheet.getCells().get("C2").putValue("Feb");
sheet.getCells().get("D2").putValue("Mar");
sheet.getCells().get("E2").putValue("Apr");
sheet.getCells().get("F2").putValue("May");
sheet.getCells().get("G2").putValue("Jun");
sheet.getCells().get("H2").putValue("Jul");
sheet.getCells().get("I2").putValue("Aug");
sheet.getCells().get("J2").putValue("Sep");
sheet.getCells().get("K2").putValue("Oct");
sheet.getCells().get("L2").putValue("Nov");
sheet.getCells().get("M2").putValue("Dec");
const allMonths = 12;
const iCount = 3;
for (let i = 0; i < iCount; i++) {
for (let j = 0; j < allMonths; j++) {
const _row = i + 2;
const _column = j + 1; 
sheet.getCells().get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
}
}

// This is the Dropdownlist for Dynamic Data
const ca = AsposeCells.CellArea.createCellArea(9, 0, 9, 0);
const _index = sheet.getValidations().add(ca);
const _va = sheet.getValidations().get(_index);
_va.setType(AsposeCells.ValidationType.List);
_va.setInCellDropDown(true);
_va.setFormula1("=$B$2:$M$2");
sheet.getCells().get("A9").putValue("Current Month");
sheet.getCells().get("A10").putValue("Jan");
const _style = sheet.getCells().get("A10").getStyle();
_style.getFont().setIsBold(true);
_style.setPattern(AsposeCells.BackgroundType.Solid);
_style.setForegroundColor(AsposeCells.Color.Yellow);
sheet.getCells().get("A10").setStyle(_style);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtMonthData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtXLabels");
sheets.getNames().get(index).setRefersTo("=Sheet1!$A$3:$A$5");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 8, 2, 20, 8);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("month", true);
chart.getNSeries().get(0).setName("=Sheet1!$A$10");
chart.getNSeries().get(0).setValues("Sheet1!ChtMonthData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtXLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicChartWithDropdownlist.xlsx"));
```

## **Anteckningar**
I den genererade filen kommer diagrammet dynamiskt att räkna data för den valda månaden. Detta görs med hjälp av "OFFSET"-formeln i provkoden:

```
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

Du kan prova att ändra värde i listrutan i cellen "Ark1!$A$10", och du kommer att se den dynamiska förändringen av diagrammet. Nu har vi skapat ett dynamiskt diagram med rullgardinsmeny med hjälp av Aspose.Cells framgångsrikt.
{{< app/cells/assistant language="nodejs-cpp" >}}
