---  
title: Bereichsrahmen mit Node.js via C++ setzen  
linktitle: Bereichsgrenze festlegen  
type: docs  
weight: 600  
url: /de/nodejs-cpp/set-range-border/  
---  

## **Mögliche Verwendungsszenarien**  
Wenn Sie den Rahmen für einen Bereich setzen möchten, müssen Sie nicht jede Zelle einzeln setzen. Sie können den Rahmen für den gesamten Bereich festlegen. Aspose.Cells for Node.js via C++ bietet diese Funktion.  
Dieser Artikel enthält ein Beispiel, das zeigt, wie mit Aspose.Cells for Node.js via C++ der Bereichsrahmen gesetzt wird.  

## **Bereichsgrenze in Excel festlegen**  
Um die Grenze eines Bereichs in Excel festzulegen, befolgen Sie diese Schritte:  
1. Wählen Sie den Zellenbereich aus, für den Sie die Grenze festlegen möchten.  
2. Suchen Sie im Register „Start“ in der Gruppe „Schriftart“.  
3. Klicken Sie in der Gruppe „Schriftart“ auf die Schaltfläche „Rahmen“.  
<br>  
<img src="border.png" />  
4. Wählen Sie den zu verwendenden Randtyp aus den Optionen im Dropdown-Menü aus. Sie können aus voreingestellten Rahmenstilen wählen oder Ihren eigenen Rahmen anpassen.  
5. Sobald Sie den gewünschten Rahmenstil ausgewählt haben, wird der Rahmen auf den ausgewählten Zellenbereich angewendet.  

## **Bereichsrahmen mit Aspose.Cells for Node.js via C++ setzen**  
Dieses Beispiel zeigt, wie Sie:  

1. Ein Arbeitsbuch erstellen.  
2. Daten in die Zellen des ersten Arbeitsblatts einfügen.  
3. Erstellen Sie ein [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).  
4. Setzen Sie den inneren Rahmen des Bereichs.  
5. Setzen Sie den äußeren Rahmen des Bereichs.  

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
{{< app/cells/assistant language="nodejs-cpp" >}}
