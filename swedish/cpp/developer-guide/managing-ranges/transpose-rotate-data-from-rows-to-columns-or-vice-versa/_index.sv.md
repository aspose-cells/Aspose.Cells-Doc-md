---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for C++ with three different approaches.
linktitle: Transponera intervall
url: /sv/cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, C++-bibliotek, kalkylblad, transponera intervall, rotera data, transponeringsfunktion, dynamisk matrisformel, matrisformel, Excel TRANSPOSE, rader till kolumner
type: docs
weight: 80
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for C++ stöder transponering (rotering) av data så att rader blir kolumner och kolumner blir rader på tre olika sätt. Den första metoden använder den inbyggda `Range.Transpose()`-metoden och fungerar i alla versioner av Excel, medan den andra använder `Cell.SetDynamicArrayFormula()` för att skriva en modern dynamisk matrisformel `=TRANSPOSE(...)` som spills automatiskt i Excel 365 eller Excel 2021. Den tredje metoden använder `Cell.SetArrayFormula()` för att skriva en klassisk Ctrl+Shift+Enter (CSE) matrisformel som är kompatibel med äldre Excel-versioner. Den här artikeln går igenom varje metod med stegvisa instruktioner och kompletta kodexempel.
{{% /alert %}}

## **Introduktion**
Att transponera ett intervall innebär att man roterar det så att det som var en rad blir en kolumn och det som var en kolumn blir en rad, vilket effektivt speglar data över dess huvuddiagonal. I Microsoft Excel utför kalkylbladsfunktionen `TRANSPOSE` denna operation, och den konceptuella referensen finns dokumenterad på [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Samma idé kan användas programmatiskt på ett intervall av celler, vilket är användbart i många affärs- och rapporteringsscenarier.
Vanliga scenarier där transponering är användbar inkluderar följande.
- Omorientering av kvartals- eller årsrapporter där kvartal normalt löper över sidan och regioner nerför sidan, eller tvärtom.
- Byta axelorientering i dashboards eller diagram så att en tidsserie löper nerför sidan istället för över.
- Omforma data som importerats från externa system så att det matchar layouten som förväntas av nedströmsanalys- eller rapporteringsmallar.
För att göra resten av artikeln konkret använder varje exempel följande lilla tabell över försäljning per region per kvartal. I exempelarbetsboken upptar denna tabell intervallet **A1:D5**, med **A1** lämnad tom som det övre vänstra hörnet, **B1:D1** innehåller regionrubrikerna, och **A2:A5** innehåller kvartalsrubrikerna.
| Region            | Europe    | Asien     | Nordamerika |
|-------------------|-----------|-----------|-------------|
| Qtr 1             | 21704714  | 8774099   | 12094215    |
| Qtr 2             | 17987034  | 12214447  | 10873099    |
| Qtr 3             | 19485029  | 14356879  | 15689543    |
| Qtr 4             | 22567894  | 15763492  | 17456723    |
Artikeln presenterar sedan tre olika sätt att transponera dessa data med Aspose.Cells for C++, var och ett lämpat för en annan Excel-version och användningsfall.

## **Metod 1 — Transponera intervall på plats (Range.Transpose)**
Använd denna metod när du vill transponera data utan att använda kalkylbladsfunktionen `TRANSPOSE`. Den fungerar i **alla versioner av Excel** och har inget beroende av dynamiska matriser, vilket gör den till det säkraste kompatibilitetsalternativet över versioner. Den är idealisk när du bara behöver det slutliga transponerade resultatet och inte behöver behålla den ursprungliga `TRANSPOSE`-formeln i arbetsboken.

### **API som används**
`Range.Transpose()` är en instansmetod på klassen `Aspose.Cells.Range`. Genom att anropa den vänds intervallet på plats genom att byta dess rader och kolumner, så det som var en rad blir en kolumn och det som var en kolumn blir en rad. Metoden modifierar de underliggande cellerna direkt utan att skriva någon formel.

### **Steg**
1. Öppna källarbetsboken med `LoadOptions` inställt på `.xlsx`-format genom att skapa en `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. Hämta det första kalkylbladet från arbetsboken med `workbook.GetWorksheets().Get(0)`.
3. Kom åt kalkylbladets cellsamling via `worksheet.GetCells()`.
4. Skapa källintervallet som täcker **A1:D5** genom att anropa `cells.CreateRange(u"A1:D5")`.
5. Anropa `source.Transpose()` för att rotera intervallet på plats, så att rader och kolumner byter plats.
6. Spara arbetsboken med `workbook.Save(outputFile)`.
Efter transponeringen håller samma ankarrintervall den roterade datan. Den första raden läser (tom, **Europa**, **Asien**, **Nordamerika**) och den första kolumnen läser (tom, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Varje ursprunglig kolumn av försäljning blir en rad i det transponerade intervallet.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    U16String srcFile(u"source.xlsx");
    U16String outputFile(u"transposed.xlsx");
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(srcFile, loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Range source = cells.CreateRange(u"A1:D5");
    source.Transpose();
    workbook.Save(outputFile);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Metod 2 — Transponera med dynamisk matrisformel (Excel 365 / 2021)**
Använd denna metod när du vill bevara formeln `=TRANSPOSE(A1:D5)` som en levande formel i utdataarbetsboken så att resultatet uppdateras automatiskt om källdatan ändras, och målets Excel-fil kommer att öppnas i **Excel 365 / Excel 2021 eller senare** där dynamiska matriser och spilloperatorn stöds.

### **API som används**
`Cell.SetDynamicArrayFormula(const char* formula, FormulaParseOptions options, bool calculateValue)` är en metod på `Aspose.Cells.Cell` som sätter cellens formel som en **dynamisk matrisformel**. Excel utvärderar formeln en gång och spills automatiskt resultatet till de omgivande cellerna. Den tredje parametern, när den sätts till `true`, instruerar Aspose.Cells att också beräkna de resulterande värdena vid skrivningstillfället.

### **Steg**
1. Ladda källarbetsboken genom att konstruera `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. Hämta det första kalkylbladet via `workbook.GetWorksheets().Get(0)` och kom åt dess `Cells`-samling via `worksheet.GetCells()`.
3. Placera den dynamiska matrisformeln i cell **A6**, precis under källintervallet, genom att anropa `cells.Get(u"A6").SetDynamicArrayFormula(u"=TRANSPOSE(A1:D5)", nullptr, true)`.
4. Argumentet `nullptr` skickar standardinställda `FormulaParseOptions`, och det tredje argumentet `true` säger åt Aspose.Cells att behandla formeln som en dynamisk matris och att utvärdera den så att de spillda värdena skrivs till arbetsboken.
5. Spara arbetsboken med `workbook.Save(outputFile)`.
Cell **A6** innehåller formeln `=TRANSPOSE(A1:D5)` och Excel spills automatiskt resultatet till regionen **A6:D10**, ett block på 5 rader gånger 4 kolumner lika med den transponerade datan.

{{% alert color="primary" %}}
Denna metod fungerar **endast i Excel 365 / 2021 eller senare**. Äldre Excel-versioner kommer inte att spillda dynamiska matrisformler korrekt.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    std::string srcFile = "source.xlsx";
    std::string outFile = "output_transpose_dynamic.xlsx";
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(U16String(srcFile.c_str()), loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(u"A6");
    FormulaParseOptions options;
    cell.SetDynamicArrayFormula(U16String("=TRANSPOSE(A1:D5)"), options, true);
    workbook.Save(U16String(outFile.c_str()), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Metod 3 — Transponera med klassisk matrisformel (CSE)**
Använd denna metod när du vill att en `TRANSPOSE`-formel ska bevaras i arbetsboken men målets Excel-fil kan öppnas i **äldre Excel-versioner (före 2021, inklusive 2019, 2016, 2013 och så vidare)** där dynamisk matris-spilling inte stöds. Den klassiska CSE (Ctrl+Shift+Enter) matrisformeln är det bakåtkompatibla alternativet som alla Excel-versioner kan utvärdera.

### **API som används**
`Cell.SetArrayFormula(const char* arrayFormula, int nRows, int nColumns)` är en metod på `Aspose.Cells.Cell` som tilldelar en **klassisk matrisformel (CSE)** till ankarcellen och deklarerar dimensionerna på den resulterande matrisen. Aspose.Cells skriver markören för flercells-matrisformel så att Excel utvärderar formeln som ett enda matrisuttryck som fyller det deklarerade intervallet.

### **Steg**
1. Ladda källarbetsboken på samma sätt som i de tidigare metoderna, genom att konstruera `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. Hämta det första kalkylbladet via `workbook.GetWorksheets().Get(0)` och kom åt dess `Cells`-samling via `worksheet.GetCells()`.
3. Anropa `cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5)`. Det andra argumentet `4` är antalet rader i destinationsmatrisen och det tredje argumentet `5` är antalet kolumner.
4. Spara arbetsboken med `workbook.Save(outputFile)`.
Cell **A6** är ankaret för matrisformeln och den utvärderade matrisen sträcker sig över 4 rader gånger 5 kolumner med start från A6, vilket matchar de transponerade dimensionerna av A1:D5-källan. Excel skriver en enda matrisformelsmarkör över det resulterande intervallet så att äldre Excel-versioner utvärderar det korrekt.

{{% alert color="primary" %}}
CSE-matrisformler är det klassiska Excel-sättet att utvärdera ett `TRANSPOSE`-uttryck och denna metod är universellt kompatibel över Excel-versioner.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Ladda källarbetsboken med xlsx LoadOptions
    std::string srcFile = "source.xlsx";
    Workbook workbook(U16String(srcFile.c_str()), LoadOptions(LoadFormat::Xlsx));
    // Få åtkomst till det första kalkylbladet och dess Cells-samling
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Ställ in den klassiska CSE-matrisformeln på cell A6.
    // Formeln =TRANSPOSE(A1:D5) roterar källintervallet med 5 rader x 4 kolumner
    // till en 4-rad x 5-kolumns matris. Det andra argumentet (4) är antalet rader
    // och det tredje argumentet (5) är antalet kolumner i den resulterande matrisen.
    // Aspose.Cells skriver CSE-matrisformelmarkeringen så att Excel utvärderar den som
    // en enda flercelligs matrisformel, kompatibel med äldre Excel-versioner
    // (2019, 2016, 2013, etc.) som inte stöder dynamisk matrisläckage.
    cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5);
    // Spara arbetsboken så att matrisformelmarkeringen bevaras
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Jämförelse — När man ska använda varje metod**
| Metod | API / Metod | Excel-version | Källformel bevarad? | Utdataintervall |
|----------|--------------|---------------|--------------------------|--------------|
| Metod 1 — Transponering på plats | `Range.Transpose()` | Alla Excel-versioner | Nej (endast värden) | Samma ankarrintervall, 5×4 |
| Metod 2 — Dynamisk matrisformel | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | Ja (spillds dynamiskt) | Spillat från ankaret |
| Metod 3 — Klassisk matrisformel (CSE) | `Cell.SetArrayFormula` | Alla Excel-versioner | Ja (flercells-matrisformel) | Explicit storlek, 4×5 |
Använd **Metod 1** när du behöver en snabb, kompatibel transformation över versioner och bara behöver de transponerade värdena skrivna till filen. Använd **Metod 2** när modern Excel är garanterad och du vill att formeln ska förbli levande och uppdateras om källan ändras. Använd **Metod 3** när du behöver den bredaste kompatibiliteten med en bevarad formel över alla Excel-versioner, inklusive de äldre versionerna som inte stöder dynamiska matriser.

## **Relaterade artiklar**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for C++](/cells/sv/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Infoga en bild i en cell](/cells/sv/cpp/inserting-an-image-into-a-cell/)
- [Dela Excel-filer i flera filer](/cells/sv/cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="" >}}