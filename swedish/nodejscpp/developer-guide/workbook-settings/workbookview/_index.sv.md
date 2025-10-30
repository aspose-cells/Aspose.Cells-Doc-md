---
title: Hur man styr arbetsboksvisningen med Node.js via C++
linktitle: Hur man Kontrollerar Workbook View
type: docs
weight: 600
url: /sv/nodejs-cpp/how-to-control-workbook-view/
description: Lär dig hur du styr arbetsboksvisningen genom Aspose.Cells for Node.js via C++ API.
keywords: Hur man styr arbetsboksvisningen med Node.js via C++, sätt Excel vy med Node.js via C++, hantera arbetsboksvisning med Node.js via C++, sätt arbetsboksvisning med Node.js via C++, styra Excel vy med Node.js via C++.
---

## **Möjliga användningsscenario**
När du behöver justera visningen av Excel-sidor måste du veta hur du styr varje modul, såsom horisontella och vertikala skrollningslador, om du ska dölja öppna Excel-filer, och så vidare. Aspose.Cells for Node.js via C++ erbjuder denna funktion. Aspose.Cells for Node.js via C++ tillhandahåller följande egenskaper och metoder för att hjälpa dig att uppnå dina mål.

- [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)
- [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--)
- [**WorkbookSettings.isHidden()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHidden--)
- [**WorkbookSettings.isMinimized()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isMinimized--)
- [**WorkbookSettings.getWindowHeight()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowHeight--)
- [**WorkbookSettings.getWindowWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowWidth--)
- [**WorkbookSettings.getWindowLeft()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowLeft--)
- [**WorkbookSettings.getWindowTop()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowTop--)

## **Hur man styr arbetsboksvisning med Aspose.Cells for Node.js via C++**
Detta exempel visar hur man:

1. Skapa en arbetsbok.
1. Lägga till data till celler i den första arbetsboken.
1. Dölj horisontella och vertikala rullningsfält för Workbook View.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating an Workbook object
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

cell = cells.get("E10");
const temp = workbook.createStyle();
temp.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(temp);

// Hide horizontal and vertical scrollbars
workbook.getSettings().setIsHScrollBarVisible(false);
workbook.getSettings().setIsVScrollBarVisible(false);

workbook.save("out.xlsx");
```

Förhandsgranskning av resultatfil:
<br>
<image src="result.png" width="70%" />

{{< app/cells/assistant language="nodejs-cpp" >}}
