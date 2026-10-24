---
title: Skydda och Hävda skydd
linktitle: Kryptering och skydd
description: Det här avsnittet beskriver hur man krypterar och dekrypterar Excel-filer samt skyddar Excel-data, inklusive filkryptering, skrivskydd, skydd av arbetsboksstruktur, kalkylbladsskydd och digitala signaturer med Python-kod
keywords: Aspose.Cells, Python via .NET, kryptera, dekryptera, lösenord, skydda, ta bort skydd, arbetsboksskydd, kalkylbladsskydd, skrivskydd, digital signatur, Python
type: docs
weight: 68
url: /sv/python-net/protect-and-unprotect/
alias: [/python-net/security-features/]
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-arbetsböcker innehåller ofta känslig finansiell, affärsrelaterad eller personlig information som måste skyddas mot obehörig åtkomst. Aspose.Cells for Python via .NET erbjuder en omfattande uppsättning skyddsfunktioner som speglar funktionerna i Microsoft Excel, vilket gör att du kan säkra dina data på filnivå, arbetsboksnivå och kalkylbladsnivå.

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET erbjuder ett brett utbud av skyddsfunktioner, från filnivå till datanivå, i likhet med MS Excel. Dessa funktioner inkluderar kryptering av filer med lösenord, tvingande skrivskyddad åtkomst via ett lösenord för att ändra, skydd av arbetsboksstruktur, skydd av kalkylblad och digital signering av arbetsböcker.
{{% /alert %}}

## Kryptera och dekryptera Excel-filer
Ett lösenord som anges på en Excel-fil hindrar obehöriga användare från att öppna eller visa arbetsbokens innehåll. För att kryptera en arbetsbok, tilldela en lösenordssträng till `workbook.settings.password` och spara sedan arbetsboken. Aspose.Cells skriver filen i krypterad form. För att öppna en krypterad arbetsbok för dekryptering, instansiera ett `LoadOptions`-objekt, sätt `load_options.password` till samma lösenord som användes vid krypteringen, och skicka det till `Workbook`-konstruktorn. Aspose.Cells tillämpar det angivna lösenordet transparent så att resten av din kod kan interagera med det dekrypterade innehållet som om filen var en vanlig arbetsbok.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cell = sheet.cells.get("A1")
cell.put_value("Confidential Data")
workbook.settings.password = "OpenPassword123"
workbook.save("encrypted.xlsx")
load_options = ac.LoadOptions()
load_options.password = "OpenPassword123"
decrypted_workbook = ac.Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.worksheets[0].cells.get("A1").string_value)
```

## Skrivskydd (lösenord för att ändra)
Excel stöder två distinkta lösenordslager. Det första är ett lösenord för att öppna, vilket krypterar själva filen och som tas upp i föregående avsnitt. Det andra är ett lösenord för att ändra, vilket inte blockerar användare från att öppna arbetsboken; istället rekommenderar Excel att filen öppnas i skrivskyddat läge om inte lösenordet för att ändra anges. Konfigurera detta beteende i Aspose.Cells via `workbook.settings.write_protection`. Sätt dess `password`-egenskap till lösenordet för att ändra och dess `author`-egenskap för att identifiera vem som tillämpade skyddet. Använd metoden `write_protection.validate_password(string)` för att kontrollera om ett angivet lösenord för att ändra är korrekt, vilket returnerar `true` vid matchning och `false` annars.

```python
import aspose.cells as ac
# Skapa en ny arbetsbok från grunden
workbook = ac.Workbook()
# Skriv ett exempelvärde till cell A1 i det första kalkylbladet
workbook.worksheets[0].cells.get("A1").put_value("Sample Data")
# Konfigurera skrivskyddet: ange lösenordet för att ändra och författaren
workbook.settings.write_protection.password = "ModifyPwd"
workbook.settings.write_protection.author = "AuthorName"
# Spara arbetsboken så att skrivskyddet bevaras
workbook.save("WriteProtectedWorkbook.xlsx")
# Validera lösenordet för att ändra med det korrekta lösenordet
is_correct_valid = workbook.settings.write_protection.validate_password("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Validera lösenordet för att ändra med ett felaktigt lösenord för att demonstrera den andra grenen
is_wrong_valid = workbook.settings.write_protection.validate_password("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
```

## Skydda och ta bort skydd för arbetsboksstruktur
Att skydda arbetsbokens struktur hindrar andra användare från att visa dolda kalkylblad, lägga till nya kalkylblad, flytta kalkylblad, ta bort kalkylblad, dölja kalkylblad eller byta namn på kalkylblad. Det skyddade tillståndet gäller bladstrukturen snarare än cellinnehållet i något blad. För att tillämpa strukturskydd, anropa `workbook.protect(ProtectionType.STRUCTURE, "password")`. För att ta bort skyddet, anropa `workbook.unprotect("password")` och ange rätt lösenord. Enumvärdet `ProtectionType.STRUCTURE` används här och är skilt från andra skyddstyper som `ProtectionType.WINDOWS`.

```python
import aspose.cells as ac
# Skapa en ny arbetsbok
workbook = ac.Workbook()
# Lägg till ett andra kalkylblad
workbook.worksheets.add()
# Skriv ett exempelvärde i cell A1 i det första kalkylbladet
workbook.worksheets[0].cells.get(0, 0).put_value("Sample Data")
# Skydda arbetsbokens struktur
workbook.protect(ac.ProtectionType.STRUCTURE, "StructPwd")
# Spara arbetsboken som structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Ladda om filen till en ny Workbook-instans
loaded_workbook = ac.Workbook(file_path)
# Ta bort struktskyddet
loaded_workbook.unprotect("StructPwd")
# Skriv ut bekräftelsemeddelande
print("Structure protection has been successfully removed from the workbook.")
```

## Skydda och ta bort skydd för kalkylblad
Kalkylbladsskydd låser cellerna i ett kalkylblad mot oavsiktliga eller avsiktliga ändringar. Användare kan inte redigera låsta celler utan att ange lösenordet. Detta är det typiska skyddet som används för att skydda formler, rubriker eller avsedda dataregistreringsområden i delade kalkylblad. För att skydda ett kalkylblad, anropa `worksheet.protect(ProtectionType.ALL, "password")`. Att använda `ProtectionType.ALL` aktiverar alla tillgängliga skyddsalternativ som att markera låsta celler, formatera celler, infoga rader och kolumner samt ta bort rader och kolumner. För att ta bort skyddet, anropa `worksheet.unprotect("password")` med rätt lösenord. Finkornigare kontroll är tillgänglig genom att kombinera andra skyddstyper som `Contents`, `Objects` och `Scenarios` med bitvis OR.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
sheet.cells.get("A1").put_value("Sample Data")
sheet.protect(ac.ProtectionType.ALL, "SheetPwd")
workbook.save("sheet_protected.xlsx")
workbook_reloaded = ac.Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.worksheets[0]
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
```

## Lägg till och validera digitala signaturer
En digital signatur försäkrar mottagarna om att arbetsbokens innehåll är autentiskt och inte har ändrats sedan det signerades. Aspose.Cells tillhandahåller stöd för digitala signaturer via namnrymden `aspose.cells.digital_signatures`. Det typiska arbetsflödet läser in en `.pfx`-certifikatfil via `System.Security.Cryptography.X509Certificates.X509Certificate2`, omsluter den i en `aspose.cells.digital_signatures.DigitalSignature`, lägger till signaturen i en `DigitalSignatureCollection` och tillämpar samlingen på arbetsboken via `workbook.add_digital_signature(DigitalSignatureCollection)`. Egenskapen `digital_signature.comments` kan registrera signeringskontext som signeringstid och syfte. Alla ändringar som görs i arbetsboken efter signering gör signaturen ogiltig, så ett valideringssteg på mottagarsidan kan upptäcka manipulering.

```python
from datetime import datetime
import aspose.cells as ac
from aspose.cells.digitalsignatures import DigitalSignature, DigitalSignatureCollection
with open("signature.pfx", "rb") as certificate_file:
    certificate = certificate_file.read()
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", datetime.now())
signatures = DigitalSignatureCollection()
signatures.add(signature)
workbook = ac.Workbook()
workbook.worksheets[0].cells.get("A1").put_value("Sample Value")
workbook.add_digital_signature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
```

## Relaterade artiklar
- [Kryptera och dekryptera Excel-filer](/cells/sv/python-net/encrypt-and-decrypt-excel-files/)
- [Skydda och ta bort skydd för arbetsboksstruktur](/cells/sv/python-net/protect-and-unprotect-workbook-structure/)
- [Skydda och ta bort skydd för kalkylblad](/cells/sv/python-net/protect-and-unprotect-worksheets/)
- [Lösenordsskydda eller ta bort skydd för delad arbetsbok](/cells/sv/python-net/password-protect-or-unprotect-the-shared-workbook/)
- [Tilldela och validera digitala signaturer](/cells/sv/python-net/assign-and-validate-digital-signatures/)
- [Kontrollera lösenord för att ändra med Aspose.Cells](/cells/sv/python-net/check-password-to-modify-using-aspose-cells/)
- [Identifiera filformat för krypterade Office Open XML - OOXML-filer](/cells/sv/python-net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Kryptera Excel-filer](/cells/sv/python-net/encrypting-excel-files/)
- [Hur man identifierar ett filformat och kontrollerar om filen är krypterad](/cells/sv/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="python-net" >}}