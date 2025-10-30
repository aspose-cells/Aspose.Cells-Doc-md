---
title: Rendern des Arbeitsblatts in einen Grafik Kontext mit Node.js via C++
linktitle: Arbeitsblatt in Grafikkontext rendern
type: docs
weight: 300
url: /de/nodejs-cpp/render-worksheet-to-graphic-context/
description: Erfahren Sie, wie Sie ein Arbeitsblatt mithilfe von Aspose.Cells for Node.js via C++ in einen Grafik Kontext rendern. Dies umfasst das Rendern in Bilddateien, auf Bildschirmen und Druckern.
---

{{% alert color="primary" %}}

Aspose.Cells kann jetzt Arbeitsblätter in einen Grafik-Kontext rendern. Der Grafik-Kontext kann alles Mögliche sein, z. B. eine Bilddatei, ein Bildschirm oder ein Drucker. Bitte verwenden Sie eine der beiden folgenden Methoden, um ein Arbeitsblatt in einen Grafik-Kontext zu rendern.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

Der folgende Code veranschaulicht, wie man mit Aspose.Cells ein Arbeitsblatt in einen Grafik-Kontext rendert. Nach der Ausführung des Codes wird das gesamte Arbeitsblatt ausgegeben und der verbleibende leere Raum im Grafik-Kontext wird mit blauer Farbe ausgefüllt, und das Bild wird als **OutputImage_out_.png** gespeichert. Sie können jede Quelldatei Excel verwenden, um diesen Code auszuprobieren. Bitte lesen Sie auch die Kommentare im Code für ein besseres Verständnis.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Create workbook object from source file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create empty image buffer
const bmpOptions = new AsposeCells.ImageOrPrintOptions();
bmpOptions.setOnePagePerSheet(true);

// Render worksheet to image
const sheetRender = new AsposeCells.SheetRender(worksheet, bmpOptions);
sheetRender.toImage(0, dataDir + "/OutputImage_out.png");

// Save the image in Png format
```
{{< app/cells/assistant language="nodejs-cpp" >}}
