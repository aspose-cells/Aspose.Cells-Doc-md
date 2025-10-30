---  
title: Passwortschutz für das VBA Projekt der Excel Arbeitsmappe mit Node.js via C++  
linktitle: Schützen Sie das VBA Projekt der Excel Arbeitsmappe mit einem Passwort  
type: docs  
weight: 10  
url: /de/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/  
description: Erfahren Sie, wie Sie das VBA Projekt einer Excel Arbeitsmappe mit Aspose.Cells for Node.js via C++ mit Passwort schützen.  
---  

## **Passwortschutz für das VBA-Projekt der Excel-Arbeitsmappe in Node.js**  

Sie können das VBA (Visual Basic for Applications)-Projekt einer Arbeitsmappe mit Aspose.Cells mit [**VbaProject.protect(boolean, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#protect-boolean-string-)-Methode passwortschützen.  

## **Beispielcode**  

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](43352067.xlsm), greift auf ihr VBA-Projekt zu, schützt es mit einem Passwort und speichert es schließlich als [Ausgabedatei](43352068.xlsm).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "samplePasswordProtectVBAProject.xlsm"));

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Lock the VBA project for viewing with password.
vbaProject.protect(true, "11");

// Save the output Excel file
workbook.save(path.join(dataDir, "outputPasswordProtectVBAProject.xlsm"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
