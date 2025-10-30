---  
title: Geben Sie an, wie Strings im Ausgabepdf und Bild mit Node.js über C++ gekreuzt werden sollen  
linktitle: Angabe, wie Zeichen in der Ausgabedatei PDF und Bild gekreuzt werden sollen  
type: docs  
weight: 120  
url: /de/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/  
description: Lernen Sie, die Textüberlauf im Ausgabepdf/Bild zu steuern, indem Sie den Kreuztyp mit Aspose.Cells for Node.js via C++ festlegen.  
---  

## **Mögliche Verwendungsszenarien**

Wenn eine Zelle Text oder eine Zeichenkette enthält, aber diese größer ist als die Breite der Zelle, überläuft die Zeichenkette, wenn die nächste Zelle in der nächsten Spalte null oder leer ist. Beim Speichern Ihrer Excel-Datei als PDF/Bild können Sie diesen Überlauf steuern, indem Sie den Kreuztyp mit dem [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype) Enumerationswert festlegen. Es hat die folgenden Werte:

- **TextCrossType.Default**: Zeigt den Text wie MS Excel an, der von der nächsten Zelle abhängt. Wenn die nächste Zelle null ist, wird die Zeichenkette kreuzen oder abgeschnitten.

- **TextCrossType.CrossKeep**: Zeigen Sie die Zeichenfolge wie MS Excel beim Exportieren in PDF/Bild.

- **TextCrossType.CrossOverride**: Zeigen Sie den gesamten Text, indem Sie andere Zellen kreuzen und den Text der gekreuzten Zellen überschreiben.

- **TextCrossType.StrictInCell**: Zeige nur den String innerhalb der Breite der Zelle an.

## **Angabe, wie Zeichen in der Ausgabedatei PDF/Bild mithilfe von TextCrossType überquert werden sollen**

Der folgende Beispielcode lädt die Beispiel-Excel-Datei und speichert sie im PDF-/Bildformat, indem verschiedene [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype) angegeben werden. Die Beispiel-Excel-Datei und Ausgabedateien können von den folgenden Links heruntergeladen werden:

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### Beispielcode

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCrosssType.xlsx"));

// Initialize PDF save options
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set text cross type
pdfSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Save PDF file
workbook.save(outputDir + "outputCrosssType.pdf", pdfSaveOptions);

// Initialize image or print options
const imageSaveOptions = new AsposeCells.ImageOrPrintOptions();

// Set text cross type
imageSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Initialize sheet renderer object
const sheetRenderer = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imageSaveOptions);

sheetRenderer.toImage(0, outputDir + "outputCrosssType.png");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
