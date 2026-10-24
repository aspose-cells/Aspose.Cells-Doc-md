---
title: Skydda och avsäkra med Node.js via C++
linktitle: Kryptering och skydd
description: Det här avsnittet introducerar hur du krypterar och dekrypterar Excel-filer och skyddar Excel-data, och täcker filkryptering, skrivskydd, skydd av arbetsbokens struktur, skydd av kalkylblad och digitala signaturer med JavaScript-kod
keywords: Aspose.Cells, Node.js, C++, kryptera, dekryptera, lösenord, skydda, ta bort skydd, arbetsboksskydd, kalkylbladsskydd, skrivskydd, digital signatur, JavaScript
type: docs
weight: 68
url: /sv/nodejs-cpp/protect-and-unprotect/
alias: [/nodejs-cpp/security-features/]
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-arbetsböcker lagrar ofta känslig finansiell, affärsrelaterad eller personlig information som måste skyddas mot obehörig åtkomst. Aspose.Cells for Node.js via C++ tillhandahåller en omfattande uppsättning skyddsfunktioner som speglar funktionerna i Microsoft Excel, så att du kan säkra dina data på filnivå, arbetsboksnivå och kalkylbladsnivå.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ erbjuder ett brett utbud av skyddsfunktioner, från filnivå till datanivå, som liknar MS Excel. Funktionerna omfattar att kryptera filer med ett lösenord, tillämpa skrivskydd via ett lösenord för att ändra, skydda arbetsbokens struktur, skydda kalkylblad och signera arbetsböcker digitalt.
{{% /alert %}}

## Kryptera och dekryptera Excel-filer
Ett lösenord som anges för en Excel-fil hindrar obehöriga användare från att öppna eller visa innehållet i arbetsboken. Om du vill kryptera en arbetsbok tilldelar du en lösenordssträng till `workbook.getSettings().setPassword()` och sparar sedan arbetsboken. Aspose.Cells skriver filen i krypterad form. Om du vill öppna en krypterad arbetsbok för dekryptering instansierar du ett `LoadOptions`-objekt, anger samma lösenord som användes vid kryptering i `loadOptions.setPassword()` och skickar det till `Workbook`-konstruktorn. Aspose.Cells tillämpar det angivna lösenordet automatiskt så att resten av koden kan arbeta med det dekrypterade innehållet som om filen vore en vanlig arbetsbok.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
let loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("OpenPassword123");
let decryptedWorkbook = new AsposeCells.Workbook("encrypted.xlsx", loadOptions);
console.log("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## Skrivskydd (lösenord för att ändra)
Excel stöder två olika lösenordsnivåer. Den första är ett lösenord för att öppna filen, vilket krypterar själva filen och behandlas i föregående avsnitt. Den andra är ett lösenord för att ändra, vilket inte hindrar användare från att öppna arbetsboken. Excel rekommenderar i stället att filen öppnas i skrivskyddat läge om inte lösenordet för att ändra anges. Du konfigurerar detta beteende i Aspose.Cells med `workbook.getSettings().getWriteProtection()`. Ange egenskapen `password` till lösenordet för att ändra och egenskapen `author` till den person som har tillämpat skyddet. Använd metoden `writeProtection.validatePassword(string)` för att kontrollera om ett angivet lösenord för att ändra är korrekt. Den returnerar `true` vid matchning och `false` annars.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// Skriv ett exempelvärde till cell A1 i det första kalkylbladet
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
// Konfigurera skrivskyddet: ange lösenordet för att ändra och författaren
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
// Spara arbetsboken så att skrivskyddet sparas
workbook.save("WriteProtectedWorkbook.xlsx");
// Validera lösenordet för att ändra med rätt lösenord
let isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
console.log("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Validera lösenordet för att ändra med felaktigt lösenord för att demonstrera den andra grenen
let isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
console.log("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Skydda arbetsbokens struktur och ta bort skyddet
Att skydda arbetsbokens struktur hindrar andra användare från att visa dolda kalkylblad, lägga till nya kalkylblad, flytta kalkylblad, ta bort kalkylblad, dölja kalkylblad eller byta namn på kalkylblad. Det skyddade tillståndet gäller kalkylbladens struktur och inte cellinnehållet i något enskilt kalkylblad. Om du vill tillämpa strukturskydd anropar du `workbook.protect(ProtectionType.Structure, "password")`. Om du vill ta bort skyddet anropar du `workbook.unprotect("password")` och anger rätt lösenord. Enumerationsvärdet `ProtectionType.Structure` används här och är skilt från andra skyddstyper som `ProtectionType.Windows`.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// Lägg till ett andra kalkylblad
workbook.getWorksheets().add();
// Skriv ett exempelvärde till cell A1 i det första kalkylbladet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Skydda arbetsbokens struktur
workbook.protect(AsposeCells.ProtectionType.Structure, "StructPwd");
// Spara arbetsboken som structure_protected.xlsx
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Ladda om filen till en ny Workbook-instans
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// Ta bort strukturskyddet
loadedWorkbook.unprotect("StructPwd");
// Skriv ut bekräftelsemeddelande
console.log("Structure protection has been successfully removed from the workbook.");
```

## Skydda kalkylblad och ta bort skyddet
Kalkylbladsskydd låser cellerna i ett kalkylblad så att de inte kan ändras oavsiktligt eller avsiktligt. Användare kan inte redigera låsta celler utan att ange lösenordet. Detta är det vanliga skyddet som används för att skydda formler, rubriker eller utvalda områden för datainmatning i delade kalkylblad. Om du vill skydda ett kalkylblad anropar du `worksheet.protect(ProtectionType.All, "password")`. Om du använder `ProtectionType.All` aktiveras alla tillgängliga skyddsalternativ, till exempel att välja låsta celler, formatera celler, infoga rader och kolumner samt ta bort rader och kolumner. Om du vill ta bort skyddet anropar du `worksheet.unprotect("password")` med rätt lösenord. Mer detaljerad kontroll är tillgänglig genom att kombinera andra skyddstyper som `Contents`, `Objects` och `Scenarios` med bitvis OR.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.All, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## Lägg till och validera digitala signaturer
En digital signatur intygar för mottagarna att innehållet i arbetsboken är autentiskt och inte har ändrats sedan det signerades. Aspose.Cells erbjuder stöd för digitala signaturer via namnrymden `Aspose.Cells.DigitalSignatures`. Det vanliga arbetsflödet är att läsa in en `.pfx`-certifikatfil med hjälp av kryptografiska verktyg i Node.js, omsluta den i en `Aspose.Cells.DigitalSignatures.DigitalSignature`, lägga till signaturen i en `DigitalSignatureCollection` och tillämpa samlingen på arbetsboken med `workbook.addDigitalSignature(digitalSignatureCollection)`. Egenskapen `digitalSignature.comments` kan användas för att dokumentera signeringssammanhang, till exempel tidpunkt och syfte med signeringen. Alla ändringar som görs i arbetsboken efter signeringen gör signaturen ogiltig, så ett valideringssteg på mottagarsidan kan upptäcka manipulering.

```javascript
const AsposeCells = require("aspose.cells.node");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

## Relaterade artiklar
- [Kryptera och dekryptera Excel-filer](/cells/sv/nodejs-cpp/encrypt-and-decrypt-excel-files/)
- [Skydda arbetsbokens struktur och ta bort skyddet](/cells/sv/nodejs-cpp/protect-and-unprotect-workbook-structure/)
- [Skydda och ta bort skydd för kalkylblad](/cells/sv/nodejs-cpp/protect-and-unprotect-worksheets/)
- [Skydda den delade arbetsboken med lösenord eller ta bort skyddet](/cells/sv/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/)
- [Tilldela och validera digitala signaturer](/cells/sv/nodejs-cpp/assign-and-validate-digital-signatures/)
- [Kontrollera lösenord för att ändra med Aspose.Cells](/cells/sv/nodejs-cpp/check-password-to-modify-using-aspose-cells/)
- [Identifiera filformat för krypterade Office Open XML - OOXML-filer](/cells/sv/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Kryptering av Excel-filer](/cells/sv/nodejs-cpp/encrypting-excel-files/)
- [Hur du identifierar ett filformat och kontrollerar om filen är krypterad](/cells/sv/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="nodejs-cpp" >}}