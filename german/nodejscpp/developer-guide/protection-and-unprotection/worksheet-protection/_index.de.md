---  
title: Arbeitsblatt mit Node.js über C++ schützen und un保护en  
linktitle: Arbeitsblatt schützen und entschützen  
type: docs  
weight: 40  
url: /de/nodejs-cpp/protect-and-unprotect-worksheets/  
description: Arbeitsblatt von Excel Dateien mit Aspose.Cells for Node.js via C++ schützen und un保护en.  
---  

{{% alert color="primary" %}}  
Um zu verhindern, dass andere Benutzer versehentlich oder absichtlich Daten in einem Arbeitsblatt ändern, verschieben oder löschen, können Sie die Zellen in Ihrem Excel-Arbeitsblatt sperren und das Blatt dann mit einem Kennwort schützen.  
{{% /alert %}}  

## **Arbeitsblatt in MS Excel schützen und aufheben**  

**![Arbeitsblatt schützen und aufheben](schuetzen-und-aufheben.png)**  

1. Klicken Sie auf **Überprüfen > Arbeitsblatt schützen**.  
1. Geben Sie ein Passwort in das **Passwortfeld** ein.  
1. Wählen Sie die **Zulassen**-Optionen aus.  
1. Wählen Sie **OK**, geben Sie das Passwort erneut ein, um es zu bestätigen, und wählen Sie dann erneut **OK**.  

## **Arbeitsblatt mit Aspose.Cells for Node.js via C++ schützen.**  
Es sind nur die folgenden einfachen Codezeilen erforderlich, um die Arbeitsmappenstruktur von Excel-Dateien zu schützen.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.protect(AsposeCells.ProtectionType.Contents);
// Protect worksheet with password.
sheet.getProtection().setPassword("test");
// Save as Excel file.
workbook.save("Book1.xlsx");
```  

## **Arbeitsblatt mit Aspose.Cells for Node.js via C++ un保护en.**  
Das Entschutz des Arbeitsblatts ist einfach mit Aspose.Cells API. Wenn das Arbeitsblatt kennwortgeschützt ist, wird ein korrektes Passwort benötigt.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook(filePath);
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.unprotect("password");
// Save Excel file.
workbook.save("Book1.xlsx");
```  

## **Erweiterte Themen**  
- [Erweiterte Schutzeinstellungen seit Excel XP](/cells/de/nodejs-cpp/advanced-protection-settings-since-excel-xp/)  
- [Überprüfen Sie, ob das Arbeitsblatt mit einem Kennwort geschützt ist](/cells/de/nodejs-cpp/detect-if-worksheet-is-password-protected/)  
- [Arbeitsblätter schützen](/cells/de/nodejs-cpp/protecting-worksheets/)  
- [Arbeitsblatt entsperren](/cells/de/nodejs-cpp/unprotect-a-worksheet/)  
- [Überprüfen Sie das verwendete Kennwort zum Schutz des Arbeitsblatts](/cells/de/nodejs-cpp/verify-password-used-to-protect-the-worksheet/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
