---  
title: Skapa dynamiska diagram med Node.js via C++  
linktitle: Skapa dynamiska diagram  
description: Lär dig skapa dynamiska diagram i Aspose.Cells for Node.js via C++. Denna guide visar hur du dynamiskt uppdaterar diagramdata, serier och formatering baserat på dina krav, vilket gör att du kan visa ändrande data visuellt i dina blad.  
keywords: Aspose.Cells för Node.js, diagram, dynamiska diagram, data, serier, formatering, blad, uppdatering.  
type: docs  
weight: 240  
url: /sv/nodejs-cpp/create-dynamic-charts/  
---  

{{% alert color="primary" %}}  
Dynamiska (eller interaktiva) diagram har förmågan att ändra sig när du ändrar omfånget för data. Med andra ord kan de dynamiska diagrammen automatiskt återspegla förändringar när datakällan ändras. För att trigga ändringen i datakällan kan man använda filteralternativet för Excel-tabeller eller använda en kontroll såsom ComboBox eller rullgardinslista.

Denna artikel visar användningen av Aspose.Cells for Node.js via C++ API:er för att skapa dynamiska diagram med båda nämnda metoder.  
{{% /alert %}}  

## **Använda Excel-tabeller**  

{{% alert color="primary" %}}  
Excel-tabeller kallas ListObjects i Aspose.Cells perspektiv, därför kommer vi använda termen "ListObject" istället för "Tabell" för tydlighet. Läs gärna i detalj om hur man [skapar ListObjects](/cells/sv/nodejs-cpp/create-and-format-table/) med Aspose.Cells for Node.js via C++.  
{{% /alert %}}  

ListObjects ger den inbyggda funktionen för att sortera och filtrera data vid användarinteraktion. Både sorterings- och filtreringsalternativen tillhandahålls via rullgardinslistor som automatiskt läggs till i rubrikraden för [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject). Tack vare dessa funktioner (sortering och filtrering) verkar [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) vara den perfekta kandidaten för att fungera som datakälla till ett dynamiskt diagram eftersom förändringar i sortering eller filtrering kommer att ändra datarepresentationen i diagrammet för att återspegla det aktuella tillståndet av [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject).

För att hålla demonstrationen enkel att förstå, skapar vi [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) från grunden och går framåt steg för steg enligt nedan.

1. Skapa en tom [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Åtkomst till [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) av den första [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) i [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Infoga några data i cellerna.
1. Skapa [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) baserat på den insatta datan.
1. Skapa [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) baserat på dataintervall av [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject).
1. Spara resultatet på disken.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const book = new AsposeCells.Workbook();
// Access first worksheet from the collection
const sheet = book.getWorksheets().get(0);
// Access cells collection of the first worksheet
const cells = sheet.getCells();

// Insert data column-wise
cells.get("A1").putValue("Category");
cells.get("A2").putValue("Fruit");
cells.get("A3").putValue("Fruit");
cells.get("A4").putValue("Fruit");
cells.get("A5").putValue("Fruit");
cells.get("A6").putValue("Vegetables");
cells.get("A7").putValue("Vegetables");
cells.get("A8").putValue("Vegetables");
cells.get("A9").putValue("Vegetables");
cells.get("A10").putValue("Beverages");
cells.get("A11").putValue("Beverages");
cells.get("A12").putValue("Beverages");

cells.get("B1").putValue("Food");
cells.get("B2").putValue("Apple");
cells.get("B3").putValue("Banana");
cells.get("B4").putValue("Apricot");
cells.get("B5").putValue("Grapes");
cells.get("B6").putValue("Carrot");
cells.get("B7").putValue("Onion");
cells.get("B8").putValue("Cabbage");
cells.get("B9").putValue("Potato");
cells.get("B10").putValue("Coke");
cells.get("B11").putValue("Coladas");
cells.get("B12").putValue("Fizz");

cells.get("C1").putValue("Cost");
cells.get("C2").putValue(2.2);
cells.get("C3").putValue(3.1);
cells.get("C4").putValue(4.1);
cells.get("C5").putValue(5.1);
cells.get("C6").putValue(4.4);
cells.get("C7").putValue(5.4);
cells.get("C8").putValue(6.5);
cells.get("C9").putValue(5.3);
cells.get("C10").putValue(3.2);
cells.get("C11").putValue(3.6);
cells.get("C12").putValue(5.2);

cells.get("D1").putValue("Profit");
cells.get("D2").putValue(0.1);
cells.get("D3").putValue(0.4);
cells.get("D4").putValue(0.5);
cells.get("D5").putValue(0.6);
cells.get("D6").putValue(0.7);
cells.get("D7").putValue(1.3);
cells.get("D8").putValue(0.8);
cells.get("D9").putValue(1.3);
cells.get("D10").putValue(2.2);
cells.get("D11").putValue(2.4);
cells.get("D12").putValue(3.3);

// Create ListObject, Get the List objects collection in the first worksheet
const listObjects = sheet.getListObjects();

// Add a List based on the data source range with headers on
let index = listObjects.add(0, 0, 11, 3, true);

sheet.autoFitColumns();

// Create chart based on ListObject
index = sheet.getCharts().add(AsposeCells.ChartType.Column, 21, 1, 35, 18);
const chart = sheet.getCharts().get(index);
chart.setChartDataRange("A1:D12", true);
chart.getNSeries().setCategoryData("A2:B12");

// Save spreadsheet
book.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Använda dynamiska formler**  

Om du inte vill använda [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) som datakälla till det dynamiska diagrammet, är det andra alternativet att använda Excel-funktioner (eller formler) för att skapa ett dynamiskt dataintervall och en kontroll (såsom ComboBox) för att utlösa förändringen i data. I detta scenario kommer vi att använda VLOOKUP-funktionen för att hämta lämpliga värden baserat på valet av ComboBox. När valet ändras kommer VLOOKUP att uppdatera cellvärdet. Om ett område av celler använder VLOOKUP, kan hela området uppdateras vid användarinteraktion, vilket gör att det kan användas som källa till det dynamiska diagrammet.

För att hålla demonstrationen enkel att förstå kommer vi att skapa arbetsboken från början och gå framåt steg för steg enligt följande anvisningar.

1. Skapa en tom [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Åtkomst till [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) av den första [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) i [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Infoga några data i cellerna genom att skapa en namngiven range. Dessa data kommer att tjäna som en serie till det dynamiska diagrammet.
1. Skapa [**ComboBox**](https://reference.aspose.com/cells/nodejs-cpp/combobox) baserat på det namngivna intervall som skapades i föregående steg.
1. Infoga mer data i cellerna som kommer att fungera som källa till VLOOKUP-funktionen.
1. Infoga VLOOKUP-funktion (med lämpliga parametrar) till ett cellområde. Detta område kommer att fungera som källa till det dynamiska diagrammet.
1. Skapa [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) baserat på det område som skapades i föregående steg.
1. Spara resultatet på disken.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range in the second worksheet
const range = worksheet.getCells().createRange("C21", "C24");

// Name the range
range.setName("MyRange");

// Fill different cells with data in the range
range.get(0, 0).putValue("North");
range.get(1, 0).putValue("South");
range.get(2, 0).putValue("East");
range.get(3, 0).putValue("West");

const comboBox = worksheet.getShapes().addComboBox(15, 0, 2, 0, 17, 64);
comboBox.setInputRange("=MyRange");
comboBox.setLinkedCell("=B16");
comboBox.setSelectedIndex(0);
const cell = worksheet.getCells().get("B16");
const style = cell.getStyle();
style.getFont().setColor(AsposeCells.Color.White);
cell.setStyle(style);

worksheet.getCells().get("C16").setFormula("=INDEX(Sheet1!$C$21:$C$24,$B$16,1)");

// Put some data for chart source
// Data Headers
worksheet.getCells().get("D15").putValue("Jan");
worksheet.getCells().get("D20").putValue("Jan");

worksheet.getCells().get("E15").putValue("Feb");
worksheet.getCells().get("E20").putValue("Feb");

worksheet.getCells().get("F15").putValue("Mar");
worksheet.getCells().get("F20").putValue("Mar");

worksheet.getCells().get("G15").putValue("Apr");
worksheet.getCells().get("G20").putValue("Apr");

worksheet.getCells().get("H15").putValue("May");
worksheet.getCells().get("H20").putValue("May");

worksheet.getCells().get("I15").putValue("Jun");
worksheet.getCells().get("I20").putValue("Jun");

// Data
worksheet.getCells().get("D21").putValue(304);
worksheet.getCells().get("D22").putValue(402);
worksheet.getCells().get("D23").putValue(321);
worksheet.getCells().get("D24").putValue(123);

worksheet.getCells().get("E21").putValue(300);
worksheet.getCells().get("E22").putValue(500);
worksheet.getCells().get("E23").putValue(219);
worksheet.getCells().get("E24").putValue(422);

worksheet.getCells().get("F21").putValue(222);
worksheet.getCells().get("F22").putValue(331);
worksheet.getCells().get("F23").putValue(112);
worksheet.getCells().get("F24").putValue(350);

worksheet.getCells().get("G21").putValue(100);
worksheet.getCells().get("G22").putValue(200);
worksheet.getCells().get("G23").putValue(300);
worksheet.getCells().get("G24").putValue(400);

worksheet.getCells().get("H21").putValue(200);
worksheet.getCells().get("H22").putValue(300);
worksheet.getCells().get("H23").putValue(400);
worksheet.getCells().get("H24").putValue(500);

worksheet.getCells().get("I21").putValue(400);
worksheet.getCells().get("I22").putValue(200);
worksheet.getCells().get("I23").putValue(200);
worksheet.getCells().get("I24").putValue(100);

// Dynamically load data on selection of Dropdown value
worksheet.getCells().get("D16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,2,FALSE),0)");
worksheet.getCells().get("E16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,3,FALSE),0)");
worksheet.getCells().get("F16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,4,FALSE),0)");
worksheet.getCells().get("G16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,5,FALSE),0)");
worksheet.getCells().get("H16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,6,FALSE),0)");
worksheet.getCells().get("I16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,7,FALSE),0)");

// Create Chart
const index = worksheet.getCharts().add(AsposeCells.ChartType.Column, 0, 3, 12, 9);
const chart = worksheet.getCharts().get(index);
chart.getNSeries().add("='Sheet1'!$D$16:$I$16", false);
chart.getNSeries().get(0).setName("=C16");
chart.getNSeries().setCategoryData("=$D$15:$I$15");

// Save result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
