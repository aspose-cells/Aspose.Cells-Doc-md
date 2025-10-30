---
title: Excel in HTML  Verwendung der PresentationPreference Option für besseres Layout mit Node.js über C++
linktitle: Excel zu HTML  Verwenden Sie die PresentationPreference Option für ein besseres Layout
type: docs
weight: 220
url: /de/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
---

{{% alert color="primary" %}} 

Aspose.Cells bietet eine nützliche Eigenschaft HtmlSaveOptions.presentationPreference für Entwickler, die beim Speichern einer Microsoft Excel-Datei in HTML- oder MHT-Format ein ansprechenderes Layout wünschen. Der Standardwert der Eigenschaft ist false. Wir empfehlen, diese Eigenschaft auf true zu setzen, um eine attraktivere Präsentation von Excel-Berichten zu erhalten.

{{% /alert %}} 

Siehe den untenstehenden Beispielcode, der zeigt, wie man eine HTML-Datei aus einem Excel-Bericht mit Präsentationspräferenz rendert.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate the Workbook
// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Create HtmlSaveOptions object
const options = new AsposeCells.HtmlSaveOptions();
// Set the Presentation preference option
options.setPresentationPreference(true);

// Save the Excel file to HTML with specified option
workbook.save(path.join(dataDir, "outPresentationlayout1.out.html"), options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
