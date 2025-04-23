---
title: Nur bestimmte Unicode Zeichen während des Speicherns in PDF ändern
linktitle: Ändern Sie die Schriftart nur für bestimmte Unicode Zeichen beim Speichern in PDF
type: docs
weight: 260
url: /de/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Lernen Sie, wie Sie die Schriftart bestimmter Unicode Zeichen beim Speichern in PDF mit Aspose.Cells for Node.js via C++ ändern. 
---

{{% alert color="primary" %}} 

Einige Unicode-Zeichen können von der benutzerdefinierten Schriftart nicht angezeigt werden. Ein solches Unicode-Zeichen ist **Trennstrich** (U+2011) und seine Unicode-Nummer ist 8209. Dieses Zeichen kann nicht mit **Times New Roman** angezeigt werden, aber es kann mit anderen Schriften wie **Arial Unicode MS** angezeigt werden.

 Wenn ein solches Zeichen innerhalb eines Wortes oder Satzes auftritt, das in einer bestimmten Schriftart wie Times New Roman vorliegt, ändert Aspose.Cells die Schriftart des gesamten Wortes oder Satzes in eine Schriftart, die dieses Zeichen anzeigen kann, z.B. Arial Unicode oder MS.

 Dies ist jedoch unerwünscht und einige Nutzer möchten nur die Schriftart dieses spezifischen Zeichens ändern, statt der gesamten Wort- oder Satzschriftart.

 Um dieses Problem zu lösen, stellt Aspose.Cells die Eigenschaft `PdfSaveOptions.isFontSubstitutionCharGranularity` bereit, die auf true gesetzt werden sollte, damit nur die Schriftart der nicht darstellbaren Zeichen in eine darstellbare Schriftart geändert wird, während der Rest des Wortes oder Satzes in der Originalschriftart bleibt.

{{% /alert %}} 

## **Beispiel**
Der folgende Screenshot vergleicht die beiden Ausgabepdf-Dateien, die vom unten stehenden Beispielcode erstellt wurden.

Es gibt ein PDF ohne Einstellung der Eigenschaft `PdfSaveOptions.isFontSubstitutionCharGranularity` und ein anderes, nachdem diese auf true gesetzt wurde.

Wie Sie im ersten PDF sehen können, hat sich die Schriftart des gesamten Satzes von Times New Roman zu Arial Unicode MS geändert, wegen des Nicht-Brechenden Gedankenstrichs. Im zweiten PDF hat sich nur die Schriftart des Nicht-Brechenden Gedankenstrichs geändert.

|**Erste PDF-Datei**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Zweite PDF-Datei**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Beispielcode**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cells
const cell1 = worksheet.getCells().get("A1");
const cell2 = worksheet.getCells().get("B1");

// Set the styles of both cells to Times New Roman
let style = cell1.getStyle();
style.getFont().setName("Times New Roman");
cell1.setStyle(style);
cell2.setStyle(style);

// Put the values inside the cell
cell1.putValue("Hello without Non-Breaking Hyphen");
cell2.putValue("Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen");

// Autofit the columns
worksheet.autoFitColumns();

// Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
workbook.save(path.join(dataDir, "SampleOutput_out.pdf"));

// Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
const opts = new AsposeCells.PdfSaveOptions();
opts.setIsFontSubstitutionCharGranularity(true);
workbook.save(path.join(dataDir, "SampleOutput2_out.pdf"), opts);
```



