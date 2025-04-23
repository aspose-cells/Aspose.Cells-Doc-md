---  
title: Sätt områdegräns med Node.js via C++  
linktitle: Ange intervallsram  
type: docs  
weight: 600  
url: /sv/nodejs-cpp/set-range-border/  
---  

## **Möjliga användningsscenario**  
 När du vill sätta gränsen för ett område behöver du inte sätta varje cell individuellt. Du kan ange gränsen för området. Aspose.Cells for Node.js via C++ erbjuder denna funktion.  
Denna artikel ger ett exempel på kod som använder Aspose.Cells for Node.js via C++ för att sätta områdegräns.  

## **Ange intervallsram i Excel**  
För att ställa in gränsen för en serie i Excel kan du följa dessa steg:  
1. Välj det cellområde där du vill tillämpa gränsen.  
2. I fliken "Start" på menyfliksområdet, leta upp gruppen "Teckenformat".  
3. Inom gruppen "Teckenformat", klicka på knappen "Gränser".  
<br>  
<img src="border.png" />  
4. Välj den typ av gräns som du vill använda från alternativen i rullgardinsmenyn. Du kan välja mellan förinställda gränstyper eller anpassa din egen gräns.  
5. När du har valt önskad gränstil kommer gränsen att appliceras på det valda cellområdet.  

## **Sätt områdegräns med Aspose.Cells for Node.js via C++**  
Detta exempel visar hur man:  

1. Skapa en arbetsbok.  
2. Lägg till data i celler i första kalkylbladet.  
3. Skapa en [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).  
4. Sätt inre gräns för området.  
5. Sätt yttre gräns för området.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Create a range (A1:C5).
const range = cells.createRange("A1", "C5");

// set inner border of range
const innerColor = workbook.createCellsColor();
innerColor.setColor(AsposeCells.Color.Red);
range.setInsideBorders(AsposeCells.BorderType.Vertical, AsposeCells.CellBorderType.Thin, innerColor);
innerColor.setColor(AsposeCells.Color.Green);
range.setInsideBorders(AsposeCells.BorderType.Horizontal, AsposeCells.CellBorderType.Thin, innerColor);

// set outer border of range
const outerColor = workbook.createCellsColor();
outerColor.setColor(AsposeCells.Color.Blue);
range.setOutlineBorders(AsposeCells.CellBorderType.Thin, outerColor);

workbook.save("out.xlsx");
```  
