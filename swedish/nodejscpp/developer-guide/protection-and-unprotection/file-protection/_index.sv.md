---  
title: Kryptera och dekryptera Excel filer med Node.js via C++  
linktitle: Kryptera och dekryptera Excel filer  
type: docs  
weight: 10  
url: /sv/nodejs-cpp/encrypt-and-decrypt-excel-files/  
description: Hur man krypterar och dekrypterar Excel filer med Node.js via C++. Lås och lås upp Excel filer.  
---  

{{% alert color="primary" %}}  
Microsoft Excel (97 - 365) gör det möjligt för dig att kryptera och lösenordsskydda dina kalkylblad. Det använder algoritmer som tillhandahålls av en kryptografisk tjänsteleverantör, eller CSP, en uppsättning krypteringsalgoritmer med olika egenskaper. Standard-CSP är 'Kontors 97/2000-kompatibel' eller 'Svag kryptering (XOR)'. Det är viktigt att välja rätt krypteringsnyckellängd. Vissa CSP:er stöder inte mer än 40 eller 56 bitar. Det anses vara svag kryptering. För stark kryptering krävs en minsta nyckellängd på 128 bitar. Microsoft Windows innehåller också CSP:er som erbjuder starka krypteringstyper, till exempel 'Microsoft Strong Cryptographic Provider'. För att ge dig en uppfattning, 128 bitar kryptering är vad banker använder för att kryptera anslutningen med sina internetbankssystem.  

Aspose.Cells gör det möjligt för dig att kryptera och lösenordsskydda Microsoft Excel-filer med önskad krypteringstyp.  
{{% /alert %}}  

## **Använda Microsoft Excel**  

För att ställa in filkrypteringsinställningar i Microsoft Excel (här Microsoft Excel 2003):  

1. Från menyn **Verktyg**, välj **Alternativ**. En dialogruta kommer att visas.  
2. Välj fliken **Säkerhet**.  
3. Skriv in ett lösenord och klicka på **Avancerat**  
4. Välj krypteringstyp och bekräfta lösenordet.  

## **Kryptera Excel-fil med Aspose.Cells for Node.js via C++**  

Följande exempel visar hur man krypterar och lösenordsskyddar en Excel-fil med Aspose.Cells API.  

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

### **Anger Lösenord för att ändra alternativ**  

Följande exempel visar hur man ställer in alternativet **Lösenord för att ändra** i Microsoft Excel för en befintlig fil med hjälp av Aspose.Cells API.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```  


## **Dekryptera Excel-fil med Aspose.Cells for Node.js via C++**  
Det är mycket enkelt att öppna en lösenordsskyddad Excel-fil och dekryptera den med Aspose.Cells API som visas i följande kod:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open encrypted file with password.
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("password");
const workbook = new AsposeCells.Workbook(filePath, loadOptions);

// Remove password.
workbook.getSettings().setPassword(null);

// Save the file.
workbook.save(filePath);
```  


## **Fortsatta ämnen**  
- [Kryptera och dekryptera ODS-filer](/cells/sv/nodejs-cpp/encrypt-and-decrypt-ods-files/)  
- [Ange stark krypterings typ](/cells/sv/nodejs-cpp/setting-strong-encryption-type/)  
- [Ange författare vid skrivskydd av arbetsbok](/cells/sv/nodejs-cpp/specify-author-while-write-protecting-workbook/)  
- [Verifiera lösenord för krypterade filer](/cells/sv/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
