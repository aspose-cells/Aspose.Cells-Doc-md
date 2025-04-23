---  
title: Arbeitsblattstruktur mit Node.js über C++ schützen und un保护en  
linktitle: Arbeitsmappenstruktur schützen und entschützen  
type: docs  
weight: 40  
url: /de/nodejs-cpp/protect-and-unprotect-workbook-structure/  
description: Arbeitsblattstruktur von Excel Dateien mit Node.js über C++ schützen und un保护en.  
---  


{{% alert color="primary" %}}  
Um zu verhindern, dass andere Benutzer versteckte Arbeitsblätter einsehen, Arbeitsblätter hinzufügen, verschieben, löschen oder ausblenden und Arbeitsblätter umbenennen, können Sie die Struktur Ihres Excel-Arbeitsblatts mit einem Kennwort schützen.  
{{% /alert %}}  


## **Schützen und entschützen der Arbeitsmappenstruktur in MS Excel**  

**![Arbeitsmappenstruktur schützen und entschützen](schuetzen-und-entschuetzen-arbeitsmappenstruktur.png)**  

1. Klicken Sie auf **Überprüfen > Arbeitsmappe schützen**.  
1. Geben Sie ein Passwort in das **Passwortfeld** ein.  
1. Wählen Sie **OK**, geben Sie das Passwort erneut ein, um es zu bestätigen, und wählen Sie dann erneut **OK**.  


## **Arbeitsblattstruktur mit Aspose.Cells for Node.js via C++ schützen**  
Es sind nur die folgenden einfachen Codezeilen erforderlich, um die Arbeitsmappenstruktur von Excel-Dateien zu schützen.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Protect workbook structure.
workbook.protect(AsposeCells.ProtectionType.Structure, "password");
// Save Excel file.
workbook.save(filePath);
```  

## **Arbeitsblattstruktur mit Aspose.Cells for Node.js via C++ un保护en**  
Die Entschützung der Arbeitsmappenstruktur ist mit der Aspose.Cells API einfach.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open an Excel file which workbook structure is protected.
const workbook = new AsposeCells.Workbook(filePath);
// Unprotect workbook structure.
workbook.unprotect("password");
// Save Excel file.
workbook.save(filePath);
```  

{{% alert color="primary" %}}  
Hinweis: Ein korrektes Passwort ist erforderlich.  
{{% /alert %}}  

