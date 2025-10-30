---
title: Kryptera Excel filer med Node.js via C++
linktitle: Kryptering av Excel filer
type: docs
weight: 90
url: /sv/nodejs-cpp/encrypting-excel-files/
description: Lär dig hur du krypterar och lösenordsskyddar Excel filer med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) gör det möjligt för dig att kryptera och lösenordsskydda dina kalkylblad. Det använder algoritmer som tillhandahålls av en kryptografisk tjänsteleverantör, eller CSP, en uppsättning krypteringsalgoritmer med olika egenskaper. Standard-CSP är 'Kontors 97/2000-kompatibel' eller 'Svag kryptering (XOR)'. Det är viktigt att välja rätt krypteringsnyckellängd. Vissa CSP:er stöder inte mer än 40 eller 56 bitar. Det anses vara svag kryptering. För stark kryptering krävs en minsta nyckellängd på 128 bitar. Microsoft Windows innehåller också CSP:er som erbjuder starka krypteringstyper, till exempel 'Microsoft Strong Cryptographic Provider'. För att ge dig en uppfattning, 128 bitar kryptering är vad banker använder för att kryptera anslutningen med sina internetbankssystem.

Aspose.Cells gör det möjligt för dig att kryptera och lösenordsskydda Microsoft Excel-filer med önskad krypteringstyp.

{{% /alert %}}

## **Använda Microsoft Excel**

För att ställa in filkrypteringsinställningar i Microsoft Excel (här Microsoft Excel 2003):

1. Från menyn **Verktyg**, välj **Alternativ**. En dialogruta kommer att visas.
1. Välj fliken **Säkerhet**.
1. Ange ett lösenord och klicka på **Avancerat**
1. Välj krypteringstyp och bekräfta lösenordet.

## **Kryptering med Aspose.Cells for Node.js via C++**

Exemplet nedan visar hur man krypterar och lösenordsskyddar en Excel-fil med hjälp av Aspose.Cells API.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Specify XOR encryption type.
workbook.setEncryptionOptions(AsposeCells.EncryptionType.XOR, 40);

// Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);

// Password protect the file.
workbook.getSettings().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```

### **Ange lösenord för att ändra alternativ**

Följande exempel visar hur man ställer in alternativet **Lösenord för att ändra** i Microsoft Excel för en befintlig fil med hjälp av Aspose.Cells API.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```

## **Verifiera lösenordet för den krypterade filen**

För att verifiera lösenordet för den krypterade filen erbjuder Aspose.Cells for Node.js via C++ metoden [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-). Dessa metoder tar emot två parametrar, filströmmen och lösenordet som ska verifieras.
Följande kodavsnitt demonstrerar användningen av metod [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) för att verifiera om det angivna lösenordet är giltigt eller inte.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "EncryptedBook1.xlsx");

// Create a Stream object
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

const isPasswordValid = AsposeCells.FileFormatUtil.verifyPassword(fstream, "1234");

console.log("Password is Valid: " + isPasswordValid);
```

## **Kryptering/Dekryptering av ODS-fil med Aspose.Cells**

Aspose.Cells tillåter kryptering och dekryptering av ODS-filer. Den dekrypterade ODS-filen kan öppnas i både Excel och OpenOffice, medan den krypterade ODS-filen endast kan öppnas i OpenOffice efter att ha angett lösenordet. Excel kan inte öppna den krypterade ODS-filen och kan visa en varning. Krypteringsalternativen är inte tillämpliga för ODS-filer jämfört med andra filtyper. För att kryptera en ODS-fil, ladda filen och ställ in [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) till det faktiska lösenordet innan du sparar den. Den krypterade ODS-filen kan öppnas i OpenOffice endast.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = RunExamples.Get_SourceDirectory();
// Output directory
const outputDir = RunExamples.Get_OutputDirectory();

// Open an ODS file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleODSFile.ods"));

// Password protect the file
workbook.getSettings().setPassword("1234");

// Save the ODS file
workbook.save(path.join(outputDir, "outputEncryptedODSFile.ods"));
```

För att dekryptera en ODS-fil, ladda in filen genom att ange ett lösenord i [**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--). När filen har laddats, ställ in strängen för [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) till null.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

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
