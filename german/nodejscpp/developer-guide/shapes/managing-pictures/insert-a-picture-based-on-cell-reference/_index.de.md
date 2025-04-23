---
title: Einfügen eines Bildes basierend auf Zellreferenz mit Node.js über C++
linktitle: Bild anhand eines Zellbezugs einfügen
type: docs
weight: 150
url: /de/nodejs-cpp/insert-a-picture-based-on-cell-reference/
description: Lernen Sie, wie Sie basierend auf einer Zellreferenz ein Bild in ein Arbeitsblatt einfügen, indem Sie Aspose.Cells for Node.js via C++ verwenden. Zeigen Sie Zellendaten in einem Bild.
---

{{% alert color="primary" %}}
Manchmal haben Sie ein leeres Bild und müssen Daten oder Inhalte im Bild anzeigen, indem Sie einen Zellbezug in der Formel-Leiste festlegen. Aspose.Cells unterstützt diese Funktion (Microsoft Excel 2010).
{{% /alert %}}

## Einfügen eines Bildes anhand eines Zellbezugs

Aspose.Cells for Node.js via C++ unterstützt das Anzeigen des Inhalts einer Zelle in einer Bildform. Sie können das Bild mit der Zelle verknüpfen, die die anzuzeigenden Daten enthält. Da die Zelle oder der Zellbereich mit dem Grafikobjekt verknüpft ist, erscheinen Änderungen an den Daten in dieser Zelle oder diesem Zellbereich automatisch im Grafikobjekt. Fügen Sie ein Bild in das Arbeitsblatt ein, indem Sie die Methode [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) der Sammlung [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection) (eingeschlossen in das [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) Objekt) aufrufen. Bestimmen Sie den Zellbereich mit dem [**Picture.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--) Attribut des [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture) Objekts.

### Codebeispiel

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

// Get the conditional icon's image data
const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
// Create a stream based on the image data
const stream = Uint8Array.from(imagedata);

// Add a blank picture to the D1 cell
const pic = workbook.getWorksheets().get(0).getShapes().addPicture(0, 3, stream, 10, 10);
// Specify the formula that refers to the source range of cells
pic.setFormula("A1:C10");
// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "referencedpicture.out.xlsx"));
```
