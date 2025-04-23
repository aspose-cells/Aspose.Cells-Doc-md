---  
title: Autor beim Schriftsschutz des Arbeitsblatts mit Node.js über C++ angeben  
linktitle: Autor beim Schreibschutz des Arbeitsmappenschreibens spezifizieren  
type: docs  
weight: 40  
url: /de/nodejs-cpp/specify-author-while-write-protecting-workbook/  
description: Geben Sie einen Autorennamen an, während Sie mit Aspose.Cells for Node.js via C++ ein Arbeitsblatt schützen.  
---  

## **Mögliche Verwendungsszenarien**

Sie können beim Schutz Ihres Arbeitsblatts mit Aspose.Cells API einen Autorennamen angeben. Bitte verwenden Sie dazu die Eigenschaft [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--).

## **Autor beim Schreibschutz des Arbeitsmappenschreibens spezifizieren**

Der folgende Beispielcode zeigt die Verwendung der Eigenschaft [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--). Der Code erstellt ein leeres Arbeitsbuch, schützt es mit einem Passwort, gibt den Autorennamen an und speichert es als [Ausgabedatei Excel](67338582.xlsx). Die folgende Bildschirmaufnahme zeigt den Effekt des Beispielcodes auf die Ausgabedatei Excel zu Ihrer Referenz.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Create empty workbook.
const workbook = new AsposeCells.Workbook();

// Write protect workbook with password.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Specify author while write protecting workbook.
workbook.getSettings().getWriteProtection().setAuthor("SimonAspose");

// Save the workbook in XLSX format.
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx"));
```  

