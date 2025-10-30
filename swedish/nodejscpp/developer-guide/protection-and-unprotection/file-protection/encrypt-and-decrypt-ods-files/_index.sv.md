---
title: Kryptera och dekryptera ODS filer med Node.js via C++
linktitle: Kryptera och dekryptera ODS filer
type: docs
weight: 10
url: /sv/nodejs-cpp/encrypt-and-decrypt-ods-files/
description: Lösenordsskydda och kryptera ODS filer med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}
 OpenOffice.org är en komplett kontorssvit som stöder lösenordsskydd och kryptering av filer. En krypterad ODS-fil kan dock endast öppnas av OpenOffice efter att ha angett lösenordet. Excel kan inte öppna den krypterade ODS-filen och kan visa varningsmeddelanden. Krypteringsalternativen är inte tillämpliga för ODS-filer till skillnad från andra filtyper. 
Aspose.Cells låter dig kryptera och dekryptera ODS-filer. Dekrypterade ODS-filer kan öppnas både i Excel och OpenOffice.
{{% /alert %}}

## **Kryptera med OpenOffice Calc**
1. Välj **Spara som** och klicka på **Spara med lösenord** rutan.
1. Klicka på **Spara**-knappen.
1. Skriv ditt önskade lösenord i både **Ange lösenord för att öppna** och **Bekräfta lösenord**-fälten i dialogrutan Ange lösenord som öppnas. 
1. Klicka på **OK**-knappen för att spara filen.

## **Kryptera ODS-fil med Aspose.Cells for Node.js via C++**
För att kryptera en ODS-fil, ladda filen och sätt [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--)-värdet till det faktiska lösenordet innan du sparar den. Den krypterade ODS-filen kan öppnas i OpenOffice endast.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "source");
const outputDir = path.join(__dirname, "output");

// Open an ODS file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleODSFile.ods"));

// Password protect the file
workbook.getSettings().setPassword("1234");

// Save the ODS file
workbook.save(path.join(outputDir, "outputEncryptedODSFile.ods"));
```

## **Dekryptera ODS-fil med Aspose.Cells for Node.js via C++**
För att dekryptera en ODS-fil, ladda filen genom att ange ett lösenord i [**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--). När filen är laddad, sätt [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--)-strängen till null.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open an encrypted ODS file
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Ods);

// Set original password
loadOptions.setPassword("1234");

// Load the encrypted ODS file with the appropriate load options
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleEncryptedODSFile.ods"), loadOptions);

// Set the password to null
workbook.getSettings().setPassword(null);

// Save the decrypted ODS file
workbook.save(outputDir + "outputDecryptedODSFile.ods");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
