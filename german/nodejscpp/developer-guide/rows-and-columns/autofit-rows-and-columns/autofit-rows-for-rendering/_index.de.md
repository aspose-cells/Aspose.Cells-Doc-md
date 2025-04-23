---  
title: AutoFit Zeilen zur Darstellung mit Node.js über C++  
linktitle: AutoFit für das Rendern von Zeilen  
type: docs  
weight: 130  
url: /de/nodejs-cpp/autofit-rows-for-rendering/  
description: Lernen, wie man Zeilen in Excel mit Aspose.Cells for Node.js via C++ automatisch anpasst, um eine Darstellung zu optimieren. Verhindern Sie das Abschneiden von Texten in gespeicherten PDF Dateien.  
---  

Im Allgemeinen können Sie beim Anzeigen aller Textinhalte in einer Zelle die Zeile im Normalansicht mit 100 % Zoom in Microsoft Excel automatisch anpassen. Dadurch ist der Text in der Normalansicht vollständig sichtbar, und auch beim Drucken oder Speichern als PDF wird der Text korrekt angezeigt.

In einigen Fällen funktioniert die automatische Zeilenanpassung in der Normalansicht gut, aber beim Wechsel in die Druckansicht oder beim Speichern als PDF wird der Text abgeschnitten. Bitte prüfen Sie die Quelldatei [Book1.xlsx](Book1.xlsx) und Screenshots.

![Text wird in der Druckansicht beschnitten](text_clipped_in_printview.png)

Wenn Sie verhindern möchten, dass Text im gespeicherten PDF-Datei abgeschnitten wird, können Sie die Zeile mit der Option [AutoFitterOptions.getForRendering()](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getForRendering--) automatisch anpassen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Init workbook instance.
const workbook = new AsposeCells.Workbook(filePath);

// Set autofit options for rendering.
const autoFitterOptions = new AsposeCells.AutoFitterOptions();
autoFitterOptions.setForRendering(true);

// Autofit rows with options.
workbook.getWorksheets().get(0).autoFitRows(autoFitterOptions);

// Save to pdf.
workbook.save("output.pdf", AsposeCells.SaveFormat.Pdf);
```

Nun wird der Text nicht in der Ausgabe-PDF-Datei beschnitten.

![Text wird in der gespeicherten PDF-Datei nicht beschnitten](text_not_clipped_in_saved_pdf.png)  
