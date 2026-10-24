---
title: Skydda och Hävda skydd
linktitle: Skydd
description: Det här avsnittet introducerar hur man krypterar och dekrypterar Excel-filer och skyddar Excel-data, inklusive filkryptering, skrivskydd, skydd av arbetsboksstruktur, skydd av kalkylblad och digitala signaturer med Python-kod
keywords: Aspose.Cells, Python via Java, kryptera, dekryptera, lösenord, skydda, ta bort skydd, arbetsboksskydd, kalkylbladsskydd, skrivskydd, digital signatur, Python
type: docs
weight: 68
url: /sv/python-java/protect-and-unprotect/
alias: [/python-java/security-features/]
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-arbetsböcker lagrar ofta känslig finansiell, affärsrelaterad eller personlig information som måste skyddas från obehörig åtkomst. Aspose.Cells for Python via Java tillhandahåller en omfattande uppsättning skyddsfunktioner som speglar funktionaliteten i Microsoft Excel, vilket gör att du kan säkra dina data på filnivå, arbetsboksnivå och kalkylbladsnivå.

{{% alert color="primary" %}}
Aspose.Cells for Python via Java erbjuder ett brett utbud av skyddsfunktioner, från filnivå till datanivå, i likhet med MS Excel. Dessa funktioner omfattar kryptering av filer med ett lösenord, tvingande av skrivskyddad åtkomst via ett lösenord för att ändra, skydd av arbetsbokens struktur, skydd av kalkylblad och digital signering av arbetsböcker.
{{% /alert %}}

## Kryptera och dekryptera Excel-filer
Ett lösenord som anges för en Excel-fil förhindrar obehöriga användare från att öppna eller visa arbetsbokens innehåll. För att kryptera en arbetsbok tilldelar du en lösenordssträng till `workbook.getSettings().setPassword(...)` och sparar sedan arbetsboken. Aspose.Cells skriver filen i krypterad form. För att öppna en krypterad arbetsbok för dekryptering instansierar du ett `LoadOptions`-objekt, ställer in lösenordet via `load_options.setPassword(...)` till samma lösenord som användes vid krypteringen och skickar det till `Workbook`-konstruktorn. Aspose.Cells tillämpar det angivna lösenordet transparent så att resten av din kod kan interagera med det dekrypterade innehållet som om filen var en vanlig arbetsbok.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cell, LoadOptions
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cell = sheet.getCells().get("A1")
cell.putValue("Confidential Data")
workbook.getSettings().setPassword("OpenPassword123")
workbook.save("encrypted.xlsx")
load_options = LoadOptions()
load_options.setPassword("OpenPassword123")
decrypted_workbook = Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.getWorksheets().get(0).getCells().get("A1").getStringValue())
jpype.shutdownJVM()
```

## Skrivskydd (lösenord för att ändra)
Excel stöder två separata lösenordslager. Det första är ett lösenord för att öppna, vilket krypterar själva filen och behandlas i föregående avsnitt. Det andra är ett lösenord för att ändra, vilket inte hindrar användare från att öppna arbetsboken; i stället rekommenderar Excel att filen öppnas i skrivskyddat läge om inte lösenordet för att ändra anges. Konfigurera detta beteende i Aspose.Cells via `workbook.getSettings().getWriteProtection()`. Ställ in lösenordet via `setPassword(...)` till lösenordet för att ändra och författaren via `setAuthor(...)` för att identifiera vem som tillämpade skyddet. Använd metoden `writeProtection.validatePassword(String)` för att kontrollera om ett angivet lösenord för att ändra är korrekt, vilket returnerar `true` vid matchning och `false` annars.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Skapa en ny arbetsbok från grunden
workbook = Workbook()
# Skriv ett exempelvärde till cell A1 i det första kalkylbladet
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data")
# Konfigurera skrivskyddet: ange lösenordet för att ändra och författaren
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd")
workbook.getSettings().getWriteProtection().setAuthor("AuthorName")
# Spara arbetsboken så att skrivskyddet sparas
workbook.save("WriteProtectedWorkbook.xlsx")
# Validera lösenordet för att ändra med rätt lösenord
is_correct_valid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Validera lösenordet för att ändra med ett felaktigt lösenord för att demonstrera den andra grenen
is_wrong_valid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
jpype.shutdownJVM()
```

## Skydda och ta bort skydd för arbetsboksstruktur
Att skydda arbetsbokens struktur förhindrar andra användare från att visa dolda kalkylblad, lägga till nya kalkylblad, flytta kalkylblad, ta bort kalkylblad, dölja kalkylblad eller byta namn på kalkylblad. Det skyddade tillståndet gäller bladstrukturen snarare än cellinnehållet i något blad. För att tillämpa strukturskydd anropar du `workbook.protect(ProtectionType.STRUCTURE, "password")`. För att ta bort skyddet anropar du `workbook.unprotect("password")` och anger rätt lösenord. Enumvärdet `ProtectionType.STRUCTURE` används här och är skilt från andra skyddstyper såsom `ProtectionType.WINDOWS`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, ProtectionType
# Skapa en ny arbetsbok
workbook = Workbook()
# Lägg till ett andra kalkylblad
workbook.getWorksheets().add()
# Skriv ett exempelvärde till cell A1 i det första kalkylbladet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data")
# Skydda arbetsbokens struktur
workbook.protect(ProtectionType.STRUCTURE, "StructPwd")
# Spara arbetsboken som structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Ladda om filen till en ny Workbook-instans
loaded_workbook = Workbook(file_path)
# Ta bort strukturskyddet
loaded_workbook.unprotect("StructPwd")
# Skriv ut bekräftelsemeddelande
print("Structure protection has been successfully removed from the workbook.")
jpype.shutdownJVM()
```

## Skydda och ta bort skydd för kalkylblad
Kalkylbladsskydd låser cellerna i ett kalkylblad mot oavsiktliga eller avsiktliga ändringar. Användare kan inte redigera låsta celler utan att ange lösenordet. Detta är det typiska skyddet som används för att skydda formler, rubriker eller angivna dataregistreringsområden i delade kalkylblad. För att skydda ett kalkylblad anropar du `worksheet.protect(ProtectionType.ALL, "password")`. Att använda `ProtectionType.ALL` aktiverar alla tillgängliga skyddsalternativ som att välja låsta celler, formatera celler, infoga rader och kolumner samt ta bort rader och kolumner. För att ta bort skyddet anropar du `worksheet.unprotect("password")` med rätt lösenord. Finkornigare kontroll är tillgänglig genom att kombinera andra skyddstyper som `ProtectionType.CONTENTS`, `ProtectionType.OBJECTS` och `ProtectionType.SCENARIOS` med bitvis OR.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, ProtectionType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sample Data")
worksheet.protect(ProtectionType.ALL, "SheetPwd", None)
workbook.save("sheet_protected.xlsx")
workbook_reloaded = Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.getWorksheets().get(0)
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
jpype.shutdownJVM()
```

## Lägg till och validera digitala signaturer
En digital signatur försäkrar mottagarna om att arbetsbokens innehåll är autentiskt och inte har ändrats sedan det signerades. Aspose.Cells erbjuder stöd för digitala signaturer via namnrymden `Aspose.Cells.DigitalSignatures`. Det typiska arbetsflödet läser in en `.pfx`-certifikatfil via `java.security.KeyStore`, omsluter den i en `Aspose.Cells.DigitalSignatures.DigitalSignature`, lägger till signaturen i en `DigitalSignatureCollection` och tillämpar samlingen på arbetsboken via `workbook.addDigitalSignature(digitalSignatureCollection)`. Egenskapen `digitalSignature.getComments()` kan registrera signeringskontext såsom signeringstid och syfte. Alla ändringar som görs i arbetsboken efter signeringen ogiltigförklarar signaturen, så ett valideringssteg på mottagarsidan kan upptäcka manipulering.

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, DigitalSignature, DigitalSignatureCollection
from java.security import KeyStore
from java.io import FileInputStream
from java.util import Date
# Ladda certifikat från PFX-fil med Java KeyStore
key_store = KeyStore.getInstance("PKCS12")
fis = FileInputStream("signature.pfx")
key_store.load(fis, "pfx-password")
fis.close()
# Hämta certifikatet
alias = key_store.aliases().nextElement()
certificate = key_store.getCertificate(alias)
# Skapa digital signatur
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", Date())
signatures = DigitalSignatureCollection()
signatures.add(signature)
# Skapa arbetsbok och lägg till signatur
workbook = Workbook()
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value")
workbook.addDigitalSignature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
jpype.shutdownJVM()
```

## Relaterade artiklar
- [Kryptera och dekryptera Excel-filer](/cells/sv/python-java/encrypt-and-decrypt-excel-files/)
- [Skydda och ta bort skydd för arbetsboksstruktur](/cells/sv/python-java/protect-and-unprotect-workbook-structure/)
- [Skydda och ta bort skydd för kalkylblad](/cells/sv/python-java/protect-and-unprotect-worksheet/)
- [Kontrollera lösenord för att ändra med Aspose.Cells](/cells/sv/python-java/check-password-to-modify-using-aspose-cells/)

{{< app/cells/assistant language="python" >}}