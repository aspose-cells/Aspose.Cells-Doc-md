---  
title: Aktualisieren Sie die Werte verknüpfter Formen mit Node.js via C++  
linktitle: Aktualisieren von Werten verknüpfter Formen  
type: docs  
weight: 3200  
url: /de/nodejs-cpp/refresh-values-of-linked-shapes/  
description: Erfahren Sie, wie Sie die Werte verknüpfter Formen in Excel mit Aspose.Cells for Node.js via C++ aktualisieren.  
---  

{{% alert color="primary" %}}  

Manchmal haben Sie eine verknüpfte Form in Ihrer Excel-Datei, die mit einer Zelle verbunden ist. Änderungen an der verknüpften Zelle ändern auch die verknüpfte Form. Dies funktioniert auch mit Aspose.Cells for Node.js via C++, wenn Sie Ihre Arbeitsmappe im XLS- oder XLSX-Format speichern. Wenn Sie die Arbeitsmappe jedoch im PDF- oder HTML-Format speichern möchten, müssen Sie die Methode [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--) aufrufen, um den Wert der verknüpften Form zu aktualisieren.  

{{% /alert %}}  

## Beispiel  

Das folgende Screenshot zeigt die Quell-Excel-Datei, die im untenstehenden Beispielcode verwendet wird. Es enthält ein verbundenes Bild, das mit den Zellen A1 bis E4 verknüpft ist. Wir werden den Wert der Zelle B4 mit Aspose.Cells ändern und dann die [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--)-Methode aufrufen, um den Wert des Bildes zu aktualisieren und als PDF zu speichern.  

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)  

Sie können die [Quell-Excel-Datei](95584291.xlsx) und das [Ausgabepdf](95584292.pdf) über die bereitgestellten Links herunterladen.  

### Node.js-Code zum Aktualisieren der Werte verknüpfter Formen  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleRefreshValueOfLinkedShapes.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Change the value of cell B4
const cell = worksheet.getCells().get("B4");
cell.putValue(100);

// Update the value of the Linked Picture which is linked to cell B4
worksheet.getShapes().updateSelectedValue();

// Save the workbook in PDF format
workbook.save(path.join(outputDir, "outputRefreshValueOfLinkedShapes.pdf"), AsposeCells.SaveFormat.Pdf);
```  
