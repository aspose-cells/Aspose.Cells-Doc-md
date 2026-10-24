---
title: Skydda och Hävda skydd
linktitle: Kryptering och skydd
type: docs
weight: 68
url: /sv/net/protect-and-unprotect/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/net/security-features/]
description: Denna sektion introducerar hur man krypterar och dekrypterar Excel-filer och skyddar Excel-data, och täcker filkryptering, skrivskydd, skydd av arbetsboksstruktur, kalkylbladsskydd och digitala signaturer med C#-kod
keywords: Aspose.Cells, .NET, kryptera, dekryptera, lösenord, skydda, ta bort skydd, arbetsboksskydd, kalkylbladsskydd, skrivskydd, digital signatur, C#
---

Excel-arbetsböcker lagrar ofta känslig finansiell, affärsrelaterad eller personlig information som måste skyddas från obehörig åtkomst. Aspose.Cells for .NET erbjuder en omfattande uppsättning skyddsfunktioner som speglar funktionerna i Microsoft Excel, vilket gör att du kan säkra dina data på filnivå, arbetsboksnivå och kalkylbladsnivå.

{{% alert color="primary" %}}
Aspose.Cells for .NET erbjuder ett brett utbud av skyddsfunktioner, från filnivå till datanivå, liknande MS Excel. Dessa funktioner inkluderar kryptering av filer med ett lösenord, tvingande skrivskyddad åtkomst via ett lösenord för att ändra, skydd av arbetsboksstruktur, skydd av kalkylblad och digital signering av arbetsböcker.
{{% /alert %}}

## Kryptera och dekryptera Excel-filer
Ett lösenord som anges för en Excel-fil hindrar obehöriga användare från att öppna eller visa arbetsbokens innehåll. För att kryptera en arbetsbok tilldelar du en lösenordssträng till `Workbook.Settings.Password` och sparar sedan arbetsboken. Aspose.Cells skriver filen i krypterad form. För att öppna en krypterad arbetsbok för dekryptering, instansierar du ett `LoadOptions`-objekt, ställer in `LoadOptions.Password` på samma lösenord som användes vid krypteringen, och skickar det till `Workbook`-konstruktorn. Aspose.Cells tillämpar det angivna lösenordet transparent så att resten av din kod kan interagera med det dekrypterade innehållet som om filen var en vanlig arbetsbok.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cell cell = sheet.Cells["A1"];
cell.PutValue("Confidential Data");
workbook.Settings.Password = "OpenPassword123";
workbook.Save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.Password = "OpenPassword123";
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
Console.WriteLine("Decrypted cell A1 value: " + decryptedWorkbook.Worksheets[0].Cells["A1"].StringValue);
```

## Skrivskydd (lösenord för att ändra)
Excel stöder två distinkta lösenordslager. Det första är ett lösenord för att öppna, vilket krypterar själva filen och behandlas i föregående avsnitt. Det andra är ett lösenord för att ändra, vilket inte blockerar användare från att öppna arbetsboken; istället rekommenderar Excel att filen öppnas i skrivskyddat läge om inte lösenordet för att ändra anges. Konfigurera detta beteende i Aspose.Cells via `Workbook.Settings.WriteProtection`. Ställ in dess `Password`-egenskap till lösenordet för att ändra och dess `Author`-egenskap för att identifiera vem som tillämpade skyddet. Använd metoden `WriteProtection.ValidatePassword(string)` för att kontrollera om ett angivet lösenord för att ändra är korrekt, vilket returnerar `true` vid matchning och `false` annars.

```csharp
using System;
using Aspose.Cells;
// Skapa en ny arbetsbok från grunden
Workbook workbook = new Workbook();
// Skriv ett exempelvärde till cell A1 i det första kalkylbladet
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Data");
// Konfigurera skrivskyddet: ange lösenord för att ändra och författare
workbook.Settings.WriteProtection.Password = "ModifyPwd";
workbook.Settings.WriteProtection.Author = "AuthorName";
// Spara arbetsboken så att skrivskyddet bevaras
workbook.Save("WriteProtectedWorkbook.xlsx");
// Validera lösenordet för att ändra med rätt lösenord
bool isCorrectValid = workbook.Settings.WriteProtection.ValidatePassword("ModifyPwd");
Console.WriteLine("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Validera lösenordet för att ändra med ett felaktigt lösenord för att demonstrera den andra grenen
bool isWrongValid = workbook.Settings.WriteProtection.ValidatePassword("WrongPwd");
Console.WriteLine("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Skydda och ta bort skydd för arbetsboksstruktur
Att skydda arbetsboksstrukturen hindrar andra användare från att visa dolda kalkylblad, lägga till nya kalkylblad, flytta kalkylblad, ta bort kalkylblad, dölja kalkylblad eller byta namn på kalkylblad. Det skyddade tillståndet gäller bladstrukturen snarare än cellinnehållet i något blad. För att tillämpa strukturskydd, anropa `workbook.Protect(ProtectionType.Structure, "password")`. För att ta bort skyddet, anropa `workbook.Unprotect("password")` och ange rätt lösenord. Enum-värdet `ProtectionType.Structure` används här och är skilt från andra skyddstyper som `ProtectionType.Windows`.

```csharp
using System;
using Aspose.Cells;
// Skapa en ny arbetsbok
Workbook workbook = new Workbook();
// Lägg till ett andra kalkylblad
workbook.Worksheets.Add();
// Skriv ett exempelvärde till cell A1 i det första kalkylbladet
workbook.Worksheets[0].Cells[0, 0].PutValue("Sample Data");
// Skydda arbetsbokens struktur
workbook.Protect(ProtectionType.Structure, "StructPwd");
// Spara arbetsboken som structure_protected.xlsx
string filePath = "structure_protected.xlsx";
workbook.Save(filePath);
// Ladda om filen till en ny Workbook-instans
Workbook loadedWorkbook = new Workbook(filePath);
// Ta bort strukturskyddet
loadedWorkbook.Unprotect("StructPwd");
// Skriv ut bekräftelsemeddelande
Console.WriteLine("Structure protection has been successfully removed from the workbook.");
```

## Skydda och ta bort skydd för kalkylblad
Kalkylbladsskydd låser cellerna i ett kalkylblad mot oavsiktliga eller avsiktliga ändringar. Användare kan inte redigera låsta celler utan att ange lösenordet. Detta är det typiska skyddet som används för att skydda formler, rubriker eller angivna dataregistreringsområden i delade kalkylblad. För att skydda ett kalkylblad, anropa `worksheet.Protect(ProtectionType.All, "password")`. Att använda `ProtectionType.All` aktiverar alla tillgängliga skyddsalternativ som att välja låsta celler, formatera celler, infoga rader och kolumner samt ta bort rader och kolumner. För att ta bort skyddet, anropa `worksheet.Unprotect("password")` med rätt lösenord. Finkornigare kontroll är tillgänglig genom att kombinera andra skyddstyper som `Contents`, `Objects` och `Scenarios` med bitvis OR.

```csharp
using System;
using Aspose.Cells;
var workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
sheet.Cells["A1"].PutValue("Sample Data");
sheet.Protect(ProtectionType.All, "SheetPwd");
workbook.Save("sheet_protected.xlsx");
var workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.Worksheets[0];
sheetReloaded.Unprotect("SheetPwd");
Console.WriteLine("Worksheet protection removed successfully.");
```

## Lägg till och validera digitala signaturer
En digital signatur försäkrar mottagarna om att arbetsbokens innehåll är autentiskt och inte har ändrats sedan det signerades. Aspose.Cells erbjuder stöd för digitala signaturer via namnrymden `Aspose.Cells.DigitalSignatures`. Det typiska arbetsflödet läser in en `.pfx`-certifikatfil via `System.Security.Cryptography.X509Certificates.X509Certificate2`, omsluter den i en `Aspose.Cells.DigitalSignatures.DigitalSignature`, lägger till signaturen i en `DigitalSignatureCollection` och tillämpar samlingen på arbetsboken via `Workbook.AddDigitalSignature(DigitalSignatureCollection)`. Egenskapen `DigitalSignature.Comments` kan registrera signeringskontext som signeringstid och syfte. Alla ändringar som görs i arbetsboken efter signeringen ogiltigförklarar signaturen, så ett valideringssteg på mottagarsidan kan upptäcka manipulering.

```csharp
using System;
using System.IO;
using System.Security.Cryptography.X509Certificates;
using Aspose.Cells;
using Aspose.Cells.DigitalSignatures;
X509Certificate2 certificate = new X509Certificate2("signature.pfx", "pfx-password");
DigitalSignature signature = new DigitalSignature(certificate, "Signed by Aspose.Cells", DateTime.Now);
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.Add(signature);
Workbook workbook = new Workbook();
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Value");
workbook.AddDigitalSignature(signatures);
workbook.Save("signed_workbook.xlsx");
Console.WriteLine("The workbook has been digitally signed.");
```

## Relaterade artiklar
- [Kryptera och dekryptera Excel-filer](/cells/sv/net/encrypt-and-decrypt-excel-files/)
- [Skydda och ta bort skydd för arbetsboksstruktur](/cells/sv/net/protect-and-unprotect-workbook-structure/)
- [Skydda och ta bort skydd för kalkylblad](/cells/sv/net/protect-and-unprotect-worksheets/)
- [Lösenordsskydda eller ta bort skyddet för den delade arbetsboken](/cells/sv/net/password-protect-or-unprotect-the-shared-workbook/)
- [Tilldela och validera digitala signaturer](/cells/sv/net/assign-and-validate-digital-signatures/)
- [Kontrollera lösenord för att ändra med Aspose.Cells](/cells/sv/net/check-password-to-modify-using-aspose-cells/)
- [Identifiera filformat för krypterade Office Open XML - OOXML-filer](/cells/sv/net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Kryptering av Excel-filer](/cells/sv/net/encrypting-excel-files/)
- [Hur man identifierar ett filformat och kontrollerar om filen är krypterad](/cells/sv/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="csharp" >}}