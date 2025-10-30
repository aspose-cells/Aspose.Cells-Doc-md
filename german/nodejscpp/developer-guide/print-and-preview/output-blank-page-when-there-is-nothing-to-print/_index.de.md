---
title: Leere Seite ausgeben, wenn nichts gedruckt werden kann, mit Node.js via C++
linktitle: Leeres Blatt ausgeben, wenn nichts gedruckt werden muss
type: docs
weight: 90
url: /de/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/
---

## **Mögliche Verwendungsszenarien**

Wenn das Blatt leer ist, druckt Aspose.Cells beim Exportieren des Arbeitsblatts in ein Bild nichts. Sie können dieses Verhalten ändern, indem Sie die [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--)-Eigenschaft verwenden. Wenn Sie sie auf **true** setzen, wird die leere Seite gedruckt.

## **Leeres Blatt ausgeben, wenn nichts gedruckt werden muss**

Das folgende Beispiel erstellt ein leeres Arbeitsbuch mit einem leeren Arbeitsblatt und rendert das leere Arbeitsblatt in ein Bild, nachdem die [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--)-Eigenschaft auf **true** gesetzt wurde. Dadurch wird die leere Seite generiert, da nichts gedruckt werden kann, siehe Bild unten.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet - it is empty sheet
const ws = wb.getWorksheets().get(0);

// Specify image or print options
// Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
// So that empty page gets printed
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Png);
opts.setOutputBlankPageWhenNothingToPrint(true);

// Render empty sheet to png image
const sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, path.join(outputDir, "OutputBlankPageWhenNothingToPrint.png"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
