---
title: Kryptera, dekryptera, skydda och avskydda Excel filer
linktitle: Kryptering och skydd
description: Den här delen beskriver hur du krypterar och dekrypterar Excel-filer och skyddar Excel-data samt täcker filkryptering, skrivskydd, strukturskydd för arbetsböcker, kalkylbladsskydd och digitala signaturer med Java-kod
keywords: Aspose.Cells, Java, kryptera, dekryptera, lösenord, skydda, ta bort skydd, arbetsboksskydd, kalkylbladsskydd, skrivskydd, digital signatur
type: docs
weight: 68
url: /sv/java/protect-and-unprotect/
alias: [/java/security-features/]
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-arbetsböcker lagrar ofta känslig finansiell, affärsrelaterad eller personlig information som måste skyddas mot obehörig åtkomst. Aspose.Cells for Java erbjuder en omfattande uppsättning skyddsfunktioner som motsvarar funktionerna i Microsoft Excel, så att du kan säkra dina data på fil-, arbetsboks- och kalkylbladsnivå.

{{% alert color="primary" %}}
Aspose.Cells for Java erbjuder ett brett utbud av skyddsfunktioner, från filnivå till datanivå, som liknar MS Excel. Funktionerna omfattar kryptering av filer med ett lösenord, skrivskyddad åtkomst genom ett lösenord för att ändra, skydd av arbetsboksstruktur, skydd av kalkylblad och digital signering av arbetsböcker.
{{% /alert %}}

## Kryptera och dekryptera Excel-filer
Ett lösenord som anges för en Excel-fil hindrar obehöriga användare från att öppna eller visa arbetsbokens innehåll. Om du vill kryptera en arbetsbok tilldelar du en lösenordssträng till `Workbook.Settings.Password` (som nås via `workbook.getSettings().setPassword(...)`) och sparar sedan arbetsboken. Aspose.Cells skriver filen i krypterad form. För att öppna en krypterad arbetsbok för dekryptering instansierar du ett `LoadOptions`-objekt, anger `LoadOptions.Password` (via `loadOptions.setPassword(...)`) till samma lösenord som användes vid kryptering och skickar det till `Workbook`-konstruktorn. Aspose.Cells tillämpar det angivna lösenordet transparent, så att resten av koden kan interagera med det dekrypterade innehållet som om filen vore en vanlig arbetsbok.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cell cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.setPassword("OpenPassword123");
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
System.out.println("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## Skrivskydd (lösenord för att ändra)
Excel stöder två separata lager av lösenord. Det första är ett lösenord för att öppna, som krypterar själva filen och behandlas i föregående avsnitt. Det andra är ett lösenord för att ändra, som inte hindrar användare från att öppna arbetsboken. I stället rekommenderar Excel att filen öppnas i skrivskyddat läge om inte lösenordet för att ändra anges. Konfigurera detta beteende i Aspose.Cells via `Workbook.Settings.WriteProtection` (som nås via `workbook.getSettings().getWriteProtection()`). Ange dess `Password`-egenskap (via `writeProtection.setPassword(...)`) till lösenordet för att ändra och dess `Author`-egenskap (via `writeProtection.setAuthor(...)`) för att ange vem som har tillämpat skyddet. Använd metoden `WriteProtection.validatePassword(String)` för att kontrollera om ett angivet lösenord för att ändra är korrekt. Den returnerar `true` vid en träff och `false` annars.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
workbook.save("WriteProtectedWorkbook.xlsx");
boolean isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
System.out.println("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
boolean isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
System.out.println("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Skydda och ta bort skydd för arbetsboksstrukturen
Om du skyddar arbetsboksstrukturen hindras andra användare från att visa dolda kalkylblad, lägga till nya kalkylblad, flytta kalkylblad, ta bort kalkylblad, dölja kalkylblad eller byta namn på kalkylblad. Det skyddade tillståndet gäller strukturen hos kalkylbladen och inte cellinnehållet i dem. För att tillämpa strukturskydd anropar du `workbook.protect(ProtectionType.STRUCTURE, "password")`. För att ta bort skyddet anropar du `workbook.unprotect("password")` och anger rätt lösenord. Enum-värdet `ProtectionType.STRUCTURE` används här och skiljer sig från andra skyddstyper som `ProtectionType.WINDOWS`.

```java
import com.aspose.cells.*;
// Skapa en ny arbetsbok
Workbook workbook = new Workbook();
// Lägg till ett andra kalkylblad
workbook.getWorksheets().add();
// Skriv ett exempelvärde till cell A1 i det första kalkylbladet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Skydda arbetsbokens struktur
workbook.protect(ProtectionType.STRUCTURE, "StructPwd");
// Spara arbetsboken som structure_protected.xlsx
String filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Ladda om filen till en ny Workbook-instans
Workbook loadedWorkbook = new Workbook(filePath);
// Ta bort strukturskyddet
loadedWorkbook.unprotect("StructPwd");
// Skriv ut bekräftelsemeddelande
System.out.println("Structure protection has been successfully removed from the workbook.");
```

## Skydda och ta bort skydd för kalkylblad
Kalkylbladsskydd låser cellerna i ett kalkylblad så att de inte ändras oavsiktligt eller avsiktligt. Användare kan inte redigera låsta celler utan att ange lösenordet. Det är det typiska skyddet som används för att skydda formler, rubriker eller avgränsade områden för datainmatning i delade kalkylblad. För att skydda ett kalkylblad anropar du `worksheet.protect(ProtectionType.ALL, "password")`. `ProtectionType.ALL` aktiverar alla tillgängliga skyddsalternativ, till exempel att välja låsta celler, formatera celler, infoga rader och kolumner samt ta bort rader och kolumner. För att ta bort skyddet anropar du `worksheet.unprotect("password")` med rätt lösenord. Finkornigare kontroll fås genom att kombinera andra skyddstyper, till exempel `CONTENTS`, `OBJECTS` och `SCENARIOS`, med bitvis OR.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(ProtectionType.ALL, "SheetPwd", "SheetPwd");
workbook.save("sheet_protected.xlsx");
Workbook workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
System.out.println("Worksheet protection removed successfully.");
```

## Lägg till och validera digitala signaturer
En digital signatur intygar för mottagarna att arbetsbokens innehåll är autentiskt och inte har ändrats sedan det signerades. Aspose.Cells erbjuder stöd för digitala signaturer via paketet `com.aspose.cells.DigitalSignatures`. Det typiska arbetsflödet läser in en `.pfx`-certifikatfil via Java:s säkerhets-API:er (till exempel `java.security.KeyStore` och `java.security.cert.X509Certificate`), omsluter den i en `com.aspose.cells.DigitalSignatures.DigitalSignature`, lägger till signaturen i en `DigitalSignatureCollection` och tillämpar samlingen på arbetsboken via `workbook.addDigitalSignature(DigitalSignatureCollection)`. Egenskapen `DigitalSignature.getComments()` kan användas för att dokumentera signeringssammanhang, till exempel tidpunkten och syftet med signeringen. Alla ändringar som görs i arbetsboken efter signeringen gör signaturen ogiltig, så ett valideringssteg på mottagarsidan kan upptäcka manipulation.

```java
import com.aspose.cells.*;
import java.io.FileInputStream;
import java.security.KeyStore;
KeyStore pfxKeyStore = KeyStore.getInstance("PKCS12");
pfxKeyStore.load(new FileInputStream("signature.pfx"), "pfx-password".toCharArray());
DigitalSignature signature = new DigitalSignature(pfxKeyStore, "pfx-password", "Signed by Aspose.Cells", new DateTime());
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.add(signature);
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
System.out.println("The workbook has been digitally signed.");
```

## Relaterade artiklar
- [Kryptera och dekryptera Excel-filer](/cells/sv/java/encrypt-and-decrypt-excel-files/)
- [Skydda och ta bort skydd för arbetsboksstrukturen](/cells/sv/java/protect-and-unprotect-workbook-structure/)
- [Skydda och ta bort skydd för kalkylblad](/cells/sv/java/protect-and-unprotect-worksheet/)
- [Skydda den delade arbetsboken med lösenord eller ta bort skyddet](/cells/sv/java/password-protect-or-unprotect-the-shared-workbook/)
- [Tilldela och validera digitala signaturer](/cells/sv/java/assign-and-validate-digital-signatures/)
- [Identifiera filformat för krypterade Office Open XML - OOXML-filer](/cells/sv/java/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Så här identifierar du ett filformat och kontrollerar om filen är krypterad](/cells/sv/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="java" >}}