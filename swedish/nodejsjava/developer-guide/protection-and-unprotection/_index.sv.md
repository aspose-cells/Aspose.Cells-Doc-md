---
title: Skydda och Hävda skydd
linktitle: Kryptering och skydd
description: Denna sektion introducerar hur man krypterar och dekrypterar Excel-filer och skyddar Excel-data, och täcker filkryptering, skrivskydd, skydd av arbetsboksstruktur, kalkylbladsskydd och digitala signaturer med JavaScript-kod
keywords: Aspose.Cells, Node.js via Java, kryptera, dekryptera, lösenord, skydda, ta bort skydd, arbetsboksskydd, kalkylbladsskydd, skrivskydd, digital signatur, JavaScript
type: docs
weight: 68
url: /sv/nodejs-java/protect-and-unprotect/
alias: [/nodejs-java/security-features/]
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-arbetsböcker lagrar ofta känslig ekonomisk, affärs- eller personlig information som måste skyddas mot obehörig åtkomst. Aspose.Cells for Node.js via Java erbjuder en omfattande uppsättning skyddsfunktioner som speglar funktionerna i Microsoft Excel, vilket gör att du kan säkra dina data på filnivå, arbetsboksnivå och kalkylbladsnivå.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java erbjuder ett brett utbud av skyddsfunktioner, från filnivå till datanivå, liknande MS Excel. Dessa funktioner inkluderar kryptering av filer med ett lösenord, tvingande skrivskyddad åtkomst genom ett lösenord för att ändra, skydd av arbetsboksstruktur, skydd av kalkylblad och digital signering av arbetsböcker.
{{% /alert %}}

## Kryptera och dekryptera Excel-filer
Ett lösenord som anges för en Excel-fil förhindrar obehöriga användare från att öppna eller visa arbetsbokens innehåll. För att kryptera en arbetsbok, tilldela en lösenordssträng till `workbook.getSettings().setPassword(...)` och spara sedan arbetsboken. Aspose.Cells skriver filen i krypterad form. För att öppna en krypterad arbetsbok för dekryptering, instansiera ett `LoadOptions`-objekt, ange `loadOptions.setPassword(...)` till samma lösenord som användes vid krypteringen, och skicka det till `Workbook`-konstruktorn. Aspose.Cells tillämpar det angivna lösenordet transparent så att resten av din kod kan interagera med det dekrypterade innehållet som om filen vore en vanlig arbetsbok.

```javascript
const AsposeCells = require("aspose.cells");
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
Excel stöder två distinkta lösenordslager. Det första är ett lösenord för att öppna, vilket krypterar själva filen och täcks i föregående avsnitt. Det andra är ett lösenord för att ändra, vilket inte blockerar användare från att öppna arbetsboken; istället rekommenderar Excel att filen öppnas i skrivskyddat läge om inte lösenordet för att ändra anges. Konfigurera detta beteende i Aspose.Cells genom `workbook.getSettings().getWriteProtection()`. Ange dess `Password`-egenskap till lösenordet för att ändra och dess `Author`-egenskap för att identifiera vem som tillämpade skyddet. Använd metoden `writeProtection.validatePassword(string)` för att kontrollera om ett angivet lösenord för att ändra är korrekt, vilket returnerar `true` vid matchning och `false` annars.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// Skriv ett exempelvärde till cell A1 i det första kalkylbladet
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
// Konfigurera skrivskyddet: ange lösenordet för att ändra och författaren
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
// Spara arbetsboken så att skrivskyddet bevaras
workbook.save("WriteProtectedWorkbook.xlsx");
// Validera lösenordet för att ändra med det korrekta lösenordet
let isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
console.log("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Validera lösenordet för att ändra med ett felaktigt lösenord för att demonstrera den andra grenen
let isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
console.log("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Skydda och ta bort skydd för arbetsboksstruktur
Att skydda arbetsboksstrukturen förhindrar andra användare från att visa dolda kalkylblad, lägga till nya kalkylblad, flytta kalkylblad, ta bort kalkylblad, dölja kalkylblad eller byta namn på kalkylblad. Det skyddade tillståndet gäller bladstrukturen snarare än cellinnehållet i något blad. För att tillämpa strukturskydd, anropa `workbook.protect(ProtectionType.Structure, "password")`. För att ta bort skyddet, anropa `workbook.unprotect("password")` och ange rätt lösenord. Enumvärdet `ProtectionType.Structure` används här och är skiljt från andra skyddstyper såsom `ProtectionType.Windows`.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// Lägg till ett andra kalkylblad
workbook.getWorksheets().add();
// Skriv ett exempelvärde till cell A1 i det första kalkylbladet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Skydda arbetsbokens struktur
workbook.protect(AsposeCells.ProtectionType.STRUCTURE, "StructPwd");
// Spara arbetsboken som structure_protected.xlsx
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Ladda om filen till en ny arbetsboksinstans
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// Ta bort struktskyddet
loadedWorkbook.unprotect("StructPwd");
// Skriv ut bekräftelsemeddelande
console.log("Structure protection has been successfully removed from the workbook.");
```

## Skydda och ta bort skydd för kalkylblad
Kalkylbladsskydd låser cellerna i ett kalkylblad mot oavsiktliga eller avsiktliga ändringar. Användare kan inte redigera låsta celler utan att ange lösenordet. Detta är det typiska skyddet som används för att skydda formler, rubriker eller avsedda dataregistreringsområden i delade kalkylblad. För att skydda ett kalkylblad, anropa `worksheet.protect(ProtectionType.All, "password")`. Att använda `ProtectionType.All` aktiverar alla tillgängliga skyddsalternativ såsom att välja låsta celler, formatera celler, infoga rader och kolumner samt ta bort rader och kolumner. För att ta bort skyddet, anropa `worksheet.unprotect("password")` med rätt lösenord. Finkornigare kontroll är tillgänglig genom att kombinera andra skyddstyper såsom `Contents`, `Objects` och `Scenarios` med bitvis OR.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.ALL, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## Lägg till och validera digitala signaturer
En digital signatur försäkrar mottagarna om att arbetsbokens innehåll är autentiskt och inte har ändrats sedan det signerades. Aspose.Cells stöder digitala signaturer via klasser som `AsposeCells.DigitalSignature` och `AsposeCells.DigitalSignatureCollection`. Det typiska arbetsflödet skapar en `AsposeCells.DigitalSignature` direkt från en `.pfx`-certifikatfil tillsammans med dess lösenord och signeringskommentarer, lägger till signaturen i en `DigitalSignatureCollection` och tillämpar samlingen på arbetsboken via `workbook.addDigitalSignature(DigitalSignatureCollection)`. Egenskapen `DigitalSignature.Comments` kan registrera signeringskontext såsom signeringstid och syfte. Alla ändringar som görs i arbetsboken efter signeringen ogiltigförklarar signaturen, så ett valideringssteg på mottagarsidan kan upptäcka manipulering.

```javascript
const AsposeCells = require("aspose.cells");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

{{< app/cells/assistant language="nodejs-java" >}}