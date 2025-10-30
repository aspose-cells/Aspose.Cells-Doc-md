---
title: Wie man die Arbeitsmappenansicht mit Node.js über C++ kontrolliert
linktitle: Wie man die Ansicht der Arbeitsmappe steuert
type: docs
weight: 600
url: /de/nodejs-cpp/how-to-control-workbook-view/
description: Erfahren Sie, wie Sie die Arbeitsmappenansicht durch die API Aspose.Cells for Node.js via C++ steuern.
keywords: Wie man die Arbeitsmappenansicht mit Node.js über C++, Excel Ansicht mit Node.js über C++ festlegt, Arbeitsmappenansicht mit Node.js über C++ bedient, Arbeitsmappenansicht mit Node.js über C++ setzt, Excel Ansicht mit Node.js über C++ kontrolliert.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie die Anzeige der Excel-Seiten anpassen müssen, sollten Sie wissen, wie man jede Komponente steuert, z. B. horizontale und vertikale Bildlaufleisten, ob offene Excel-Dateien versteckt werden sollen usw. Aspose.Cells for Node.js via C++ bietet diese Funktion an. Aspose.Cells for Node.js via C++ stellt die folgenden Eigenschaften und Methoden bereit, um Ihre Ziele zu erreichen.

- [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)
- [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--)
- [**WorkbookSettings.isHidden()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHidden--)
- [**WorkbookSettings.isMinimized()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isMinimized--)
- [**WorkbookSettings.getWindowHeight()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowHeight--)
- [**WorkbookSettings.getWindowWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowWidth--)
- [**WorkbookSettings.getWindowLeft()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowLeft--)
- [**WorkbookSettings.getWindowTop()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowTop--)

## **So steuern Sie die Arbeitsmappenansicht mit Aspose.Cells for Node.js via C++**
Dieses Beispiel zeigt, wie Sie:

1. Ein Arbeitsbuch erstellen.
1. Daten zu Zellen im ersten Arbeitsblatt hinzufügen.
1. Horizontale und vertikale Bildlaufleisten der Arbeitsbuchansicht ausblenden.

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

Vorschau der Ergebnisdatei:
<br>
<image src="result.png" width="70%" />

{{< app/cells/assistant language="nodejs-cpp" >}}
