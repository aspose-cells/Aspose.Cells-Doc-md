---
title: Skydda och avskydda med C++
linktitle: Kryptering och skydd
description: Den här sektionen beskriver hur du krypterar och dekrypterar Excel-filer och skyddar Excel-data, inklusive filkryptering, skrivskydd, skydd av arbetsboksstruktur, kalkylbladsskydd och digitala signaturer med C++-kod
keywords: Aspose.Cells, Aspose.Cells for C++, kryptera, dekryptera, lösenord, skydda, ta bort skydd, arbetsboksskydd, kalkylbladsskydd, skrivskydd, digital signatur, C++
type: docs
weight: 68
url: /sv/cpp/protect-and-unprotect/
alias: [/cpp/security-features/]
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-arbetsböcker lagrar ofta känslig finansiell, affärs- eller personlig information som måste skyddas från obehörig åtkomst. Aspose.Cells for C++ erbjuder en omfattande uppsättning av skyddsfunktioner som återspeglar Microsoft Excels funktioner och som gör att du kan skydda dina data på filnivå, arbetsboksnivå och kalkylbladsnivå.

{{% alert color="primary" %}}
Aspose.Cells for C++ erbjuder ett brett utbud av skyddsfunktioner, från filnivå till datanivå, i likhet med MS Excel. Dessa funktioner omfattar att kryptera filer med ett lösenord, tvinga fram skrivskyddad åtkomst med ett lösenord för att ändra, skydda arbetsboksstrukturen, skydda kalkylblad och digitalt signera arbetsböcker.
{{% /alert %}}

## Kryptera och dekryptera Excel-filer
Ett lösenord som anges för en Excel-fil förhindrar obehöriga användare från att öppna eller visa arbetsbokens innehåll. För att kryptera en arbetsbok tilldelar du en lösenordssträng till `workbook.GetSettings().SetPassword()` och sparar sedan arbetsboken. Aspose.Cells skriver filen i krypterad form. För att öppna en krypterad arbetsbok för dekryptering instansierar du ett `LoadOptions`-objekt, anger `LoadOptions.SetPassword()` till samma lösenord som användes vid krypteringen och skickar det till `Workbook`-konstruktorn. Aspose.Cells tillämpar det angivna lösenordet transparent, så att resten av koden kan interagera med det dekrypterade innehållet som om filen vore en vanlig arbetsbok.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(u"Confidential Data");
    workbook.GetSettings().SetPassword(U16String("OpenPassword123"));
    workbook.Save(u"encrypted.xlsx");
    LoadOptions loadOptions;
    loadOptions.SetPassword(U16String("OpenPassword123"));
    Workbook decryptedWorkbook(u"encrypted.xlsx", loadOptions);
    U16String cellValue = decryptedWorkbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue();
    std::cout << "Decrypted cell A1 value: " << cellValue.ToUtf8() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Skrivskydd (lösenord för att ändra)
Excel stöder två olika lösenordstyper. Det första är ett lösenord för att öppna, som krypterar själva filen och beskrivs i föregående avsnitt. Det andra är ett lösenord för att ändra, som inte hindrar användare från att öppna arbetsboken. I stället rekommenderar Excel att filen öppnas i skrivskyddat läge om inte lösenordet för att ändra anges. Konfigurera det här beteendet i Aspose.Cells via `workbook.GetSettings().GetWriteProtection()`. Ange egenskapen `Password` till lösenordet för att ändra och egenskapen `Author` för att identifiera vem som tillämpade skyddet. Använd metoden `WriteProtection.ValidatePassword()` för att kontrollera om ett angivet lösenord för att ändra är korrekt. Metoden returnerar `true` vid en matchning och `false` annars.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    Cell a1 = cells.Get(u"A1");
    a1.PutValue(u"Sample Data");
    workbook.GetSettings().GetWriteProtection().SetPassword(u"ModifyPwd");
    workbook.GetSettings().GetWriteProtection().SetAuthor(u"AuthorName");
    workbook.Save(u"WriteProtectedWorkbook.xlsx");
    bool isCorrectValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"ModifyPwd");
    std::cout << "ValidatePassword(\"ModifyPwd\") returned: " << (isCorrectValid ? "True" : "False") << std::endl;
    bool isWrongValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"WrongPwd");
    std::cout << "ValidatePassword(\"WrongPwd\") returned: " << (isWrongValid ? "True" : "False") << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Skydda och ta bort skydd för arbetsboksstruktur
Att skydda arbetsboksstrukturen förhindrar andra användare från att visa dolda kalkylblad, lägga till nya kalkylblad, flytta kalkylblad, ta bort kalkylblad, dölja kalkylblad eller byta namn på kalkylblad. Skyddet gäller bladstrukturen och inte cellinnehållet i något blad. För att tillämpa strukturskydd anropar du `workbook.Protect(ProtectionType::Structure, "password")`. För att ta bort skyddet anropar du `workbook.Unprotect("password")` och anger rätt lösenord. Enum-värdet `ProtectionType::Structure` används här och skiljer sig från andra skyddstyper, till exempel `ProtectionType::Windows`.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Skapa en ny arbetsbok
    Workbook workbook;
    // Lägg till ett andra kalkylblad
    workbook.GetWorksheets().Add();
    // Skriv ett exempelvärde till cell A1 i det första kalkylbladet
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(u"Sample Data");
    // Skydda arbetsbokens struktur
    workbook.Protect(ProtectionType::Structure, u"StructPwd");
    // Spara arbetsboken som structure_protected.xlsx
    U16String filePath = u"structure_protected.xlsx";
    workbook.Save(filePath);
    // Ladda om filen i en ny Workbook-instans
    Workbook loadedWorkbook(filePath);
    // Ta bort struktskyddet
    loadedWorkbook.Unprotect(u"StructPwd");
    // Skriv ut bekräftelsemeddelande
    std::cout << "Structure protection has been successfully removed from the workbook." << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Skydda och ta bort skydd för kalkylblad
Kalkylbladsskydd låser cellerna i ett kalkylblad mot oavsiktliga eller avsiktliga ändringar. Användare kan inte redigera låsta celler utan att ange lösenordet. Detta är den typiska skyddsmetoden för att skydda formler, rubriker eller avsedda dataregistreringsområden i delade kalkylblad. För att skydda ett kalkylblad anropar du `worksheet.Protect(ProtectionType::All, "password")`. Att använda `ProtectionType::All` aktiverar alla tillgängliga skyddsalternativ, till exempel markering av låsta celler, formatering av celler, infogning av rader och kolumner samt borttagning av rader och kolumner. För att ta bort skyddet anropar du `worksheet.Unprotect("password")` med rätt lösenord. Mer detaljerad kontroll fås genom att kombinera andra skyddstyper, såsom `Contents`, `Objects` och `Scenarios`, med bitvis OR.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Data");
    sheet.Protect(ProtectionType::All, u"SheetPwd");
    workbook.Save(u"sheet_protected.xlsx");
    Workbook workbookReloaded(u"sheet_protected.xlsx");
    Worksheet sheetReloaded = workbookReloaded.GetWorksheets().Get(0);
    sheetReloaded.Unprotect(u"SheetPwd");
    std::cout << "Worksheet protection removed successfully.\n";
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Lägg till och validera digitala signaturer
En digital signatur intygar för mottagarna att arbetsbokens innehåll är autentiskt och inte har ändrats sedan det signerades. Aspose.Cells erbjuder stöd för digitala signaturer via namnrymden `Aspose::Cells::DigitalSignatures`. Det typiska arbetsflödet är att läsa in en `.pfx`-certifikatfil, skapa en `Aspose::Cells::DigitalSignatures::DigitalSignature` utifrån den, lägga till signaturen i en `DigitalSignatureCollection` och tillämpa samlingen på arbetsboken via `workbook.AddDigitalSignature(DigitalSignatureCollection)`. Egenskapen `DigitalSignature.GetComments()` kan användas för att registrera kontexten för signeringen, till exempel tidpunkten och syftet med signeringen. Varje ändring av arbetsboken efter signeringen ogiltigförklarar signaturen, så ett valideringssteg på mottagarsidan kan upptäcka manipulering.

```cpp
#include "Aspose.Cells.h"
#include <chrono>
#include <ctime>
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;
int main() {
    Aspose::Cells::Startup();
    std::time_t t = std::time(nullptr);
    std::tm tm{};
    localtime_s(&tm, &t);
    Date currentDate{0};
    currentDate.year = tm.tm_year + 1900;
    currentDate.month = tm.tm_mon + 1;
    currentDate.day = tm.tm_mday;
    currentDate.hour = tm.tm_hour;
    currentDate.minute = tm.tm_min;
    currentDate.second = tm.tm_sec;
    DigitalSignature signature(u"signature.pfx", u"pfx-password", u"Signed by Aspose.Cells", currentDate);
    DigitalSignatureCollection signatures;
    signatures.Add(signature);
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Value");
    workbook.AddDigitalSignature(signatures);
    workbook.Save(u"signed_workbook.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Relaterade artiklar
- [Kryptera och dekryptera Excel-filer](/cells/sv/cpp/encrypt-and-decrypt-excel-files/)
- [Skydda och ta bort skydd för arbetsboksstruktur](/cells/sv/cpp/protect-and-unprotect-workbook-structure/)
- [Skydda och ta bort skydd för kalkylblad](/cells/sv/cpp/protect-and-unprotect-worksheets/)
- [Lösenordsskydda eller ta bort skydd för delad arbetsbok](/cells/sv/cpp/password-protect-or-unprotect-the-shared-workbook/)
- [Kontrollera lösenord för att ändra med Aspose.Cells](/cells/sv/cpp/check-password-to-modify-using-aspose-cells/)
- [Identifiera filformat för krypterade Office Open XML - OOXML-filer](/cells/sv/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Kryptera Excel-filer](/cells/sv/cpp/encrypting-excel-files/)
- [Identifiera filformat och kontrollera om filen är krypterad](/cells/sv/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="cpp" >}}