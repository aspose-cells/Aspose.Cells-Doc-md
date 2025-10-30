---  
title: Wie man das Tabellenregister mit Node.js über C++ kontrolliert  
linktitle: Steuerung der Registerkartenleiste  
type: docs  
weight: 600  
url: /de/nodejs-cpp/how-to-control-sheet-tab-bar/  
description: Erfahren Sie, wie Sie die Registerkartenleiste mithilfe von Aspose.Cells for Node.js via C++ steuern.  
keywords: Wie man die Registerkartenleiste mit Node.js über C++ steuert, Arbeitsblatt Registerkartenleiste mit Node.js über C++ bedient, Registerkartenleiste mit Node.js über C++ setzt, Registerkartenleiste mit Node.js über C++ kontrolliert.  
---  

## **Mögliche Verwendungsszenarien**  
Wenn Sie die Anzeige der Excel-Tab-Leiste anpassen müssen, sollten Sie wissen, wie Sie die Registerkartenleiste steuern, z. B. das Verbergen oder Anzeigen der Registerkartenleiste, Ändern der Breite der Registerkartenleiste, Festlegen des ersten sichtbaren Tabs usw. Aspose.Cells for Node.js via C++ unterstützt diese Funktionen. Aspose.Cells bietet die folgenden Eigenschaften und Methoden, um Ihre Ziele zu erreichen.

- [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--)
- [**WorkbookSettings.getSheetTabBarWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getSheetTabBarWidth--)
- [**WorkbookSettings.getFirstVisibleTab()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getFirstVisibleTab--)

## **Wie man die Registerkartenleiste mit Aspose.Cells for Node.js via C++ kontrolliert**  
Dieses Beispiel zeigt, wie Sie:

1. Ein Arbeitsbuch erstellen.
1. Daten zu Zellen im ersten Arbeitsblatt hinzufügen.
1. Zeigen Sie die Registerkarte an und legen Sie die Breite der Registerkartenleiste fest.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
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

// Display the sheet tab and set the width of the tab bar
workbook.getSettings().setShowTabs(true);
workbook.getSettings().setSheetTabBarWidth(150);

workbook.save("out.xlsx");
```

Vorschau der Ergebnisdatei:  
<br>  
<image src="result.png" width="70%" />  


{{< app/cells/assistant language="nodejs-cpp" >}}
